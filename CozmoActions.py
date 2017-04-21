import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees


# The importance of this file is to create actions for cozmo
# http://cozmosdk.anki.com/docs/generated/cozmo.action.html

class Cozmo_Actions:
    def __init__(self,speed,d,ang,h):
        self.speed = speed
        self.distance = d
        self.angle = ang
        self.height = h
    def _movebackward(self, distance, speed, robot):
        # travel backward
        robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()
    def _moveforward(self, distance, speed, robot):
        # move forward
        robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()
    def _rotate(self, angle, robot):
        # cozmo will rotate at some angle
        robot.turn_in_place(degrees(-angle)).wait_for_completed()
    def moveAction(self,robot: cozmo.robot.Robot):

        # cozmo moves a distance forward or backward
        if self.distance < 0:
            self._movebackward(self.distance, self.speed, robot)
        else:
            self._moveforward(self.distance, self.speed, robot)
    def turnAction(self, robot: cozmo.robot.Robot):
        # Cozmo turns right or left
        self._rotate(self.angle, robot)
    def liftAction(self,robot: cozmo.robot.Robot):
        # lift action
        self._lift(self.height,robot)
    def _lift(self,height,robot):
        robot.set_lift_height(height=height, accel=10.0, max_speed=10.0, duration=0.0, in_parallel=False, num_retries=3)

    def compositeAction(self,robot: cozmo.robot.Robot):
        robot.start_freeplay_behaviors()
    def stopcompositeAction(self,robot: cozmo.robot.Robot):
        robot.stop_freeplay_behaviors()
    def setSpeed(self,speed):
        self.speed = speed
    def setAngle(self,angle):
        self.angle = angle
    def setDistance(self,distance):
        self.distance = distance
    def setHeight(self,height):
        self.height = height


# testing commands
c = Cozmo_Actions(100,100,130,0.0)
#cozmo.run_program(c.moveAction)
#cozmo.run_program(c.turnAction)
#cozmo.run_program(c.liftAction)
cozmo.run_program(c.compositeAction)
