from CozmoVector import CozmoVector

class CozmoLocation(object):
    def __init__(self, angle, distance, direction):
        self.vector = CozmoVector(angle, distance, direction)
