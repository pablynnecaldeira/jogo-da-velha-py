##----------------------------------
# Projeto jogo da velha
# Disciplina: Lógica de Programação
# Participantes:
##----------------------------------

#Funções do usuário

def criaMatriz():
    mat = [ [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    return mat

def posicaoOcupada(matriz, posicao):
    return False
         	# verifica se a posição escolhida pelo jogador está ocupada. Deve retornar True ou False
  	# completar o código

def registraJogada(mat, posicao, jogador):
      	# Esta função deve inserir a marcação do jogador na posição informada.
      	# a função deve retornar a matriz preenchida
  	# completar o código
        return
    
def apresentaMatriz(mat):
  	print(mat[0][0], "|", mat[0][1], "|", mat[0][2])
  	print("-" * 10)
  	print(mat[1][0], "|", mat[1][1], "|", mat[1][2])
  	print("-" * 10)
  	print(mat[2][0], "|", mat[2][1], "|", mat[2][2])
  	return


def trocaJogador(jogador):
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
    return jogador
#

def verificaGanhador(mat, jogador):
    if mat[0][0] and mat [0][1] and mat[0][2]or mat [1][0] and mat [1][1] and mat [1][2]or mat[2][0] and mat [2][1] and mat [2][2]or mat [0][0] and mat [1][0] and mat[2][0]or mat [0][1] and mat [1][1] and mat [2][1]or mat [0][2] and mat [1][2] and mat [2][2]or mat [0][0] and mat [1][1] and mat [2][2]or mat [0][2] and mat [1][1] and mat [2][0]:
        return True
        print('teset')
    else:
        return False
##----Final das funções do usuário

## ----- Programa Principal  
print("*** JOGO DA VELHA *** \n")
print("Desafie o seu colega no jogo da velha.\n")
print("Regras: a) O primeiro jogador participará com a letra X e o segundo com a letra O.")
print("        b) Os números de 1 a 9 representam os espaços que estão livres.")
print(            "Você só poderá escolher as posições livres.")
print("        c)  O vencedor será o primeiro Jogador a preencher uma linha, uma coluna ou uma diagonal.")

matriz = criaMatriz()        # Cria a Matriz do Jogo
jogador = "X"                     # Define o Jogador Inicial
c = 0
while c < 10:
    apresentaMatriz(matriz)
    posicao = int(input(f"(Jogador {jogador}) Informe a posição desejada :"))
    if posicao == 1:
        matriz [0][0]=jogador
    elif posicao == 2:
        matriz [0][1]=jogador
    elif posicao == 3:
        matriz [0][2]=jogador
    elif posicao == 4:
        matriz [1][0]=jogador
    elif posicao == 5:
        matriz [1][1]=jogador
    elif posicao == 6:
        matriz [1][2]=jogador
    elif posicao == 7:
        matriz [2][0]=jogador
    elif posicao == 8:
        matriz [2][1]=jogador
    else:
        posicao == 9
        matriz [2][2]=jogador
        
    jogador = trocaJogador (jogador)
    c += 1
        
    if verificaGanhador(matriz,jogador):
        print(f"{jogador} ganhador")
        break

    
    
## ----- Final do Programa  
    
