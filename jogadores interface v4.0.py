import PySimpleGUI as sg
from time import sleep


def veri1():
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
        [sg.Button('Enviar')]
    ]
    return sg.Window('Jogador', layout=layout, finalize=True)

indice = 0
def DadosGerais():
    linha0 = [
        [sg.Text('')]
    ]
    layout2 = [
        [sg.Frame('Lista de jogadores', layout=linha0, key='ddg')],
        [sg.Button('Mostrar Lista'), sg.Button('Sair')]
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
    c = 1
    c1 = 0
    janela3 = veri1()
    event3, value3 = janela3.read()
    if event3 == sg.WINDOW_CLOSED:
        break
    if event3 == 'CADASTRO':
        janela3.close()
        janela = TelaDados()
        while True: 
            event, value = janela.read()
            jogador['nome'] = value['nome'].title().strip()
            jogador['idade'] = int(value['idade'])
            jogador['posi'] = value['posi'].strip().upper()
            partidas = int(value['partidas'])
            jogador['pts'] = partidas
            if c == 1:
                lista.append(int(value['gol']))
            if c > 1:
                lista.append(int(value[f'gol{c1}']))
                c1 = c1 + 1
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Enviar' and partidas > 0:
                c = c+1
                janela.extend_layout(janela['container'], [[sg.Text(f'Gols {c}ª partida'), sg.Input(key='gol')]])
                if c > partidas:
                    jogador['gols'] = lista.copy()
                    jogador['media'] = sum(jogador['gols']) / jogador['pts']
                    lista.clear()
                    janela.close()
                    c = 1
                    while True:
                        janela2 = Dados()
                        event2, value2 = janela2.read()
                        if event2 == sg.WINDOW_CLOSED:
                            break
                        if event2 == "Confirmar":
                            jogadores.append(jogador.copy())
                            print(jogadores)
                            janela2.close()
                            break
                        if event2 == "Reescrever":
                            janela2.close()
                            break
                    break
    if event3 == 'VISUALIZAÇÃO':
        indice1 = 0
        indice = 0
        janela3.close()
        janela5 = DadosGerais()
        while True:
            event5, value5 = janela5.read()
            if event5 == sg.WINDOW_CLOSED:
                break
            if event5 == 'Sair':
                janela5.close()
                break
            if event5 == 'Mostrar Lista' and len(jogadores) == 0 and indice1 == 0:
                indice1 = 1
                janela5.extend_layout(janela5['ddg'], [[sg.Text(' SEM JOGADORES CADASTRADOS')]])
            if event5 == 'Mostrar Lista' and indice < len(jogadores):
                for c in range(0, len(jogadores)):
                    janela5.extend_layout(janela5['ddg'], [[sg.Text(f'\nNome: {jogadores[indice]["nome"]}\nIdade: {jogadores[indice]["idade"]}\nPosição: {jogadores[indice]["posi"]}\nTotal de gols: {sum(jogadores[indice]["gols"])}\nMedia por partida: {jogadores[indice]["media"]:.2f}')]])
                    indice = indice + 1
