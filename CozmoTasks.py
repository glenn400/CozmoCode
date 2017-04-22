import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees

from CozmoActions import Cozmo_Actions

# Task represents a goal for Cozmo must Achieve


# The importance of this file is to create tasks for cozmo
# http://cozmosdk.anki.com/docs/generated/cozmo.action.html

class CozmoTasks:
    def __init__(self, alpha, beta):
        # angle where cozmo begins task
        self.angle = alpha
        # angle where cozmo ends task
        self.angle1 = beta
        # action queue
        self.actionsList = Cozmo_Actions(0, 0, 0, 0.0)
        self.actionque = [] * 20
class CollectPinTask(CozmoTasks):
    def __init__(self,alpha,beta,angle,dfo,angle1):
        # this will be used for Cozmo to go to a Downed Pin
        super().__init__(self,alpha,beta)
        # angle that it fell at
        # distance from the origin
        # angle from which cozmo should approach the downed pin
        self.locationofDPin = [angle, dfo, angle1]

    def gotoPin(self):
        # cozmo will go to the pin that is marked as Down
        # If cozmo angle != pin location angle
        # rotate to that angle
        if ():
            #