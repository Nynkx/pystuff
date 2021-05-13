import pygame


def load_image(name, color=None):
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print(message);

    image = image.convert()

    return image, image.get_rect()