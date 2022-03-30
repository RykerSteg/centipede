import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_bullet_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_bullet_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # centipedes code
        score = cast.get_first_actor("scores")
        barriers = cast.get_actors("barriers")
        centipede = cast.get_first_actor("centipede")
        centipede_segments = centipede.get_segments()
        bullets = cast.get_actors("bullet")  
        
        for bullet in bullets:
            for segment in centipede_segments:
                if bullet.get_position().equals(segment.get_position()):

                    #points = segment.get_points()
                    points = segment.get_points()
                    score.add_points(points)
                    centipede.shrink_tail()
                    cast.remove_actor("bullet", bullet)
                    #score.add_points(points)
                   
            for barrier in barriers:
                if bullet.get_position().equals(barrier.get_position()):
                    if barrier.get_color() == constants.YELLOW:
                        points = barrier.get_points()
                        score.add_points(points)
                        barrier.set_color(constants.GREEN)
                        cast.remove_actor("bullet", bullet)
                    elif barrier.get_color() == constants.GREEN:
                        points = barrier.get_points() + 25
                        score.add_points(points)
                        barrier.set_color(constants.BLUE)
                        cast.remove_actor("bullet", bullet)
                    else:
                        points = barrier.get_points() + 50
                        score.add_points(points)                       
                        cast.remove_actor("barriers", barrier)
                        cast.remove_actor("bullet", bullet)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        centipede = cast.get_first_actor("centipede")
        centipede_length = len(centipede.get_segments())
        if  centipede_length < 1:
            self._is_game_over = True
        else:
            head = centipede.get_segments()[0]
            robot = cast.get_first_actor("robot")

        #Game will end if the centipede collides with the robot
        if head.get_position().equals(robot.get_position()):
            self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            centipede = cast.get_first_actor("centipede")
            segments = centipede.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
        pass