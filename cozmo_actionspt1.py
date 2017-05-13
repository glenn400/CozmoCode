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

                            for i in self.penob.dpl:
            if self.penob.dpl[i].down == 1:
                # add angle vector to pin vector to acquire resulant vector in polar form
                phi = self.penob.dpl[i].angle
                d1 = self.penob.dpl[i].distance

                psi = self.penob.dpl[i].headAngle
                # d2 should equal the displacement or length of pin probrally which i will call 4 cm
                d2 = 4

                # r1x = cos(phi) (degrees) * distance r1y = sin(phi)*distance
                r1x = (math.cos(phi)) * d1
                r1y = (math.sin(phi)) * d1

                # r2x = cos(phi) (degrees) * distance r2y = sin(phi)*distance
                r2x = (math.cos(psi)) * d2
                r2y = (math.sin(psi)) * d2

                # now add them together
                r3x = r2x + r1x
                r3y = r2y + r1y

                # take the magnitude  & get the angle
                # resultant angle in alpha
                alpha = math.atan2(r3y,r3x)
                r4x = r3x * r3x
                r4y = r3y * r3y
                rr = r4x + r4y
                # resultant distance
                rr1 = math.sqrt(rr)

                angle = alpha - 90.0

                # cozmo should walk up and get as close as possible
                # cozmo should rotate 90 or 180 degree so that he is facing the pin
                self.actionque[0] = Cozmo_Actions.setAngle(angle)
                # turn cozmo
                self.actionque[1] = Cozmo_Actions.turnAction()
                # then move him to the pin
'''

cozmo.run_program(cozmo_program)