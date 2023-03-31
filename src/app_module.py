import pygame
from .cmd_module import (QuitCommand, CommandType)
from .mem_module import Memory

APP_FPS = 60
APP_WINDOW_SIZE = (800, 600)


class App:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(App, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self.running = True
        self.cmd_queue = []
        self.screen = pygame.display.set_mode(APP_WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.delta = 0

        self.mem = Memory()

        return

    def listen(self):
        if not self.running:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.cmd_queue.append(QuitCommand())
                break

        return

    def update(self):
        if not self.running:
            return

        for command in self.cmd_queue:
            if command.type == CommandType.QUIT:
                self.running = False
                break

        self.cmd_queue.clear()

        return

    def render(self):
        if not self.running:
            return

        self.screen.fill("black")
        pygame.display.flip()

        return

    def tick(self):
        if not self.running:
            return

        self.delta = self.clock.tick(APP_FPS)

        return
