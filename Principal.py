import pygame, random
from Bloco import Bloco
from Carro import Carro
from Estrada import Estrada


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

try:
  pygame.init()
except:
  print("O modulo pygame não foi iniciado com sucesso")

LARGURA = 750
ALTURA = 800
tela = pygame.display.set_mode([LARGURA, ALTURA])
pygame.display.set_caption("Corrida Interminável")

estrada = Estrada(0,0)
carro = Carro(315,630)

listaObjetos = pygame.sprite.Group()
listaObjetos.add(estrada)
listaObjetos.add(carro)

clock = pygame.time.Clock()

bloco = Bloco(50,50, random.randint(0, LARGURA), 0)

listaObjetos.add(bloco)

listaBlocos = pygame.sprite.Group()

terminou = False

while not terminou:
  filaEventos = pygame.event.get()
  bloco.cair()
  for evento in filaEventos:
      if evento.type == pygame.QUIT:
          terminou = True

  carro.mover()

  bateu = pygame.sprite.collide_rect(carro, bloco)
  if bateu == True:
      print ("Você perdeu")
      terminou = True

  clock.tick(1000)

  tela.fill(BRANCO)
  listaObjetos.draw(tela)
  pygame.display.update()

pygame.quit()
exit()