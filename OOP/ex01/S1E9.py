from abc import ABC, abstractmethod


class Character(ABC):
    """character class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Character construnctor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """destructor"""
        pass


class Stark(Character):
    """stark class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Strack construnctor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Make the is_alive = False"""
        self.is_alive = False
