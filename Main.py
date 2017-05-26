import cozmo
from CozmoTasks import Cozmo_Actions
from CozmoTasks import CozmoTasks
from CozmoTasks import CollectPinTask
from CozmoTasks import ChargeTask
from CozmoTasks import GetToPin
from CozmoTasks import PlacePinTASK

from CozmoTasks import CozmoLocation
from CozmoTasks import Pendulum

# test circle method
c = GetToPin(50, 75)
c.gotoPin()

# test collect pin method
d = CollectPinTask(45, 35)
d.retrievePin(450)
d.placepinindepot(780)

# test place pin task
e = PlacePinTASK(89, 32)
e.placePininemptylocation(657)
e.getpinfromdepot(745)

# test place pin task
charge = ChargeTask
charge.chargeCozmo()
