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
class CollectPinTask(CozmoTasks):
    def __init__(self,alpha,beta,locationx,locationy,locationz):
        # this will be used for Cozmo to go to a Downed Pin
        CozmoTasks.__init__(self,alpha,beta)
        self.location = [locationx, locationy, locationz]
    def gotoPin(self):
        # cozmo will go to the pin that is marked as Down
