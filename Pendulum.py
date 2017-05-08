from PinLocation import PinLocation
from CozmoLocation import CozmoLocation
from DownedPin import DownedPin


class Pendulum(object):
    def __init__(self, angle=0, displacement=0, cozmoLocation=None):
        # the angle through which the pendulum swings defined from geographic north
        self.angle = angle
        # the distance from the center of the bob as it swings
        # >0 if toward angle
        # <0 if away from angle
        self.displacement = displacement
        # this should be a hard coded list of all the locations where a pin could be placed, including spares
        # for test purposes
        self.pl = [PinLocation(0, 0, False, False, False) for x in range(60)]
        # a placeholder where downed pin objects will be placed when identified
        self.dpl = [DownedPin(0, 0, 0, 0) for i in range(60)]
        # a location where Cozmo currently is
        self.cozmoLocation = CozmoLocation(0, 0, 0)

    def dangerZone(self):
        # I'm not sure if we want to calculate the dangerZone here or in the planner.
        pass