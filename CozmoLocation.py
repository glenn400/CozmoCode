class CozmoLocation(object):
    def __init__(self, angle=0, distance=0, direction=0):
        # the polar coordinates of Cozmo
        self.angle = angle
        self.distance = distance
        # the angle Cozmo is facing
        self.direction = direction
