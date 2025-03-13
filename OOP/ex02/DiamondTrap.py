from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""
    def __init__(self, first_name, is_alive: bool = True):
        """King constructor"""
        super().__init__(first_name, is_alive)
        self.eyes = self.eyes  # Initialize eye color from parent class
        self.hairs = self.hairs  # Initialize hair color from parent class

    def get_eyes(self):
        """Getter method"""
        return self.eyes

    def set_eyes(self, color: str):
        """Setter method"""
        self.eyes = color

    def get_hairs(self):
        """Getter method"""
        return self.hairs

    def set_hairs(self, color: str):
        """Setter method"""
        self.hairs = color
