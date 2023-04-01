from pygame.sprite import Sprite
from pygame import Surface
from enum import Enum
from .cfg_module import Config
from .mem_module import Memory


class Display:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Display, cls).__new__(cls)

        return cls.instance

    def init(self):
        self.screen_vec = []
        self.screen_ptr = 0

        main_screen_init()

        return

    def update(self):

        return


class Screen:
    def __init__(self, name, bg_color=(0, 0, 0), element_vec=[]):
        self.name = str(name)
        self.bg_color = bg_color
        self.element_vec = []

        return


class ElementType(Enum):
    RECT = 0


class Element(Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type

        return


class RectElement(Element):
    def __init__(self, size=(1, 1), pos=(0, 0), color=(0, 0, 0)):
        super().__init__(ElementType.RECT)

        try:
            if size[0] <= 0 or size[1] <= 0:
                raise ValueError("invalid size argument")
        except ValueError as err:
            print("RectElement.__init__(size):", err)
            exit(1)

        self.color = color
        self.size = size
        self.pos = pos
        self.surface = Surface(size)
        self.rect = self.surface.get_rect()

        self.surface.fill(color)

        return


def main_screen_init():
    cfg = Config()
    gui = Display()
    mem = Memory()

    print(cfg.colorscheme)
    screen = Screen("main")
    screen.bg_color = cfg.colorscheme["background"]

    positions = [(0, 0), (0.6, 0), (0, 0.6), (0.6, 0.6)]

    for position in positions:
        size = (mem.window_size[0] * 0.4, mem.window_size[1] * 0.4)
        color = cfg.colorscheme["normal"]["green"]
        pos = (
            mem.window_size[0] * position[0],
            mem.window_size[1] * position[1]
        )

        screen.element_vec.append(RectElement(size, pos, color))

    gui.screen_vec.append(screen)

    return
