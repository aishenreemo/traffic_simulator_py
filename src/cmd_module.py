from enum import Enum


class CommandType(Enum):
    QUIT = 0


class Command:
    def __init__(self, type):
        self.type = type


class QuitCommand(Command):
    def __init__(self):
        super().__init__(CommandType.QUIT)
