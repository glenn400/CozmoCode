from CozmoVector import CozmoVector

class PinLocation(object):
    def __init__(self, angle, distance, isStanding=False, isObstructed=False, isSpare=False):
        # the polar coordinates of the pin location including angle and distance
        self.vector = CozmoVector(angle, distance, 0)
        # is there is a pin in the location
        self.isStanding = isStanding
        # is there something in the way (downed pin)
        self.isObstructed = isObstructed
        # is this a location for a spare pin
        self.isSpare = isSpare
