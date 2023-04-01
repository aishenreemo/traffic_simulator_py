import pygame
from .app import App


def main():
    app = App()

    pygame.init()
    app.init()

    while app.running:
        app.listen()
        app.update()
        app.render()
        app.tick()


if __name__ == "__main__":
    main()
