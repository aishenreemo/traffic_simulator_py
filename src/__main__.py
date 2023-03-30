import pygame
from .app_module import App


def main():
    pygame.init()
    app = App()

    while app.running:
        app.listen()
        app.update()
        app.render()
        app.tick()


if __name__ == "__main__":
    main()
