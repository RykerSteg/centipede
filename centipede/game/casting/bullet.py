import constants
from game.casting.actor import Actor
from game.casting.robot import Robot
from game.shared.point import Point

class Bullet(Actor):
  '''
  Bullets that appear on the screen and move upwards toward the centipede.
  '''
  def __init__(self):
    super().__init__()
    self.set_color(constants.WHITE)
    robot = Robot()
    robot_position = robot.get_position() #same position as the Robot
    position = robot_position.add(Point(0, constants.CELL_SIZE))
    self.prepare_body(position)

  def prepare_body(self, position):
    text = "o"

    self.set_velocity(Point(0,2)) #Velocity of the bullet moving upward
    self.set_position(position)    
    self.set_text(text)