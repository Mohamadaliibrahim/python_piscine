import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class Student"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """Automatically sets the login after initialization."""
        self.login = self.name[0].capitalize() + self.surname.lower()
