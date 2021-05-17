
name1 = input("Insira o nome do jogador 1: ")
print("O jogador "+name1 + " é assinalado pelo X")
name2 = input("Insira o nome do jogador 2: ")
print("O jogador "+name2 + " é assinalado pelo O")

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

def print_board(board):
    print(board['7'],' | ',board['8'],' | ',board['9'])
    print('--------------')
    print(board['4'],' | ',board['5'],' | ',board['6'])
    print('--------------')
    print(board['1'],' | ',board['2'],' | ',board['3'])

def check_win(board):
    if board['7']==board['8']==board['9']!= ' ':
        return True
    elif board['4']==board['5']==board['6']!= ' ':
        return True
    elif board['1']==board['2']==board['3']!= ' ':
        return True
    elif board['7']==board['4']==board['1']!= ' ':
        return True
    elif board['8']==board['5']==board['2']!= ' ':
        return True
    elif board['9']==board['6']==board['3']!= ' ':
        return True
    elif board['7']==board['5']==board['3']!= ' ':
        return True
    elif board['1']==board['5']==board['9']!= ' ':
        return True
    else:
        return False
    


def fim_jogo(count_wins):
    print(name1 + ': '+count_wins[name1]+' vitórias')
    print(name2 + ': '+count_wins[name2]+' vitórias')


count_wins = {name1: 0 , name2: 0}

def jogo():
    turn = 1

    while True:
        if turn%2 == 1:
            print( name1 + " , é a sua vez de jogar")
            symbol = 'X'
        elif turn%2 == 0:
            print( name2 + " , é a sua vez de jogar")
            symbol = 'O'
        move = input('Insira no keyboard a casa que quer jogar: ')

        while True:
            if int(move) > 9:
               move = input('Insira uma nova jogada ')
            elif board[move]== ' ':
                board[move] = symbol
                break  
            else:
                move = input('Casa já preenchida. Insira uma nova jogada ') 
        

        print_board(board)

        
        if check_win(board):
            if turn%2 == 1:
                count_wins[name1] += 1
                print(name1 + ', Venceu este jogo')
            elif turn%2 == 0:
                count_wins[name2] += 1
                print(name2 + ', Venceu este jogo')
            novo_jogo = input("Quer jogar novamente [Y/N]: ")
            if novo_jogo == 'Y' or novo_jogo == 'y':
                print(name1 + ': '+str(count_wins[name1])+' vitórias')
                print(name2 + ': '+str(count_wins[name2])+' vitórias')
                for key in board:
                    board[key] = ' '
                jogo()
                
            else:
                fim_jogo(count_wins)
                
        
        turn += 1


    
        




if  __name__ == "__main__":
    jogo()
