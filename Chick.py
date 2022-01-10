import pygame
import ctypes
user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.init()


class Chick(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.chickleft = pygame.image.load('Assets/Images/chickleft.png').convert_alpha()
        self.chickright = pygame.image.load('Assets/Images/chickright.png').convert_alpha()
        self.chickjumpright = pygame.image.load('Assets/Images/chickjumpright.png').convert_alpha()
        self.chickjumpleft = pygame.image.load('Assets/Images/chickjumpleft.png').convert_alpha()
        self.chickrunleft1 = pygame.image.load('Assets/Images/chickrunleft1.png').convert_alpha()
        self.chickrunleft2 = pygame.image.load('Assets/Images/chickrunleft2.png').convert_alpha()
        self.chickrunright1 = pygame.image.load('Assets/Images/chickrunright1.png').convert_alpha()
        self.chickrunright2 = pygame.image.load('Assets/Images/chickrunright2.png').convert_alpha()
        self.flyleft1 = pygame.image.load('Assets/Images/chickflyleftst1.png').convert_alpha()
        self.flyleft2 = pygame.image.load('Assets/Images/chickflyleftst2.png').convert_alpha()
        self.flyleft3 = pygame.image.load('Assets/Images/chickflyleftst3.png').convert_alpha()
        self.flyright1 = pygame.image.load('Assets/Images/chickflyrightst1.png').convert_alpha()
        self.flyright2 = pygame.image.load('Assets/Images/chickflyrightst2.png').convert_alpha()
        self.flyright3 = pygame.image.load('Assets/Images/chickflyrightst3.png').convert_alpha()
        self.deadchick = pygame.image.load('Assets/Images/Chickdeatheffect.png').convert_alpha()
        self.chicksound = pygame.mixer.Sound('Assets/Sounds/Papapapapapa.mp3')

        self.chickimage = self.chickright
        self.on_ice = 0
        self.xspeed = 0
        self.runspeed = 5
        self.yspeed = 0
        self.gravity = 0.7
        self.jumpspeed = 15
        self.acceleration = 0.5
        self.ground = H-50
        self.chickturnr = 0
        self.runanim = 1
        self.flyanim = 1
        self.x = x
        self.y = y

        pygame.sprite.Sprite.__init__(self)
        self.image = self.chickimage
        self.rect = self.image.get_rect(bottomleft=(self.x, 0))

    def update(self):
        keys = pygame.key.get_pressed()

        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        "Обрабатываем прыжок"
        if keys[pygame.K_SPACE] and self.ground == self.rect.bottom:
            self.yspeed = self.jumpspeed

        "Поднимаем по Y"
        if self.yspeed > 0:
            self.y -= self.yspeed
            self.yspeed -= self.gravity

        "Падение и полёт"
        if self.y < self.ground and self.yspeed <= 0:
            if keys[pygame.K_SPACE]:
                if self.yspeed > -2:
                    self.yspeed -= self.gravity / 2
                else:
                    self.yspeed = -2
            else:
                if self.yspeed > -6:
                    self.yspeed -= self.gravity
                else:
                    self.yspeed = -6
            if self.y - self.yspeed >= self.ground:
                self.y = self.ground
                self.yspeed = 0

            self.y -= self.yspeed
            if self.y >= self.ground:
                self.y = self.ground
            "Движение по X "
        # ОБЕ НАЖАТЫ (Остановка)
        if keys[pygame.K_a] and keys[pygame.K_d]:
            if self.xspeed > 0:
                if self.xspeed - self.acceleration <= 0:
                    self.xspeed = 0
                else:
                    if self.rect.bottom == self.ground:
                        if self.on_ice:
                            self.xspeed -= self.acceleration / 3
                        else:
                            self.xspeed -= self.acceleration
                    elif keys[pygame.K_SPACE]:
                        self.xspeed -= self.acceleration / 1.5
                    else:
                        self.xspeed -= self.acceleration / 1.25
            else:
                if self.xspeed + self.acceleration >= 0:
                    self.xspeed = 0
                else:
                    if self.rect.bottom == self.ground:
                        if self.on_ice:
                            self.xspeed += self.acceleration / 3
                        else:
                            self.xspeed += self.acceleration
                    elif keys[pygame.K_SPACE]:
                        self.xspeed += self.acceleration / 3
                    else:
                        self.xspeed += self.acceleration / 2
        # НАЛЕВО
        elif keys[pygame.K_a] and self.xspeed <= 0:
            if self.rect.bottom == self.ground:
                if self.on_ice:
                    if self.xspeed > -self.runspeed * 1.5:
                        self.xspeed -= self.acceleration / 3
                else:
                    if self.xspeed > -self.runspeed:
                        self.xspeed -= self.acceleration
            elif keys[pygame.K_SPACE]:
                if self.xspeed > -self.runspeed / 1.5:
                    self.xspeed -= self.acceleration / 3
            else:
                if self.xspeed > -self.runspeed / 1.25:
                    self.xspeed -= self.acceleration / 2
            self.chickturnr = False
        # НАПРАВО
        elif keys[pygame.K_d] and self.xspeed >= 0:
            if self.rect.bottom == self.ground:
                if self.on_ice:
                    if self.xspeed < self.runspeed * 1.5:
                        self.xspeed += self.acceleration / 3
                else:
                    if self.xspeed < self.runspeed:
                        self.xspeed += self.acceleration
            elif keys[pygame.K_SPACE]:
                if self.xspeed < self.runspeed / 1.5:
                    self.xspeed += self.acceleration / 3
            else:
                if self.xspeed < self.runspeed / 1.25:
                    self.xspeed += self.acceleration / 2
            self.chickturnr = True
            # НЕ НАЖАТЫ (Остановка)
        else:
            if self.xspeed > 0:
                if self.xspeed - self.acceleration <= 0:
                    self.xspeed = 0
                else:
                    if self.rect.bottom == self.ground:
                        if self.on_ice:
                            self.xspeed -= self.acceleration / 3
                        else:
                            self.xspeed -= self.acceleration
                    elif keys[pygame.K_SPACE]:
                        self.xspeed -= self.acceleration / 3
                    else:
                        self.xspeed -= self.acceleration / 2
            else:
                if self.xspeed + self.acceleration >= 0:
                    self.xspeed = 0
                else:
                    if self.rect.bottom == self.ground:
                        if self.on_ice:
                            self.xspeed += self.acceleration / 3
                        else:
                            self.xspeed += self.acceleration
                    elif keys[pygame.K_SPACE]:
                        self.xspeed += self.acceleration / 3
                    else:
                        self.xspeed += self.acceleration / 2
        self.x += self.xspeed

        "Анимация"
        # При беге
        if self.rect.bottom == self.ground and not keys[pygame.K_SPACE]:
            if self.xspeed:
                if self.runanim <= 5:
                    if self.chickturnr:
                        self.chickimage = self.chickrunright1
                    else:
                        self.chickimage = self.chickrunleft1
                    self.runanim += 1
                elif self.runanim <= 10:
                    if self.chickturnr:
                        self.chickimage = self.chickrunright2
                    else:
                        self.chickimage = self.chickrunleft2
                    self.runanim += 1
                elif self.runanim > 10:
                    self.runanim = 1
            else:
                if self.chickturnr:
                    self.chickimage = self.chickright
                else:
                    self.chickimage = self.chickleft
        # При полёте
        if not self.rect.bottom == self.ground:
            if self.yspeed >= 0:
                if self.chickturnr:
                   self.chickimage = self.chickjumpright
                else:
                    self.chickimage = self.chickjumpleft
            elif keys[pygame.K_SPACE]:
                if self.chickturnr:
                    if self.flyanim <= 10:
                        self.chickimage = self.flyright1
                        self.flyanim += 1
                    elif 10 < self.flyanim <= 20:
                        self.chickimage = self.flyright2
                        self.flyanim += 1
                    elif 20 < self.flyanim <= 30:
                        self.chickimage = self.flyright3
                        self.flyanim += 1
                    elif 30 < self.flyanim < 35:
                        self.chickimage = self.flyright2
                        self.flyanim += 1
                    elif self.flyanim == 35:
                        self.flyanim = 1
                else:
                    if self.flyanim <= 10:
                        self.chickimage = self.flyleft1
                        self.flyanim += 1
                    elif 10 < self.flyanim <= 20:
                        self.chickimage = self.flyleft2
                        self.flyanim += 1
                    elif 20 < self.flyanim <= 30:
                        self.chickimage = self.flyleft3
                        self.flyanim += 1
                    elif 30 < self.flyanim < 35:
                        self.chickimage = self.flyleft2
                        self.flyanim += 1
                    elif self.flyanim == 35:
                        self.flyanim = 1
            else:
                if self.chickturnr:
                    self.chickimage = self.chickjumpright
                else:
                    self.chickimage = self.chickjumpleft
        self.image = self.chickimage

