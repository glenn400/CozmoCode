class DownedPin(object):
    def __init__(self, angle=0, distance=0, headAngle=0):
        # the polar coordinates of the downed pin
        self.angle = angle
        self.distance = distance
        # the angle of the head of the pin
        # Cozmo must approach from this angle to pick up the pin
        self.headAngle = headAngle
