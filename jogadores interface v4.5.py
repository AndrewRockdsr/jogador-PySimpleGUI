from multiprocessing import Event
import PySimpleGUI as sg
from time import sleep


def Verifica():
    layout = [
        [sg.Text('Clique em um dos botões para cadastro ou visualização de jogadores')],
        [sg.Button('CADASTRO'), sg.Button('VISUALIZAÇÃO')]
    ] 
    
    return sg.Window('', layout=layout, finalize=True)

def TelaDados():
    linha = [
        [sg.Text(f'Gols {c}ª partida'), sg.Input(key='gol')]
    ]
    layout = [
        [sg.Text('Nome do jogador '), sg.Input(key='nome')],
        [sg.Text('Posição '), sg.Input(key='posi')],
        [sg.Text('Idade'), sg.Input(key='idade')],
        [sg.Text('Partidas '), sg.Input(key='partidas')],
        [sg.Frame('Gols', layout=linha, key='container')],
        [sg.Button('Enviar'), sg.Button('Voltar')]
    ]
    return sg.Window('Jogador', layout=layout, finalize=True)

indice = 0
def DadosGerais():
    linha0 = [
        [sg.Text('')]
    ]
    layout2 = [
        [sg.Frame('Lista de jogadores', layout=linha0, key='ddg')],
        [sg.Button('Mostrar Lista'), sg.Button('Sair'), sg.Button('Voltar')]
    ]
    

    
    return sg.Window('Jogadore cadastrados', layout=layout2, finalize=True)

def Dados():
    layout = [
        [sg.Text(f'O jogador {jogador["nome"]} tem {jogador["idade"]} anos de idade e jogou {jogador["pts"]} partidas.')],
        [sg.Text(f'Joga na posição {jogador["posi"]} e marcou no total {sum(jogador["gols"])} gols')],
        [sg.Text(f'Media de {jogador["media"]:.2f} gols por partida. ')],
        [sg.Button('Confirmar'), sg.Button('Reescrever')]
    ]
    
    return sg.Window('CONFIMAR DADOS', layout=layout, finalize=True)




lista = []
jogador = {
    'nome':'',
    'idade':'',
    'posi':'',
    'pts':'',
    'gols':'',
    'media':''
}

jogadores = []

c = 1
c1 = 0

while True:
    JanelaVerifica = Verifica()
    c = 1
    c1 = 0
    EventVerifica, ValueVerifica = JanelaVerifica.read()
    if EventVerifica == sg.WINDOW_CLOSED:
        break
    if EventVerifica == 'CADASTRO':
        JanelaVerifica.close()
        
        while True: 
            JanelaTelaDados = TelaDados()
            EventTelaDados, ValueTelaDados = JanelaTelaDados.read()
            if EventTelaDados == sg.WINDOW_CLOSED or EventTelaDados == 'Voltar':
                JanelaTelaDados.close()
                break
            jogador['nome'] = ValueTelaDados['nome'].title().strip()
            jogador['idade'] = int(ValueTelaDados['idade'])
            jogador['posi'] = ValueTelaDados['posi'].strip().upper()
            partidas = int(ValueTelaDados['partidas'])
            jogador['pts'] = partidas
            if c == 1:
                lista.append(int(ValueTelaDados['gol']))
            if c > 1:
                lista.append(int(ValueTelaDados[f'gol{c1}']))
                c1 = c1 + 1
            if EventTelaDados == 'Enviar' and partidas > 0:
                c = c+1
                JanelaTelaDados.extend_layout(JanelaTelaDados['container'], [[sg.Text(f'Gols {c}ª partida'), sg.Input(key='gol')]])
                if c > partidas:
                    jogador['gols'] = lista.copy()
                    jogador['media'] = sum(jogador['gols']) / jogador['pts']
                    lista.clear()
                    JanelaTelaDados.close()
                    c = 1
                    while True:
                        JanelaDados = Dados()
                        EventDados, ValueDados = JanelaDados.read()
                        if EventDados == sg.WINDOW_CLOSED:
                            break
                        if EventDados == "Confirmar":
                            jogadores.append(jogador.copy())
                            print(jogadores)
                            JanelaDados.close()
                            break
                        if EventDados == "Reescrever":
                            JanelaDados.close()
                            break
                    break
    if EventVerifica == 'VISUALIZAÇÃO':
        indice1 = 0
        indice = 0
        JanelaVerifica.close()
        JanelaDadosGerais = DadosGerais()
        while True:
            EventDadosGerais, valueDadosGerais = JanelaDadosGerais.read()
            if EventDadosGerais == sg.WINDOW_CLOSED or EventDadosGerais == 'Voltar':
                JanelaDadosGerais.close()
                break
            if EventDadosGerais == 'Sair':
                JanelaDadosGerais.close()
                break
            if EventDadosGerais == 'Mostrar Lista' and len(jogadores) == 0 and indice1 == 0:
                indice1 = 1
                JanelaDadosGerais.extend_layout(JanelaDadosGerais['ddg'], [[sg.Text(' SEM JOGADORES CADASTRADOS')]])
            if EventDadosGerais == 'Mostrar Lista' and indice < len(jogadores):
                for c in range(0, len(jogadores)):
                    JanelaDadosGerais.extend_layout(JanelaDadosGerais['ddg'], [[sg.Text(f'\nNome: {jogadores[indice]["nome"]}\nIdade: {jogadores[indice]["idade"]}\nPosição: {jogadores[indice]["posi"]}\nTotal de gols: {sum(jogadores[indice]["gols"])}\nMedia por partida: {jogadores[indice]["media"]:.2f}')]])
                    indice = indice + 1
