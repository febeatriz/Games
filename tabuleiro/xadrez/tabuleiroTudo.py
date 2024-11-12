import pygame  # biblioteca pygame
import random 

class objeto(pygame.sprite.Sprite):
    def __init__(self,imagem,posicao,escala,tipo2):
        super().__init__()
        # imagem associada ao sprite
        self.original=imagem
        # diminuindo o tamanho  do sprite
        self.image=pygame.transform.scale(self.original,
                   (int(self.original.get_width()*escala),
                   int(self.original.get_height()*escala)))

        # retângulo de colisão do sprite
        self.rect=self.image.get_rect()
        # posição do sprite (x,y)
        # desloca e multiplica pela largura e altura
        # do quadrado para posicionar corretamente no
        # tabuleiro
        self.rect.x=38+49*(posicao[0]-1)
        self.rect.y=40+48*(posicao[1]-1)
        # Variável de controle para verificar se o sprite sofreu kill
        self.killed=False
        # coordenadas linha e coluna do sprite
        self.coluna=posicao[0]
        self.linha=posicao[1]
        # tipo de peça
        self.tipo=tipo2
        
    # Atualiza a variável de controle quando o sprite sofre kill
    def kill(self):
        super().kill()
        self.killed = True

    # Modifica a coordenadas do sprite
    def coordenada(self,coluna2,linha2):
        self.rect.x=38+49*(coluna2-1)
        self.rect.y=40+48*(linha2-1)
        self.coluna=coluna2
        self.linha=linha2

    # verifica se o mouse esta sobre o sprite
    def mouse(self,xx,yy):
        if ((self.rect.x+5)<xx) and ((self.rect.x+30)>xx) and ((self.rect.y+5)<yy) and ((self.rect.y+30)>yy) and self.killed==False:
            return True
        else:
            return False

def mousexy(x,y): # retorna em linha e coluna as coordenadas do mouse
    return (int((x-38)/49+1),int((y-40)/48+1))

def mov_peca(col1,col2,lin1,lin2,tip):  # verifica se o movimento da peça é permitido
    if tip==1:       # se for a concha, move uma casa por vez
        if(abs(col2- col1)<= 1) and (abs(lin2-lin1)<=1):
            return True
        else:
            return False
    elif tip==2:    # se for uva, anda no maximo 2 casas na vertical ou na horizontal]. diagonal proibido
        if (abs(col2 - col1) <= 2 and lin1 == lin2) or (abs(lin2 - lin1) <= 2 and col1 == col2):
            return True
        else: return False
    elif tip==3:  # se for laranja, similar ao bispo, porém com 3 casas, anda somente na diagonal, no maximo 3 casa 
        if abs(col2 - col1) == abs(lin2 - lin1) and abs(col2 - col1) <= 3:
            return True
        else: return False 
    elif tip==4:    # se for maça, anda no maximo uma casa na horizontal ou anda no maximo 6 casas na vertial
        if (abs(col2 - col1) == 1 and lin1 == lin2) or (abs(lin2 - lin1) <= 6 and col1 == col2):
            return True
        else: return False
    elif tip==5:    #se for coração, anda similar à concha, mas no maximo 10 casas
        if abs(col2 - col1) <= 10 and abs(lin2 - lin1) <= 10:
            return True
        else: return False     
    
        

# peças do lado do jogador        
pecas=["animal.png","uva.png","laranja.png","maca.png","coracao2.png","laranja.png","uva.png","animal.png"]

# posições das peças no tabuleiro
posicao=[[0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [6,6,6,6,6,6,6,6],
          [6,6,6,6,6,6,6,6]]

tipos=[1,2,3,4,5,3,2,1]

# número de peças
npecas=8

# variável para a posição inicial da peça do jogador
posx=0
posy=0

pygame.init()  # iniciando a biblioteca

# criando tela para desenhar
tela=pygame.display.set_mode([466,454])
# neste caso as dimensões da tela são as mesmas da imagem
# que será cerregada como fundo

# carregando a imagem de fundo
caminho='tabuleiro.jpg'
background=pygame.image.load(caminho)

# carregando as imagem das peças
diamante2=pygame.image.load("diamante.png")

# criando sprites

coracao=[]
diamante=[]

# variável índice para a peça
indice=0
# variável índice para o diamante
indice2=0
# variáveis de coordenadas para o diamante
cd=0
ld=0
# variável de contagem para o tempo
contador=1000
# variável de habilita o movimento
habilita=False

for i in range(0,npecas):  # laço para criar 4 peças 
    coracao2=pygame.image.load(pecas[i])   # carregando a imagem da peça da lista
    coracao.append(objeto(coracao2,(i+1,1),0.07,tipos[i]))
  
for i in range(0,8):  # laço para criar 16 diamantes
    diamante.append(objeto(diamante2,(i+1,8),0.07,6))
    diamante.append(objeto(diamante2,(i+1,7),0.07,6))

# criando grupo de sprites
grupo_sprites=pygame.sprite.Group(coracao,diamante)

rodando=True # variável responssável pela execução do jogo

movimento=False  # variável para manter o movimento da peça

while rodando:   # o loop funciona enquanto a variável rodando for True

    # testando se alguma tecla foi pressionada
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  # se clicou para sair do jogo
            rodando=False            # quebra o laço while


    # se pressionou o botão esquerdo do mousee foi habilitado o movimento
    if  event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and habilita==True:
      
        # Obtém a posição do mouse
        mx,my=pygame.mouse.get_pos()
        # laço para verificar qual coração foi selecionado
        for i in range (0,npecas):
            if coracao[i].mouse(mx,my):
                # movimenta a peça 1 de acordo com a posição do mouse
                posx=coracao[i].coluna       # lê a posição antiga
                posy=coracao[i].linha                
                coracao[i].rect.x=mx         # carrega a nova posição
                coracao[i].rect.y=my    
                indice=i   # carrega a variável índice com a identificação da peça
                # carrega a variável informando que o movimento esta em andamento
                movimento=True      

    # se liberou o botão esquerdo do mouse
    if  event.type==pygame.MOUSEBUTTONUP and event.button==1 and habilita==True:
        
        # Obtém a posição do mouse
        mx,my=pygame.mouse.get_pos()
        # carrega a variável informando que o movimento terminou
        habilita=False
        movimento=False

        # mudando a linha e coluna da peça 
        co,li=mousexy(mx,my)       # obtendo coluna e linha

        if mov_peca(posx,co,posy,li,coracao[indice].tipo):   # se o movimento for permitido

            # laço para verificar se a peça está na posição do diamante
            for i in range(0,8):
            # se estiver na posição do diamante, elimina o diamante
                if pygame.sprite.collide_mask(coracao[indice],diamante[i]) and diamante[i].killed==False:
                    diamante[i].kill()         # elimina o diamante

            coracao[indice].coordenada(co,li) # mudando a linha e coluna da peça

        else:  # se o movimento não for permitido
            coracao[indice].coordenada(posx,posy)  # mantém a coordenada antiga
                

    if movimento==True:  # se o movimento esta ocorrendo
        mx,my=pygame.mouse.get_pos()
        # movimenta a peça de acordo com a posição do mouse
        coracao[indice].rect.x=mx
        coracao[indice].rect.y=my



    contador-=1   # decrementando o contador

    if contador==0:    # se já deu o tempo
        contador=1000  # reinicia o contador
        habilita=True # habilita o movimento das outras peças
        # movendo um diamante toda vez que der o tempo
        indice2=random.randint(0,15) # escolhendo um diamante aleatóriamente

        # verificando se existe um diamante na frente do outro        
        while diamante[indice2].killed==True or posicao[diamante[indice2].linha-2][diamante[indice2].coluna-1]==6:  # se o diamante ja tinha sido eliminado
            indice2=random.randint(0,15)     # sorteia outro diamante
        
        ld=diamante[indice2].linha   # lendo a linha do diamante
        cd=diamante[indice2].coluna  # lendo a coluna do diamante

        ld=ld-1   # recuando uma linha para o diamante

        # atualizando a variável de posição dos diamantes no tabuleiro

        posicao[ld-1][cd-1]=6                                             # carrega 6 naquela posição
        posicao[diamante[indice2].linha-1][diamante[indice2].coluna-1]=0  # carrega 0 na posição antiga do diamante

        # carregando a nova coordenada do diamante
        diamante[indice2].coordenada(cd,ld)

        print(posicao[0])  # exibe a posição das peças no prompt
        print(posicao[1])
        print(posicao[2])
        print(posicao[3])
        print(posicao[4])
        print(posicao[5])
        print(posicao[6])
        print(posicao[7])

    tela.blit(background,(0,0)) # desenha a tela de fundo

    # atualizando sprites
    grupo_sprites.update()

    # exibindo a contagem do tempo
    tela.blit(pygame.font.SysFont(None,28).render("Tempo="+str(contador),True,(0,255,0)),(10,430))
    if habilita==True:   # se o movimento foi habilitado
        tela.blit(pygame.font.SysFont(None,28).render("Habilitado",True,(0,0,255)),(300,430))
    else:   # se foi desabilitado
        tela.blit(pygame.font.SysFont(None,28).render("Desabilitado",True,(255,0,0)),(300,430))
   
  
   
    # desenhando sprites na tela
    grupo_sprites.draw(tela)
    
    # atualiza a tela
    pygame.display.flip()

    pygame.time.delay(10) # atraso em ms

# saindo do jogo    
pygame.quit()
