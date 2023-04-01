from pygame.sprite import Sprite
from pygame import Surface
import pygame

from enum import Enum
from .cfg import Config
from .mem import Memory


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

        self.surface.fill(self.color)

        return

    def fill(self, color):
        self.surface.fill(color)

        return

    def rounded(
        self,
        width=0,
        border_radius=0,
        border_top_left_radius=-1,
        border_top_right_radius=-1,
        border_bottom_left_radius=-1,
        border_bottom_right_radius=-1
    ):
        pygame.draw.rect(
            self.surface,
            self.color,
            self.rect,
            width,
            border_radius,
            border_top_left_radius,
            border_top_right_radius,
            border_bottom_left_radius,
            border_bottom_right_radius,
        )

        return


def main_screen_init():
    cfg = Config()
    gui = Display()
    mem = Memory()

    screen = Screen("main")
    screen.bg_color = cfg.colorscheme["background"]

    # put 4 green squares
    for x, y, i in [(0, 0, 3), (0.6, 0, 2), (0, 0.6, 1), (0.6, 0.6, 0)]:
        size = (mem.window_size[0] * 0.4, mem.window_size[1] * 0.4)
        color = cfg.colorscheme["normal"]["green"]
        pos = (
            mem.window_size[0] * x,
            mem.window_size[1] * y
        )

        br = [0] * 4
        br[i] = 5

        rect = RectElement(size, pos, color)
        rect.fill(screen.bg_color)
        rect.rounded(0, 0, br[0], br[1], br[2], br[3])

        screen.element_vec.append(rect)

    # put vertical lines dividing roads
    for y in [0, 0.6]:
        size = (mem.window_size[0] * 0.01, mem.window_size[1] * 0.4)
        color = cfg.colorscheme["normal"]["white"]
        pos = (
            mem.window_size[0] * 0.495,
            mem.window_size[1] * y,
        )

        rect = RectElement(size, pos, color)
        rect.fill(screen.bg_color)
        rect.rounded(0, 5)

        screen.element_vec.append(rect)

    # put horizontal lines dividing roads
    for x in [0, 0.6]:
        size = (mem.window_size[0] * 0.4, mem.window_size[1] * 0.01)
        color = cfg.colorscheme["normal"]["white"]
        pos = (
            mem.window_size[0] * x,
            mem.window_size[1] * 0.495,
        )

        rect = RectElement(size, pos, color)
        rect.fill(screen.bg_color)
        rect.rounded(0, 5)

        screen.element_vec.append(rect)

    gui.screen_vec.append(screen)

    return
