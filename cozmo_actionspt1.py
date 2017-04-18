import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees
#from cozmo.util import

def cozmo_program(robot: cozmo.robot.Robot):
 # robot.drive_straight(distance_mm(100), speed_mmps(500)).wait_for_completed()
 #robot.drive_straight(distance_mm(-3000), speed_mmps(500)).wait_for_completed()
 # robot.turn_in_place(degrees(270)).wait_for_completed()
  #robot.turn_in_place(degrees(-180)).wait_for_completed()
  robot.set_lift_height(height=0.5, accel=10, in_parallel=False, num_retries=2, duration=3)
 # robot.set_lift_height(distance_mm(0))


cozmo.run_program(cozmo_program)