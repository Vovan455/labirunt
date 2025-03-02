import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
FPS = 60

window = pygame.display.set_mode(SIZE)
backgound = pygame.transform.scale(
    pygame.image.load("background.jpg"),
    SIZE)
pygame.display.set_caption("Лабіринт. Автор: ....")
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite) :
    def __init__ (self, filename:str, size:tuple[int,int], coords: tuple[int,int], speed:int):
        super(). __init__ ()
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self. image. get_rect (center=coords )
        self.speed = speed
    def reset(self, window):
        window.blit(self. image, self. rect)

class Player (GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[pygame.K_s] and self.rect.y < HEIGHT :
            self.rect.y += self.speed

        if keys[pygame.K_d] and self.rect.x < WIDTH :
            self.rect.x += self.speed

        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed


class Enemy(GameSprite):
    def update(self, x1:int, x2:int):
        self.rect.x += self.speed
        if self.rect.x >= x2 or self.rect.x <= x1:
            self.speed = -self.speed


        

        
          

player = Player("hero.png",(75,75), (50, HEIGHT-50), 5)
enemy = Enemy("cyborg.png",(75,75), (WIDTH-250, HEIGHT//2), 5)
gold = GameSprite("treasure.png",(75,75), (WIDTH-150, HEIGHT-50), 5)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    window.blit(backgound, (0,0))
    player.update()
    player.reset(window)
    enemy.update(700, WIDTH-200)
    enemy.reset(window)
    gold.reset(window)

    pygame.display.update()
    clock.tick(FPS)