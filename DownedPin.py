from CozmoVector import CozmoVector

class DownedPin(object):
    #  the polar coordinates ovf the downed pin
    def __init__(self, angle, distance, headAngle, down=0):
        self.vector = CozmoVector(angle, distance)
        self.headangle = headAngle
        self.down = down