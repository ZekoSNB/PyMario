import abc


class CanvasObject(abc.ABC):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abc.abstractmethod
    def draw_rect(self, screen):
        pass

    @abc.abstractmethod
    def update(self, screen):
        pass

    @abc.abstractmethod
    def get_x(self):
        return self.x

    @abc.abstractmethod
    def get_y(self):
        return self.y

    @abc.abstractmethod
    def get_width(self):
        return self.width

    @abc.abstractmethod
    def get_height(self):
        return self.height

    @abc.abstractmethod
    def set_x(self, x):
        self.x = x

    @abc.abstractmethod
    def set_y(self, y):
        self.y = y

    @abc.abstractmethod
    def set_width(self, width):
        self.width = width

    @abc.abstractmethod
    def set_height(self, height):
        self.height = height
