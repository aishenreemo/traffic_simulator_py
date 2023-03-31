import pygame


class Memory:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Memory, cls).__new__(cls)

        return cls.instance

    def init(self):
        self.window_size = pygame.display.get_surface().get_size()

        return

    def update(self):
        self.window_size = pygame.display.get_surface().get_size()

        return
