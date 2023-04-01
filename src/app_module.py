import pygame
from .mem_module import Memory
from .gui_module import Display
from .cmd_module import (
    QuitCommand,
    ModifyScreenPtrCommand,
    CommandType
)

APP_FPS = 60
APP_WINDOW_SIZE = (800, 600)
APP_KEYDOWN_DELAY = 500
APP_KEYDOWN_INTERVAL = 100


class App:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(App, cls).__new__(cls)

        return cls.instance

    def init(self):
        self.running = True
        self.cmd_queue = []
        self.screen = pygame.display.set_mode(APP_WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.delta = 0

        self.mem = Memory()
        self.gui = Display()

        self.mem.init()
        self.gui.init()

        pygame.key.set_repeat(APP_KEYDOWN_DELAY, APP_KEYDOWN_INTERVAL)

        return

    def listen(self):
        if not self.running:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.cmd_queue.append(QuitCommand())
                break
            elif event.type == pygame.KEYDOWN:
                on_keydown(event)

        return

    def update(self):
        if not self.running:
            return

        self.mem.update()
        self.gui.update()

        for command in self.cmd_queue:
            if command.type == CommandType.QUIT:
                self.running = False
                break
            elif command.type == CommandType.MODIFY_SCREEN_PTR:
                self.gui.screen_ptr = command.new_ptr

        self.cmd_queue.clear()

        return

    def render(self):
        if not self.running:
            return

        try:
            screen = self.gui.screen_vec[self.gui.screen_ptr]
            self.screen.fill(screen.bg_color)
            pygame.display.flip()

        except IndexError as err:
            print("screen_ptr:", err)
            exit(1)

        return

    def tick(self):
        if not self.running:
            return

        self.delta = self.clock.tick(APP_FPS)

        return


def on_keydown(event):
    app = App()
    mods = pygame.key.get_mods()

    if event.key == pygame.K_h and mods & pygame.KMOD_CTRL:
        new_ptr = app.gui.screen_ptr

        if (app.gui.screen_ptr == 0):
            new_ptr = len(app.gui.screen_vec) - 1
        else:
            new_ptr = app.gui.screen_ptr - 1

        app.cmd_queue.append(ModifyScreenPtrCommand(new_ptr))

    elif event.key == pygame.K_l and mods & pygame.KMOD_CTRL:
        new_ptr = app.gui.screen_ptr + 1
        new_ptr %= len(app.gui.screen_vec)

        app.cmd_queue.append(ModifyScreenPtrCommand(new_ptr))

    return
