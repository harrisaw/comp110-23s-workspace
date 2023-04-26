"""File to define Bear class."""


class Bear:
    """DocString."""

    age: int
    hunger_score: int

    def __init__(self):
        """DocString."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """DocString."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """DocString."""
        self.hunger_score += num_fish
        return None
    
    def __str__(self) -> str:
        """DocString."""
        return (f"Age: {self.age}; Hunger: {self.hunger_score}")