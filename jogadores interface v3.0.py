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


while True:
    janela3 = veri1()
    event3, value3 = janela3.read()
    if event3 == sg.WINDOW_CLOSED:
        break
    if event3 == 'Continuar':
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
    if event3 == 'Sair':
        break

