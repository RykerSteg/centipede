#from centipede.centipede.constants import CELL_SIZE
#from centipede.centipede.game.casting.centipede import Centipede
import constants

from game.scripting.action import Action
from game.shared.point import Point
from game.casting.centipede import Centipede


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._move_down = Point(0, constants.CELL_SIZE)
        self._previous_direction = Point(0,0)
        self._rotate = 0

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #probably break this into another method

        self._player_movement(cast)
        self._centipede_movement(cast)

    def _player_movement(self, cast):
        #centipede = cast.get_actors("centipede")

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        #centipede = centipede[0]
        #centipede.turn_head(self._direction1)

    def _centipede_movement(self, cast):
        centipede = cast.get_first_actor("centipede")

        my_head = centipede.get_segments()[0]
        my_position = my_head.get_position()
        my_velocity = my_head.get_velocity()

        if self._rotate == 0:
            if (my_position.get_x() <= 0) or (my_position.get_x() + constants.CELL_SIZE >= constants.MAX_X):
                self._previous_direction = my_velocity.get_x()
                centipede.turn_head(self._move_down)
                self._rotate = 1
        else:
            centipede.turn_head(Point(self._previous_direction * -1, 0))
            self._rotate = 0