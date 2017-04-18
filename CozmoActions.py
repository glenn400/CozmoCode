import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees


# The importance of this file is to create actions for cozmo
# http://cozmosdk.anki.com/docs/generated/cozmo.action.html

class Cozmo_Actions:
    def _movebackward(self, distance, speed, robot):
        # travel backward
        robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()
    def _moveforward(self, distance, speed, robot):
        # move forward
        robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()
    def _rotate(self, angle, robot):
        # cozmo will rotate at some angle
        robot.turn_in_place(degrees(-angle)).wait_for_completed()
    #def _liftArms(self,height,speed):
    def moveAction(self, distance, speed, robot: cozmo.robot.Robot):
        # cozmo moves a distance forward or backward
        if distance < 0:
            self._movebackward(distance, speed, robot)
        else:
            self._moveforward(distance, speed, robot)
    def turnAction(self, robot: cozmo.robot.Robot, angle):
        # Cozmo turns right or left
        self._rotate(angle, robot)
    #def compositeAction(self):
