import cozmo
import math
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees

from CozmoActions import Cozmo_Actions
from Pendulum import Pendulum


# Task represents a goal for Cozmo must Achieve

# The importance of this file is to create tasks for cozmo
# http://cozmosdk.anki.com/docs/generated/cozmo.action.html

class CozmoTasks:
    def __init__(self, alpha, beta, actions):
        # angle where cozmo begins task
        self.angle = alpha
        # angle where cozmo ends task
        self.angle1 = beta
        self.actionque = []
        # based on image processing


class CollectPinTask(CozmoTasks):
    def __init__(self):
        # this will be used for Cozmo to go to a Downed Pin
        super().__init__(self)
        # for testing
        self.penob = Pendulum(0, 0, None)
        # angle that it fell at
        # distance from the origin
        # angle from which cozmo should approach the downed pin
        # self.downedpinList = Pendulum.downedPins
        # will populate location based on image processing

    def retrievePin(self):
        # this action will be used after cozmo circles around to near fallen pin
        # get those values from pendulum object which has the down pin info
        # how do I identify fallen pin in the Que ?
            #



class PlacePinTASK(CozmoTasks):
    # retrieve a spare pin and place it at a PinLocation
    def __init__(self):
        super().__init__(alpha=0,beta=0,actions=None)
        # this will be used to place the pin
        self.actionque = []
        # these references will be updated by image processor , for testing purposes we will add default values
        self.pendulum =Pendulum(0,0,None)

    def placePin(self,i):
        # check if cozmo is at pin depot
        # if he is at pin depot have him pick up the pin
        # use GoToPin Task to get him
        # identify which pin is not standing

        # depending on that fallen pin location we can add its vector with cozmo's to get where cozmo should be
        # add angle vector to pin vector to acquire resulant vector in polar form
        phi = self.penob.dpl[i].angle
        d1 = self.penob.dpl[i].distance

        psi = self.penob.dpl[i].headAngle
        # d2 should equal the displacement or length of pin probrally which i will call 4 cm
        d2 = 4

        # r1x = cos(phi) (degrees) * distance r1y = sin(phi)*distance
        r1x = (math.cos(phi)) * d1
        r1y = (math.sin(phi)) * d1

        # r2x = cos(phi) (degrees) * distance r2y = sin(phi)*distance
        r2x = (math.cos(psi)) * d2
        r2y = (math.sin(psi)) * d2

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

        angle = alpha - 90.0

        # cozmo should walk up and get as close as possible
        # cozmo should rotate 90 or 180 degree so that he is facing the pin
        self.actionque[0] = Cozmo_Actions.setAngle(angle)
        # turn cozmo
        self.actionque[1] = Cozmo_Actions.turnAction()
        # then move him to the pin

class ChargeTask(CozmoTasks):
    def __init__(self):
        super().__init__(alpha=0, beta=0, actions=None)
        # for testing purposes those are polar location of charger near outlet
        self.chargerLocationAngle = 90.0
        self.chargerLocationDistance = 50.0

    def chargeCozmo(self):
        # have cozmo turn to appropiate angle which is passed in through super class
        self.actionque[0] = Cozmo_Actions.setAngle(self.angle)
        # now drive Cozmo to that point
        self.actionque[1] = Cozmo_Actions.circleAction()
        # Cozmo should be at the angle where the charger is but at a 90 degree difference so turn him 90 degrees
        # if cozmo angle is 180 subtract 90 , if cozmo angle is 0 add 90
        if self.angle1 is 180:
            self.actionque[2] = Cozmo_Actions.setAngle(self.angle1 - 90)
            self.actionque[3] = Cozmo_Actions.turnAction()
            self.actionque[4] = Cozmo_Actions.setDistance(self.chargerLocationDistance - 5.0)
            self.actionque[5] = Cozmo_Actions.chargeCozmo()
        else:
            self.actionque[2] = Cozmo_Actions.setAngle(self.angle1 + 90)
            self.actionque[3] = Cozmo_Actions.turnAction()
            self.actionque[4] = Cozmo_Actions.setDistance(self.chargerLocationDistance - 5.0)
            self.actionque[5] = Cozmo_Actions.chargeCozmo()


class GetToPin(CozmoTasks):
    # get to Pin task is solely for going to a pin not picking it up
    def __init__(self):
        # setting to 0 for testing purposes
        super().__init__(alpha=0, beta=0, actions=None)
        # instatiate que for actions
        self.actionque = []

    def gotoPin(self):
        # set turn in degrees
        self.actionque[0] = Cozmo_Actions.setAngle(self.angle)
        # start from given start angle to get to pin
        self.actionque[1] = Cozmo_Actions.turnAction()
        # once cozmo is turned he should go to pin location
        self.actionque[2] = Cozmo_Actions.circleAction()
        # set the angle he should finally face
        self.actionque[3] = Cozmo_Actions.setAngle(self.angle1)
        # turn to that angle and end task
        self.actionque[4] = Cozmo_Actions.turnAction()




