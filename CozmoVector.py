import math

class CozmoVector:
    def __init__(self, alpha, magnitude):
        self.angle = alpha
        self.distance = magnitude

    def setAlpha(self, alpha):
        self.angle = alpha

    def setmagnitude(self, magnitude):
        self.distance = magnitude

    def getAlpha(self):
        return self.angle

    def getMagnitude(self):
        return self.distance

    def addVectors(self, other):
        # r1x = cos(phi) (degrees) * distance r1y = sin(phi)*distance
        r1x = (math.cos(self.angle)) * self.distance
        r1y = (math.sin(self.angle)) * self.distance

        # r2x = cos(phi) (degrees) * distance r2y = sin(phi)*distance
        r2x = (math.cos(other.angle)) * other.direction
        r2y = (math.sin(other.angle)) * other.direction

        # now add them together
        r3x = r2x + r1x
        r3y = r2y + r1y

        # take the magnitude  & get the angle
        # resultant angle in alpha
        alpha = math.atan2(r3y, r3x)
        r4x = r3x * r3x
        r4y = r3y * r3y
        rr = r4x + r4y
        # resultant distance
        rr1 = math.sqrt(rr)

        retVector = CozmoVector(alpha, rr1)

        return retVector
