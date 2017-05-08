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
        # cozmo will go to the pin that is marked as Down
        if (CozmoLocation.angle == self.angle):
            # set distance for comzo to travel to downed pin if the pin is down
            for i in len(self.penob.dpl):
                # if this pin is down create list of actions
                if (self.penob.dpl[i].down == 1):
                    # calculate polar coordinates of downed pin
                    # calculate where pin is using coordinates
                    xlocationPin = math.degrees(math.cos(self.penob.dpl[i].angle)) * self.penob.dpl[i].distance
                    ylocationPin = math.degrees(math.sin(self.penob.dpl[i].angle)) * self.penob.dpl[i].distance
                    # pass value into cozmo distance
                    self.actionque[0] = Cozmo_Actions.setDistance()
                    # set angle
                    self.actionque[1] = Cozmo_Actions.setAngle(self.angle)
                    # cozmo then turns to angle
                    self.actionque[2] = Cozmo_Actions.turnAction()
                    # go to the pin location
                    self.actionque[3] = Cozmo_Actions.moveAction()
                    # turn to the final angle to see pin
                    self.actionque[4] = Cozmo_Actions.setAngle(self.angle1)
                    # then pick up pin
                    # now take it to pin depot ?


class PlacePinTASK(CozmoTasks):
    # retrieve a spare pin and place it at a PinLocation
    def __init__(self, alpha, beta, actions):
        super().__init__(self, alpha, beta, actions)
        # this will be used to place the pin


class ChargeTask(CozmoTasks):
    def __init__(self):
        super(ChargeTask, self).__init__(self, alpha, beta, actions)
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
