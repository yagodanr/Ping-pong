from pygame import *

font.init()


class sSprite(sprite.Sprite):
    def __init__(self, kakapukaimage, x, y, speed=5, l=150, h=150):
        super().__init__()
        self.image = transform.scale(image.load(kakapukaimage), (l, h))
        self.h = h
        self.step = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(sSprite):
    def update(self):

        
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y>5:
            self.rect.y -= self.step
        if key_pressed[K_s] and self.rect.y<display.high-self.h:
            self.rect.y += self.step
    def update2(self):

        
        key_pressed1 = key.get_pressed()

        if key_pressed1[K_UP] and self.rect.y>5:
            self.rect.y -= self.step
        if key_pressed1[K_DOWN] and self.rect.y<display.high-self.h:
            self.rect.y += self.step
   

class Ball(sSprite):
    def __init__(self, kakapukaimage, x, y, speed=5, l=150, h=150):
        super().__init__(kakapukaimage, x, y, speed, l, h)
        self.sp_x = speed
        self.sp_y = speed

    def update(self):

        self.rect.x += self.sp_x
        self.rect.y += self.sp_y
        if self.rect.y<5 or self.rect.y>display.high-self.h:
            self.sp_y = -self.sp_y
            wall_s.play()
        if self.rect.x < 5:
            display.win = 2
        elif self.rect.x > display.length:
            display.win = 1






length = 1280
high = 720


window = display.set_mode((length, high))


display.set_caption("Пинг-понг")

display.length = length
display.high = high

display.win = 0



background = transform.scale(image.load("Пинга понга.jpg"), (display.length, display.high)) 
left_p = Player("Лево (1).png", 70, display.high/2-150, 5, 50, 300)
right_p = Player("Право (1).png", display.length-70-50, display.high/2-150, 5, 50, 300)

ball = Ball("ПингПонгМяч.png", display.length/2, display.high/2, 7, 75, 75)

font = font.SysFont("Arial", 36)





mixer.init() 


wall_s = mixer.Sound("Бац.ogg") 
players_s = mixer.Sound("Бриц.ogg")



clock = time.Clock()
FPS = 30



game = True

while game:
    
    
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYUP:
            if e.key == K_r:
                display.win = 0
                ball.rect.x = display.length/2
                ball.rect.y = display.high/2





    left_p.reset()
    right_p.reset()
    ball.reset()




    if sprite.collide_rect(ball, left_p) or sprite.collide_rect(ball, right_p):
        ball.sp_x = -ball.sp_x
        players_s.play()
        ball.sp_x *= 1.4
        ball.sp_y *= 1.4
        left_p.step *= 1.4
        right_p.step *= 1.4


    

    if display.win != 0:
        win = font.render(str(display.win) + " PLAYER WIN!", True, (255, 215, 0))
        window.blit(win, (length/2-100, high/2))

    else:
        left_p.update()
        right_p.update2()
        ball.update()

    clock.tick(FPS)
    display.update() 


window.blit(background, (0, 0))