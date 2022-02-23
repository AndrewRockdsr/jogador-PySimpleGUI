import PySimpleGUI as sg
c = 1

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
    
    return sg.Window('Todo List', layout=layout, finalize=True)


def Dados():
    layout = [
        [sg.Text(f'O jogador {jogador["nome"]} tem {jogador["idade"]} anos de idade e jogou {jogador["pts"]} partidas.')],
        [sg.Text(f'Joga na posição {jogador["posi"]} e marcou no total {sum(jogador["gols"])} gols')]
    ]
    
    return sg.Window('DADOS', layout=layout, finalize=True)


janela = TelaDados()

lista = []
jogador = {
    'nome':'',
    'idade':'',
    'posi':'',
    'pts':'',
    'gols':'',
    'media':''
}

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
            break

jogador['gols'] = lista.copy()
lista.clear()
janela.close()
janela2 = Dados()
janela2.read()
jogador['media'] = sum(jogador['gols']) / jogador['pts']
print(jogador)