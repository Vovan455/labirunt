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

player = GameSprite("hero.png",(75,75), (50, HEIGHT-50), 5)
enemy = GameSprite("cyborg.png",(75,75), (-150, HEIGHT//2), 5)
gold = GameSprite("hero.png",(75,75), (50, HEIGHT-50), 5)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    window.blit(backgound, (0,0))
    player.reset(window)
    enemy.reset(window)
    gold.reset(window)

    pygame.display.update()
    clock.tick(FPS)