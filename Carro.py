import pygame

class Carro(pygame.sprite.Sprite):
  def __init__(self, x, y):
      super().__init__()    #chama o construtor da superclasse
      self.image = pygame.image.load("carrinho.jpg").convert_alpha()
      self.rect = self.image.get_rect()    # pega coordenadas
      self.rect.x = x
      self.rect.y = y

  def mover(self):
      tecla = pygame.key.get_pressed()
      if tecla[pygame.K_LEFT]:
          self.rect.x -= 5

      if tecla[pygame.K_RIGHT]:
          self.rect.x += 5

