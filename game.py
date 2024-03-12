import pygame
import sys

from scripts.supports import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import TileMap


class Game():
    def __init__(self, screen_width, screen_height, fps):
        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.assets = {
            'background': load_image('background.png'),
            'player': load_image('entities\\player.png'),
            'decor': load_images('tiles\\decor'),
            'grass': load_images('tiles\\grass'),
            'large_decor': load_images('tiles\\large_decor'),
            'spawners': load_images('tiles\\spawners'),
            'stone': load_images('tiles\\stone'),
        }

        self.player = PhysicsEntity(self, (60, 60), (8, 15))
        self.tilemap = TileMap(self, tile_size=16)

        self.movement = [False, False]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.player.update(self.tilemap,
                               (self.movement[1] - self.movement[0], 0))

            self.display.blit(self.assets['background'], (0, 0))
            self.tilemap.render(self.display)
            self.player.render(self.display)

            self.screen.blit(pygame.transform.scale(
                self.display, (self.screen.get_width(), self.screen.get_height())), (0, 0))

            pygame.display.update()
            self.clock.tick(self.fps)


game = Game(960, 720, 60)
game.run()
