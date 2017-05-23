import cozmo
import math
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees

from CozmoActions import Cozmo_Actions
from Pendulum import Pendulum
from CozmoVector import CozmoVector
from CozmoLocation import CozmoLocation


# Task represents a goal for Cozmo must Achieve

# The importance of this file is to create tasks for cozmo
# http://cozmosdk.anki.com/docs/generated/cozmo.action.html

class CozmoTasks:
    def __init__(self, alpha, beta):
        # angle where cozmo begins task
        self.angle = alpha
        # angle where cozmo ends task
        self.angle1 = beta
        # action que each class must have
        self.actionque = []
        # based on image processing
        self.C = Cozmo_Actions(0, 0, 0, 0)
        self.pinLocation = CozmoVector(0, 0)
        self.cozmoLocation = CozmoLocation(0, 0, 0)
        self.pendulum = Pendulum(0, 0, None)

    def getFallenLocation(self, vector):
        self.pinLocation = vector

    def getCozmoLocation(self, vector):
        self.cozmoLocation = vector


class CollectPinTask(CozmoTasks):
    def __init__(self, alpha, beta):
        # this will be used for Cozmo to go to a Downed Pin
        super().__init__(alpha, beta)
        # for testing

    def retrievePin(self, i):
        # this event should precede or come after a drive to command

        # Cozmo will be some distance away facing the ending angle of the last task
        # check to see if his current head angle and the angle we want him to point toward are the same

        if self.cozmoLocation.headangle != self.angle:
            # if cozmoLocation.headangle != self.angle move Cozmo to the desired angle using the circle task
            self.actionque[0] = self.C.setAngle(self.angle)
            # rotate cozmo
            self.actionque[1] = self.C.turnAction()
            # i represents distance cozmo must travel to get to pin
            self.actionque[2] = self.C.setDistance(i)
            self.actionque[3] = self.C.moveAction()
            # now that cozmo must turn to face fallen pin which is the value found in angle1
            self.actionque[4] = self.C.setAngle(self.angle1)
            self.actionque[5] = self.C.turnAction()
            # now cozmo should be facing pin and should be some set distance away like 12 cm for ex
            self.actionque[6] = self.C.setDistance(6)
            self.actionque[7] = self.C.moveAction()
            # assuming cozmo has for down, pin should be halfway between beginning and end of cozmo tool so pick it up
            self.actionque[8] = self.C.setHeight(1.0)
            self.actionque[9] = self.C.liftAction()
            # rotate cozmo head angle to vector angle to get him out to designated circle
            self.actionque[10] = self.C.setAngle(self.angle)
            self.actionque[11] = self.C.turnAction()
            # now drive cozmo soem distance that is safe away from orgin
            self.actionque[12] = self.C.setDistance(i)
            self.actionque[13] = self.C.moveAction()
            # task is over by the point
            return
        else:
            # if cozmo.headangle == angle simply move cozmo in by distance i

            # i represents distance cozmo must travel to get to pin
            self.actionque[0] = self.C.setDistance(i)
            self.actionque[1] = self.C.moveAction()
            # now that cozmo must turn to face fallen pin which is the value found in angle1
            self.actionque[2] = self.C.setAngle(self.angle1)
            self.actionque[3] = self.C.turnAction()
            # now cozmo should be facing pin and should be some set distance away like 12 cm for ex
            self.actionque[4] = self.C.setDistance(6)
            self.actionque[5] = self.C.moveAction()
            # assuming cozmo has for down, pin should be halfway between beginning and end of cozmo tool so pick it up
            self.actionque[6] = self.C.setHeight(1.0)
            self.actionque[7] = self.C.liftAction()
            # rotate cozmo head angle to vector angle to get him out to designated circle
            self.actionque[8] = self.C.setAngle(self.angle)
            self.actionque[9] = self.C.turnAction()
            # now drive cozmo soem distance that is safe away from orgin
            self.actionque[10] = self.C.setDistance(i)
            self.actionque[11] = self.C.moveAction()
            # task is over by the point
            return

    def placepinindepot(self, i):
        # once Cozmo has circle to same angle as pin depot at some distance away we can take pin to pin depot
        # in order to run this task . program should have new start and end angle

        # assuming that if cozmo has gotten to the correct angle we do not need to check that parameter, we will do that in mission control
        # but we should check to see if cozmo is facing correct direction, which should be populated using get CozmoLocation

        # pin depot location can be hard coded in for testing sake it will be set to 270 degrees
        if self.cozmoLocation != 270:
            self.actionque[0] = self.C.setAngle(self.angle)
            # rotate cozmo
            self.actionque[1] = self.C.turnAction()
            # i represents distance cozmo must travel to get to pin depot
            self.actionque[2] = self.C.setDistance(i)
            self.actionque[3] = self.C.moveAction()
            # Cozmo can now drop pin , or lower his fork half way
            self.actionque[4] = self.C.setHeight(0.5)
            self.actionque[5] = self.C.liftAction()
            # cozmo can now back away from pin
            self.actionque[6] = self.C.setDistance(-i)
            self.actionque[7] = self.C.moveAction()
            # once this done turn Cozmo to his ending angle
            self.actionque[8] = self.C.setAngle(self.angle1)
            self.actionque[9] = self.C.turnAction()
            return

        else:
            # if cozmo.headangle == angle1 , no need to rotate cozmo

            # i represents distance cozmo must travel to get to pin depot
            self.actionque[0] = self.C.setDistance(i)
            self.actionque[1] = self.C.moveAction()
            # Cozmo can now drop pin , or lower his fork half way
            self.actionque[2] = self.C.setHeight(0.5)
            self.actionque[3] = self.C.liftAction()
            # cozmo can now back away from pin
            self.actionque[4] = self.C.setDistance(-i)
            self.actionque[5] = self.C.moveAction()
            # once this done turn Cozmo to his ending angle
            self.actionque[6] = self.C.setAngle(self.angle1)
            self.actionque[7] = self.C.turnAction()


# need to test
class PlacePinTASK(CozmoTasks):
    # retrieve a spare pin and place it at a PinLocation
    def __init__(self, alpha, beta):
        super().__init__(alpha, beta)

    def placePininemptylocation(self, j):
        # this task is to place pin in location of empty pin
        # this task should be run after cozmo has circled to angle where pin will go

        # check to see if cozmo is facing the same direction as his initial angle value angle 1
        if self.angle1 != self.cozmoLocation.headangle:
            # turn cozmo to face the correct angle
            self.actionque[0] = self.C.setAngle(self.angle)
            self.actionque[1] = self.C.turnAction()
            # now that cozmo is facing the correct way, move distance j to pin location
            self.actionque[2] = self.C.setDistance(j)
            self.actionque[3] = self.C.moveAction()
            # now that cozmo is where pin is placed set the pin down, assuming cozmo fork is up
            self.actionque[4] = self.C.setHeight(0.5)
            self.actionque[5] = self.C.liftAction()
            # once pin is set down cozmo is to move backward away from pin
            self.actionque[6] = self.C.setDistance(j)
            self.actionque[7] = self.C.moveAction()
            # rotate to angle1 which is final angle
            self.actionque[8] = self.C.setAngle(self.angle1)
            self.actionque[9] = self.C.turnAction()
            return
        else:
            # if cozmo.headangle == angle1 then cozmo can simply move to pin location
            # now that cozmo is facing the correct way, move distance j to pin location
            self.actionque[0] = self.C.setDistance(j)
            self.actionque[1] = self.C.moveAction()
            # now that cozmo is where pin is placed set the pin down, assuming cozmo fork is up
            self.actionque[2] = self.C.setHeight(0.5)
            self.actionque[3] = self.C.liftAction()
            # once pin is set down cozmo is to move backward away from pin
            self.actionque[4] = self.C.setDistance(-j)
            self.actionque[5] = self.C.moveAction()
            # rotate to angle1 which is final angle
            self.actionque[6] = self.C.setAngle(self.angle1)
            self.actionque[7] = self.C.turnAction()
            return

    def getpinfromdepot(self, j):
        # this function is to retrieve pin from pin depot to placed in empty pin location
        # cozmo should be at the correct angle of pin depot so we must check to see where he is facing
        if self.cozmoLocation.headangle != self.angle1:
            # turn cozmo to face the correct angle
            self.actionque[0] = self.C.setAngle(self.angle)
            self.actionque[1] = self.C.turnAction()
            # now that cozmo is facing the correct way, move distance j to pin depot
            self.actionque[2] = self.C.setDistance(j)
            self.actionque[3] = self.C.moveAction()
            # now that cozmo is where pin is, assuming his forks are down he will pick it up
            self.actionque[4] = self.C.setHeight(1.0)
            self.actionque[5] = self.C.liftAction()
            # once pin is up cozmo is to move backward away from depot
            self.actionque[6] = self.C.setDistance(-j)
            self.actionque[7] = self.C.moveAction()
            # rotate to angle1 which is final angle
            self.actionque[8] = self.C.setAngle(self.angle1)
            self.actionque[9] = self.C.turnAction()
            return

        else:
            # if cozmo is facing the correct direction we can skip changing his angle
            # now that cozmo is facing the correct way, move distance j to pin depot
            self.actionque[0] = self.C.setDistance(j)
            self.actionque[1] = self.C.moveAction()
            # now that cozmo is where pin is, assuming his forks are down he will pick it up
            self.actionque[2] = self.C.setHeight(1.0)
            self.actionque[3] = self.C.liftAction()
            # once pin is up cozmo is to move backward away from depot
            self.actionque[4] = self.C.setDistance(-j)
            self.actionque[5] = self.C.moveAction()
            # rotate to angle1 which is final angle
            self.actionque[6] = self.C.setAngle(self.angle1)
            self.actionque[7] = self.C.turnAction()
            return



class ChargeTask(CozmoTasks):
    def __init__(self):
        super().__init__(alpha=0, beta=0)
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


# need to test
class GetToPin(CozmoTasks):
    # get to Pin task is solely for going to a pin not picking it up
    def __init__(self, alpha, beta):
        # setting to 0 for testing purposes
        super().__init__(alpha, beta)
        # instantiate queue for actions

    def gotoPin(self):
        # set turn in degrees
        self.actionque[0] = self.C.setAngle(self.angle)
        # start from given start angle to get to pin
        self.actionque[1] = self.C.turnAction()
        # once cozmo is turned he should go to pin location
        self.actionque[2] = self.C.circleAction()
        # set the angle he should finally face
        self.actionque[3] = self.C.setAngle(self.angle1)
        # turn to that angle and end task
        self.actionque[4] = self.C.turnAction()
