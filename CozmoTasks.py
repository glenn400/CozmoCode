import cozmo
import math
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees

from CozmoActions import Cozmo_Actions
from CozmoLocation import CozmoLocation
from DownedPin import DownedPin
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
        for i in self.penob.dpl:
            if self.penob.dpl[i].down == 1:
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
                alpha = math.atan2(r3y,r3x)
                r4x = r3x * r3x
                r4y = r3y * r3y
                rr = r4x + r4y
                # resaultant distance
                rr1 = math.sqrt(rr)

                angle = alpha - 90.0
                # cozmo should walk up and get as close as possible
                # cozmo should rotate 90 or 180 degree so that he is facing the pin
                self.actionque[0] = Cozmo_Actions.setAngle(angle)
                # turn cozmo
                self.actionque[1] = Cozmo_Actions.turnAction()
                # then move him to the pin



class PlacePinTASK(CozmoTasks):
    # retrieve a spare pin and place it at a PinLocation
    def __init__(self, alpha, beta, actions):
        super().__init__(alpha=0,beta=0,actions=None)
        # this will be used to place the pin


class ChargeTask(CozmoTasks):
    def __init__(self):
        super().__init__(alpha=0, beta=0, actions=None)
        # for testin purposes those are polar location of charger near outlet
        self.chargerLocationAngle = 90
        self.chargerLocationDistance = 50

    def chargeCozmo(self):
        # have cozmo turn to appropiate angle of charger
        self.actionque[0] = Cozmo_Actions.setAngle(self.angle)
        # now turn cozmo
        self.actionque[1] = Cozmo_Actions.turnAction()
        # go to charger location based on cozmo location
        self.actionque[2] = Cozmo_Actions.setDistance()
        # once he sees charger turn around, Cozmo has 5 seconds to back into charger , should check to see if he is charging or if hes on charger
        self.actionque[3] = Cozmo_Actions.chargeCozmo()


class GetToPin(CozmoTasks):
    def __init__(self):
        super().__init__(alpha=0,beta=0,actions=None)
        # instatiate que for actions
        self.actionque = []
    def gotoPin(self):
        # set turn in degrees
        self.actionque[0] = Cozmo_Actions.setAngle(self.angle)
        # start from given start angle to get to pin
        self.actionque[1] = Cozmo_Actions.turnAction()
        # once cozmo is turned he should go to pin location
        self.actionque[2] = Cozmo_Actions.circleAction()




