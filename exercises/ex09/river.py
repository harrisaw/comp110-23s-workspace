"""File to define River class."""


__author__: str = "730316865"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """DocString."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """DocString."""
        new_bears: list[Bear] = []
        new_fish: list[Fish] = []

        for individual in self.bears:
            if individual.age <= 5:
                new_bears.append(individual)

        for individual in self.fish:
            if individual.age <= 3:
                new_fish.append(individual)

        self.bears = new_bears
        self.fish = new_fish

        return None

    def remove_fish(self, amount: int) -> None:
        """DocString."""
        idx = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1

    def bears_eating(self):
        """DocString."""
        for individual in self.bears:
            if len(self.fish) >= 5:
                individual.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """DocString."""
        new_bears: list[Bear] = []
        for individual in self.bears:
            if individual.hunger_score >= 0:
                new_bears.append(individual)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """DocString."""
        baby_fish = 4 * (len(self.fish) // 2)
        idx = 0
        while idx < baby_fish:
            self.fish.append(Fish())
            idx += 1
        return None
    
    def repopulate_bears(self):
        """DocString."""
        baby_bears = len(self.bears) // 2
        idx = 0
        while idx < baby_bears:
            self.bears.append(Bear())
            idx += 1
        return None
    
    def view_river(self) -> None:
        """DocString."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # self.view_river()
        # Remove hungry Bear's from River
        self.check_hunger()
        # self.view_river()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # self.view_river()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # self.view_river()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # self.view_river()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None:
        """DocString."""
        i = 0
        while i < 7:
            self.one_river_day()
            i += 1
            
