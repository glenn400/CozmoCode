class PinLocation(object):
    def __init__(self, angle=0, distance=0, isStanding=False, isObstructed=False, isSpare=False):
        # the polar coordinates of the pin location
        self.angle = angle
        # distance from origin
        self.distance = distance
        # is there is a pin in the location
        self.isStanding = isStanding
        # is there something in the way (downed pin)
        self.isObstructed = isObstructed
        # is this a location for a spare pin
        self.isSpare = isSpare
