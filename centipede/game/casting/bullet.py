import constants
from game.casting.actor import Actor
from game.casting.robot import Robot
from game.shared.point import Point

class Bullet(Actor):
  '''
  Bullets that appear on the screen and move upwards toward the centipede.
  '''
  def __init__(self, color):
    super().__init__()
    self.set_color(color)
    self.prepare_body()

  def prepare_body(self):
    position = Robot.set_position()    #Same position as robot
    text = "o"

    self.set_velocity(Point(0,2)) #Velocity of the bullet moving upward
    self.set_position(position)    
    self.set_text(text)