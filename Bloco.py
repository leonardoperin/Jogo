import pygame, random

class Bloco(pygame.sprite.Sprite):
  def __init__(self,largura,altura,x,y):
          super().__init__()
          self.image = pygame.Surface([largura,altura])
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y

  def mover(self, y):
          self.rect.y += 25

  def cair(self):
      self.rect.y += 1

      if self.rect.y > 800:
        self.rect.y = 0
        self.rect.x = random.randint(0, 1200)
