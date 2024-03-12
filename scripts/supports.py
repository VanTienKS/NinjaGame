import pygame
import os

DEFAULT_IMG_PATH = 'data\\images\\'


def load_image(path):
    image = pygame.image.load(DEFAULT_IMG_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    return image


def load_images(path):
    images = []
    for image_name in sorted(os.listdir(DEFAULT_IMG_PATH + path)):
        images.append(load_image(path + "\\" + image_name))
    return images
