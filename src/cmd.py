from enum import Enum


class CommandType(Enum):
    QUIT = 0
    MODIFY_SCREEN_PTR = 1


class Command:
    def __init__(self, type):
        self.type = type


class QuitCommand(Command):
    def __init__(self):
        super().__init__(CommandType.QUIT)


class ModifyScreenPtrCommand(Command):
    def __init__(self, new_ptr):
        super().__init__(CommandType.MODIFY_SCREEN_PTR)
        self.new_ptr = new_ptr
