import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Barrier(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, cast):
        "Constructs a new Food."
        super().__init__()
        self._points = 50
        self.spawn_barrier(cast)
        
    def spawn_barrier(self, cast):
        """Selects a random position and points that the food is worth."""
        barrier_count =random.randint(20, 30)

        for n in range(barrier_count):
            x = random.randint(2, constants.COLUMNS - 3)
            y = random.randint(1, constants.ROWS)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)
            
            barrier = Actor()
            barrier.set_text("@")
            barrier.set_color(constants.YELLOW)
            barrier.set_position(position)
            barrier.set_points(self._points)
            cast.add_actor("barriers", barrier)

        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points