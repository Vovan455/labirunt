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
#pygame.mixer.music.load("jungles.ogg")
#pygame.mixer.music.play()

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

class wall:
    def __init__(self, coords:tuple[int,int], size:tuple[int,int], color:tuple[int,int,int]):
        self.rect = pygame.Rect(coords, size)
        self.color = color

    def draw(self, windiw:pygame.Surface, width=0):
        pygame.draw.rect(window, self.color, self.rect, width=width)
        

        

        
          

player = Player("hero.png",(75,75), (50, HEIGHT-50), 5)
enemy = Enemy("cyborg.png",(75,75), (WIDTH-250, HEIGHT//2), 5)
gold = GameSprite("treasure.png",(75,75), (WIDTH-150, HEIGHT-50), 5)

wall_0 = wall((0,0),(WIDTH, HEIGHT),(10,240,10))
walls = [
    wall((10,10), (300,10), (50,200,50)),
    wall((300,10), (10,300), (50,200,50)),
    wall((10,300), (100,10), (50,200,50)),
    wall((10, 588), (400,10), (50,200,50)),
    wall((530, 124), (10, 1700), (50,200,50)),
    wall((402, 517), (10,80), (50,200,50))
]
game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    if not finish:
        window.blit(backgound, (0,0))
        player.update()
        player.reset(window)
        enemy.update(700, WIDTH-200)
        enemy.reset(window)

        gold.reset(window)

        if pygame.sprite.collide_rect(player, enemy):
            finish = True
            kick = pygame.mixer.Sound("kick.ogg")
            kick.play()

            pygame.font.init()
            font1 = pygame.font.Font(None,48)
            text = font1.render("YOU DIED", True, (255,0,0))
            window.blit(text, (WIDTH//2-100, HEIGHT//2))

        if pygame.sprite.collide_rect(player, gold):
            finish = True
            kick = pygame.mixer.Sound("money.ogg")
            kick.play()

            pygame.font.init()
            font1 = pygame.font.Font(None,48)
            text = font1.render("YOU WIN", True, (255,0,0))
            window.blit(text, (WIDTH//2-100, HEIGHT//2))
        
        

        wall_0.draw(window, width=10)
        for w in walls:
            w.draw(window)
            if pygame.sprite.collide_rect(player, w):
                finish = True
                kick = pygame.mixer.Sound("kick.ogg")
                kick.play()

                pygame.font.init()
                font1 = pygame.font.Font(None,48)
                text = font1.render("YOU DIED", True, (255,0,0))
                window.blit(text, (WIDTH//2-100, HEIGHT//2))

    pygame.display.update()
    clock.tick(FPS)