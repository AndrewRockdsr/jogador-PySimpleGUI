import PySimpleGUI as sg
c = 1

def veri1():
    layout = [
        [sg.Text('Para continuar e adicionar jogador clique em continuar')],
        [sg.Button('Continuar'), sg.Button('Sair')]
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


def Dados():
    layout = [
        [sg.Text(f'O jogador {jogador["nome"]} tem {jogador["idade"]} anos de idade e jogou {jogador["pts"]} partidas.')],
        [sg.Text(f'Joga na posição {jogador["posi"]} e marcou no total {sum(jogador["gols"])} gols')],
        [sg.Text(f'Media de {jogador["media"]:.2f} gols por partida. ')]
    ]
    
    return sg.Window('DADOS', layout=layout, finalize=True)




lista = []
jogador = {
    'nome':'',
    'idade':'',
    'posi':'',
    'pts':'',
    'gols':'',
    'media':''
}

janela3 = veri1()
while True:
    event, value = janela3.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Continuar':
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
            else:
                lista.append(int(value[f'gol{c-2}']))
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
                    break
    
    elif event == 'Sair':
        break

janela2 = Dados()
janela2.read()
