import pygame # biblioteca pygame
import cria_objeto
import sys
import random
import math

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura_tela=800
altura_tela=720
tela=pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Planetas")
placar=0

# Carregar o efeito sonoro
efeito_sonoro=pygame.mixer.Sound("explode.ogg")
#somexp=pygame.mixer.Sound("somexp.wav")

# Carregar a imagem de fundo
imagem_fundo=pygame.image.load("fundo.jpg")
# Carregando asteroide
aster=pygame.image.load("asteroid.png")
# diminuindo a escala do asteroide
asteroide=pygame.transform.scale(aster,(52,71))

# carregando a imagem de explosão
exp=pygame.image.load("explosion.png")
# diminuindo a escala da explosão
exp1=pygame.transform.scale(exp,(30,30))
# carregando explosões de outros tamanhos
exp2=pygame.transform.scale(exp,(40,40))
exp3=pygame.transform.scale(exp,(50,50))
exp4=pygame.transform.scale(exp,(60,60))
exp5=pygame.transform.scale(exp,(70,70))
exp6=pygame.transform.scale(exp,(80,80))
exp7=pygame.transform.scale(exp,(90,90))
exp8=pygame.transform.scale(exp,(100,100))

# carregando a imagem de explosão
boom=pygame.image.load("pow.png")
# diminuindo a escala da explosão
boom1=pygame.transform.scale(boom,(30,30))
# carregando explosões de outros tamanhos
boom2=pygame.transform.scale(boom,(40,40))
boom3=pygame.transform.scale(boom,(50,50))
boom4=pygame.transform.scale(boom,(60,60))
boom5=pygame.transform.scale(boom,(70,70))
boom6=pygame.transform.scale(boom,(80,80))
boom7=pygame.transform.scale(boom,(90,90))
boom8=pygame.transform.scale(boom,(100,100))


# Carregando diamante
dia=pygame.image.load("diamante.png")
# diminuindo a escala do diamante
dia=pygame.transform.scale(dia,(52,71))

# Carregando coracao
cora=pygame.image.load("heart.png")
# diminuindo a escala do coracao
coracao=pygame.transform.scale(cora,(64,60))

# Carregando nave
nav=pygame.image.load("fighter.png")
# diminuindo a escala da nave
nave=pygame.transform.scale(nav,(130,64))
nave=pygame.transform.flip(nave, True, False)

# Carregando o laser
laser=pygame.image.load("laser.png")
# diminuindo a escala do laser
laser=pygame.transform.scale(laser,(30,10))

# criando sprites
sprite1=cria_objeto.objeto(asteroide,(100,100))
sprite2=cria_objeto.objeto(nave,(0,250))
sprite3=cria_objeto.objeto(asteroide,(200,300))
sprite4=cria_objeto.objeto(asteroide,(300,300))
sprite5=cria_objeto.objeto(asteroide,(400,300))
sprite6=cria_objeto.objeto(asteroide,(500,300))
sprite7=cria_objeto.objeto(asteroide,(600,300))
sprite8=cria_objeto.objeto(asteroide,(700,300))
spritelaser=cria_objeto.objeto(laser,(1000,1000))

# criando grupo de sprites para facilitar a manipulação dos mesmos
grupo_sprites=pygame.sprite.Group(sprite1,sprite2,sprite3,spritelaser,sprite4,sprite5,sprite6,sprite7,sprite8)

# obtendo as dimensões da imagem
largura_imagem_fundo,altura_imagem_fundo=imagem_fundo.get_size()

# Posição inicial da imagem de fundo
posicao_x=0

# valor inicial da variável de temporização
tempo=0
t=0

# variáveis para a velocidade
vel1=1
vel3=8
vel4=8
vel5=8
vel6=8
vel7=8
vel8=8

# criando variáveis de contagem
conta1=-1
conta2=-1
conta3=-1
conta4=-1
conta5=-1
conta6=-1
conta7=-1
conta8=-1
conta9=-1
conta10=-1

# carregar os valores de Y1, A1 e W1 utilizando random
X1=800
Y1=random.uniform(50,650)  # posição média do asteróide em Y
A1=random.uniform(10,60)   # A1 é a amplitude da oscilação
W1=random.uniform(1,5)     # W1 é a frequência de oscilação
X3=800
Y3=random.uniform(50,650) 
A3=random.uniform(10,60)   
W3=random.uniform(1,5)    



# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if evento.key == pygame.K_SPACE: # Verifica se a tecla pressionada é a tecla de espaço
                if spritelaser.rect.x>800:
                    spritelaser.rect.x=sprite2.rect.x+90
                    spritelaser.rect.y=sprite2.rect.y+35
                    efeito_sonoro.play()

    if spritelaser.rect.x<810: # enquanto o laser estiver dentro da tela
        spritelaser.rect.x+=40 # aumenta a coordenada x dela em 40 pixels

    tempo=tempo+1  # variável de ajuste do tempo
    if tempo==10:
        tempo=0
        # Atualizar a posição da imagem de fundo
        posicao_x=posicao_x+1

    # lendo as teclas
    teclas=pygame.key.get_pressed()

    # se UP foi pressionada
    if teclas[pygame.K_UP]:
        sprite2.rect.y-=5

    # se DOWN foi pressionada
    if teclas[pygame.K_DOWN]:
        sprite2.rect.y+=5

    # se LEFT foi pressionada
    if teclas[pygame.K_LEFT]:
        sprite2.rect.x-=5

    # se RIGHT foi pressionada
    if teclas[pygame.K_RIGHT]:
        sprite2.rect.x+=5

    # mudando a posição dos sprites dos asteróides
    t=t+0.05       # incrementando a variável t
    X1=X1-vel1     # decrementa a posição em x para andar para a esquerda
    sprite1.rect.x=X1+0*A1*math.cos(W1*t)
    sprite1.rect.y=Y1+0*A1*math.sin(W1*t)
    X3=X3-vel3    
    sprite3.rect.x=X3+A3*math.cos(W3*t)
    sprite3.rect.y=Y3+A3*math.sin(W3*t)
    sprite4.rect.x-=vel4
    sprite4.rect.y=500
    sprite5.rect.x-=vel5
    sprite6.rect.x-=vel6
    sprite7.rect.x-=vel7
    sprite8.rect.x-=vel8

    if pygame.sprite.collide_mask(spritelaser,sprite1) and conta1==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite1.mudar_imagem(boom1) # muda a imagem para explosão
        conta1=9                   # carrega a variável de contagem
        #somexp.play()
 
    # repetir este código para os demais sprites 3,4,5,6,7,8
    if pygame.sprite.collide_mask(spritelaser,sprite3) and conta3==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite3.mudar_imagem(boom1) # muda a imagem para explosão
        conta3=9                    # carrega a variável de contagem
        #somexp.play()
        
    if pygame.sprite.collide_mask(spritelaser,sprite4) and conta4==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite4.mudar_imagem(boom1) # muda a imagem para explosão
        conta4=9                    # carrega a variável de contagem
        #somexp.play()
        
    if pygame.sprite.collide_mask(spritelaser,sprite5) and conta5==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite5.mudar_imagem(boom1) # muda a imagem para explosão
        conta5=9                    # carrega a variável de contagem
        #somexp.play()
        
    if pygame.sprite.collide_mask(spritelaser,sprite6) and conta6==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite6.mudar_imagem(boom1) # muda a imagem para explosão
        conta6=9                    # carrega a variável de contagem
        #somexp.play()
    if pygame.sprite.collide_mask(spritelaser,sprite7) and conta7==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite7.mudar_imagem(boom1) # muda a imagem para explosão
        conta7=9                    # carrega a variável de contagem
        #somexp.play()
    if pygame.sprite.collide_mask(spritelaser,sprite8) and conta8==-1:  # verifico se o sprite2 colidiu com o sprite 1
        spritelaser.rect.x=900     # manda para fora da tela
        placar=placar+10
        sprite8.mudar_imagem(boom1) # muda a imagem para explosão
        conta8=9                    # carrega a variável de contagem
        #somexp.play()

        # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta1>0:   # se a variável de contagem do sprite1 for maior que zero
        conta1-=1  # decrementa
    elif conta1==0:   # se chegou em zero 
        sprite1.rect.x=-100  # envia o sprite1 para a posição 
        sprite1.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta1-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta1==7:
        sprite1.mudar_imagem(boom2)
    elif conta1==6:
        sprite1.mudar_imagem(boom3)
    elif conta1==5:
        sprite1.mudar_imagem(boom4)
    elif conta1==4:
        sprite1.mudar_imagem(boom5)
    elif conta1==3:
        sprite1.mudar_imagem(boom6)
    elif conta1==2:
        sprite1.mudar_imagem(boom7)
    elif conta1==1:
        sprite1.mudar_imagem(boom8)

                # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta3>0:   # se a variável de contagem do sprite1 for maior que zero
        conta3-=1  # decrementa
    elif conta3==0:   # se chegou em zero 
        sprite3.rect.x=-100  # envia o sprite1 para a posição 
        sprite3.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta3-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta3==7:
        sprite3.mudar_imagem(boom2)
    elif conta3==6:
        sprite3.mudar_imagem(boom3)
    elif conta3==5:
        sprite3.mudar_imagem(boom4)
    elif conta3==4:
        sprite3.mudar_imagem(boom5)
    elif conta3==3:
        sprite3.mudar_imagem(boom6)
    elif conta3==2:
        sprite3.mudar_imagem(boom7)
    elif conta3==1:
        sprite3.mudar_imagem(boom8)

                # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta4>0:   # se a variável de contagem do sprite1 for maior que zero
        conta4-=1  # decrementa
    elif conta4==0:   # se chegou em zero 
        sprite4.rect.x=-100  # envia o sprite1 para a posição 
        sprite4.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta4-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta4==7:
        sprite4.mudar_imagem(boom1)
    elif conta4==6:
        sprite4.mudar_imagem(boom1)
    elif conta4==5:
        sprite4.mudar_imagem(boom1)
    elif conta4==4:
        sprite4.mudar_imagem(boom1)
    elif conta4==3:
        sprite4.mudar_imagem(boom1)
    elif conta4==2:
        sprite4.mudar_imagem(boom1)
    elif conta4==1:
        sprite4.mudar_imagem(boom1)

            # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta5>0:   # se a variável de contagem do sprite1 for maior que zero
        conta5-=1  # decrementa
    elif conta5==0:   # se chegou em zero 
        sprite5.rect.x=-100  # envia o sprite1 para a posição 
        sprite5.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta5-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta5==7:
        sprite5.mudar_imagem(boom2)
    elif conta5==6:
        sprite5.mudar_imagem(boom3)
    elif conta5==5:
        sprite5.mudar_imagem(boom4)
    elif conta5==4:
        sprite5.mudar_imagem(boom5)
    elif conta5==3:
        sprite5.mudar_imagem(boom6)
    elif conta5==2:
        sprite5.mudar_imagem(boom7)
    elif conta5==1:
        sprite5.mudar_imagem(boom8)

            # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta6>0:   # se a variável de contagem do sprite1 for maior que zero
        conta6-=1  # decrementa
    elif conta6==0:   # se chegou em zero 
        sprite6.rect.x=-100  # envia o sprite1 para a posição 
        sprite6.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta6-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta6==7:
        sprite6.mudar_imagem(boom2)
    elif conta6==6:
        sprite6.mudar_imagem(boom3)
    elif conta6==5:
        sprite6.mudar_imagem(boom4)
    elif conta6==4:
        sprite6.mudar_imagem(boom5)
    elif conta6==3:
        sprite6.mudar_imagem(boom6)
    elif conta6==2:
        sprite6.mudar_imagem(boom7)
    elif conta6==1:
        sprite6.mudar_imagem(boom8)

            # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta7>0:   # se a variável de contagem do sprite1 for maior que zero
        conta7-=1  # decrementa
    elif conta7==0:   # se chegou em zero 
        sprite7.rect.x=-100  # envia o sprite1 para a posição 
        sprite7.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta7-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta7==7:
        sprite7.mudar_imagem(boom2)
    elif conta7==6:
        sprite7.mudar_imagem(boom3)
    elif conta7==5:
        sprite7.mudar_imagem(boom4)
    elif conta7==4:
        sprite7.mudar_imagem(boom5)
    elif conta7==3:
        sprite7.mudar_imagem(boom6)
    elif conta7==2:
        sprite7.mudar_imagem(boom7)
    elif conta7==1:
        sprite7.mudar_imagem(boom8)

            # o código abaixo permite que a imagem da explosão fique durante algum tempo na tela
    if conta8>0:   # se a variável de contagem do sprite1 for maior que zero
        conta8-=1  # decrementa
    elif conta8==0:   # se chegou em zero 
        sprite8.rect.x=-100  # envia o sprite1 para a posição 
        sprite8.mudar_imagem(asteroide)  # muda a imagem para asteroide
        conta8-=1  # decrementa
    # mudando a imagem da explosão para gerar o efeito de animação
    if conta8==7:
        sprite8.mudar_imagem(boom2)
    elif conta8==6:
        sprite8.mudar_imagem(boom3)
    elif conta8==5:
        sprite8.mudar_imagem(boom4)
    elif conta8==4:
        sprite8.mudar_imagem(boom5)
    elif conta8==3:
        sprite8.mudar_imagem(boom6)
    elif conta8==2:
        sprite8.mudar_imagem(boom7)
    elif conta8==1:
        sprite8.mudar_imagem(boom8)
        

    if sprite1.rect.x<-52:  # se o asteróide desaparecer
        X1=800
        vel1=random.uniform(1,10)  # mudando a velocidade do asteróide
        Y1=random.uniform(50,650)  # posição média do asteróide em Y
        A1=random.uniform(10,60)   # A1 é a amplitude da oscilação
        W1=random.uniform(1,4)     # W1 é a frequência de oscilação

    if sprite3.rect.x<-52:  # se o asteróide desaparecer
        X3=800
        Y3=random.uniform(50,650)  # posição média do asteróide em Y
        A3=random.uniform(10,60)   # A1 é a amplitude da oscilação
        W3=random.uniform(1,4)     # W1 é a frequência de oscilação

    if sprite4.rect.x<-52:  # se o asteróide desaparecer
        sprite4.rect.x=800   # volta a aparecer do outro lado da tela
        sprite4.rect.y=random.uniform(1,629) # sorteia uma posição y para o asteróide
        vel4=random.uniform(1,10)  # mudando a velocidade do asteróide

    if sprite5.rect.x<-52:  # se o asteróide desaparecer
        sprite5.rect.x=800   # volta a aparecer do outro lado da tela
        sprite5.rect.y=random.uniform(1,629) # sorteia uma posição y para o asteróide
        vel5=random.uniform(1,10)  # mudando a velocidade do asteróide
        
    if sprite6.rect.x<-52:  # se o asteróide desaparecer
        sprite6.rect.x=800   # volta a aparecer do outro lado da tela
        sprite6.rect.y=random.uniform(1,629) # sorteia uma posição y para o asteróide
        vel6=random.uniform(1,10)  # mudando a velocidade do asteróide

    if sprite7.rect.x<-52:  # se o asteróide desaparecer
        sprite7.rect.x=800   # volta a aparecer do outro lado da tela
        sprite7.rect.y=random.uniform(1,629) # sorteia uma posição y para o asteróide
        vel7=random.uniform(1,10)  # mudando a velocidade do asteróide

    if sprite8.rect.x<-52:  # se o asteróide desaparecer
        sprite8.rect.x=800   # volta a aparecer do outro lado da tela
        sprite8.rect.y=random.uniform(1,629) # sorteia uma posição y para o asteróide
        vel8=random.uniform(1,10)  # mudando a velocidade do asteróide


        


# implementar um placar onde cada asteróide possui uma pontuação diferente
# mude a imagem dos asteróides, cada um deve ser uma figura diferente
# coloque o movimento senoidal em y em 3 asteroides  
 

    # atualizando sprites
    grupo_sprites.update()

    # Verificar se a imagem de fundo atingiu o final da tela
    if posicao_x>=largura_imagem_fundo:
        posicao_x=0   

    # Preencher a tela com a cor de fundo
    tela.fill((0,0,0))

    # Desenhar a imagem de fundo na tela
    tela.blit(imagem_fundo,(-posicao_x,0))

    # desenhando sprites na tela    
    grupo_sprites.draw(tela)

    # Exibindo o placar
    tela.blit(pygame.font.SysFont(None,28).render("Pontos="+str(placar),True,(255,255,255)),(1,700))    

    # Atualizar a tela
    pygame.display.flip()

    # Atraso em ms
    pygame.time.delay(50)
