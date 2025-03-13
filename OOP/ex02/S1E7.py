from S1E9 import Character


class Baratheon(Character):
    """Barathon class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.first_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Ruturn a string that represent the object."""
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""
        return self.__str__()

    def die(self):
        """Make is_alive False."""
        self.is_alive = False


class Lannister(Character):
    """Lannister Class"""

    def __init__(self, first_name, is_alive: bool = True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.first_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Returns a string that represent the object."""
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""
        return self.__str__()

    def die(self):
        """Make is_alive to False."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create Lannister object with the given first name"""
        return cls(first_name, is_alive)
