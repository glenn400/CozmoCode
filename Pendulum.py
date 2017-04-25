class Pendulum(object):
    def __init__(self, angle=0, displacement=0, cozmoLocation=None):
        # the angle through which the pendulum swings defined from geographic north
        self.angle = angle
        # the distance from the center of the bob as it swings
        # >0 if toward angle
        # <0 if away from angle
        self.displacement = displacement
        # this should be a hard coded list of all the locations where a pin could be placed, including spares
        self.pinLocations = []
        # a placeholder where downed pin objects will be placed when identified
        self.downedPins = []
        # a location where Cozmo currently is
        self.cozmoLocation = cozmoLocation

    def dangerZone(self):
        # I'm not sure if we want to calculate the dangerZone here or in the planner.
        pass
