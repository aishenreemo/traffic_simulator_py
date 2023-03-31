class Display:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Display, cls).__new__(cls)

        return cls.instance

    def init(self):
        self.screen_vec = []
        self.screen_ptr = 0

        # python is really weird
        # idk how this code below just works!

        screen = Screen("red")
        screen.bg_color = (255, 0, 0)
        self.screen_vec.append(screen)

        screen = Screen("green")
        screen.bg_color = (0, 255, 0)
        self.screen_vec.append(screen)

        screen = Screen("blue")
        screen.bg_color = (0, 0, 255)
        self.screen_vec.append(screen)

        return

    def update(self):

        return


class Screen:
    def __init__(self, name, bg_color=(0, 0, 0)):
        self.name = str(name)
        self.bg_color = bg_color

        return
