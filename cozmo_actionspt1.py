import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees
#from cozmo.util import

def cozmo_program(robot: cozmo.robot.Robot):
  robot.drive_wheels(l_wheel_speed=80.0,r_wheel_speed=100.0,l_wheel_acc=None,r_wheel_acc=None,duration=14.8
                     )
 # robot.drive_straight(distance_mm(100), speed_mmps(500)).wait_for_completed()
 #robot.drive_straight(distance_mm(-3000), speed_mmps(500)).wait_for_completed()
 # robot.turn_in_place(degrees(270)).wait_for_completed()
  #robot.turn_in_place(degrees(-180)).wait_for_completed()
# robot.set_lift_height(height=0.5, accel=10, in_parallel=False, num_retries=2, duration=3)
 # robot.set_lift_height(distance_mm(0))

  '''
        Ignore this
        if (CozmoLocation.angle == self.angle):
            # set distance for comzo to travel to downed pin if the pin is down
            for i in len(self.penob.dpl):
                # if this pin is down create list of actions
                if (self.penob.dpl[i].down == 1):
                    # calculate polar coordinates of downed pin
                    # calculate where pin is using coordinates
                    xlocationPin = math.degrees(math.cos(self.penob.dpl[i].angle)) * self.penob.dpl[i].distance
                    ylocationPin = math.degrees(math.sin(self.penob.dpl[i].angle)) * self.penob.dpl[i].distance
                    # pass value into cozmo distance
                    self.actionque[0] = Cozmo_Actions.setDistance()
                    # set angle
                    self.actionque[1] = Cozmo_Actions.setAngle(self.angle)
                    # cozmo then turns to angle
                    self.actionque[2] = Cozmo_Actions.turnAction()
                    # go to the pin location
                    self.actionque[3] = Cozmo_Actions.moveAction()
                    # turn to the final angle to see pin
                    self.actionque[4] = Cozmo_Actions.setAngle(self.angle1)
                    # then pick up pin
                    # now take it to pin depot ?
'''

cozmo.run_program(cozmo_program)