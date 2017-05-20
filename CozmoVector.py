# vector class for Cozmo


class CozmoVector:
    def __init__(self, alpha, magnitude, headAngle):
        self.angle = alpha
        self.direction = magnitude
        self.beta = headAngle

    def setAlpha(self, alpha):
        self.angle = alpha

    def setBeta(self, beta)
        self.beta = beta

    def setmagnitude(self, magnitude):
        self.direction = magnitude

    def getAlpha(self):
        return self.angle

    def getBeta(self):
        return self.beta

    def getMagnitude(self):
        return self.direction
