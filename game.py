import pygame
import sys

from scripts.supports import load_image, load_images

class Game():
    def __init__(self, screen_width, screen_height, fps):
        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.assest = {
            'background': load_image('background.png'),
        }
        self.img_pos = [160, 260]
        self.movement = [False, False]
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
                    
            self.screen.blit(pygame.transform.scale(self.assest['background'], (self.screen.get_width(), self.screen.get_height())), (0,0))  

            pygame.display.update()
            self.clock.tick(self.fps)

game = Game(960,720,60)
game.run()