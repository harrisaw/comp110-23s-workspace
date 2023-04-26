"""EX09: River Simulation."""


from exercises.ex09.river import River

my_river: River = River(10, 2)

my_river.view_river()

my_river.one_river_week()


# python -m exercises.ex09.river_simulation
# python -m tools.submission exercises/ex09