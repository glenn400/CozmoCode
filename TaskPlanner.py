'''
The TaskPlanner creates Tasks from DownedPins and empty, non-spare PinLocations
'''

import Cozmo
from CozmoTasks import CozmoTasks
from CozmoTasks import Cozmo_Actions
from CozmoTasks import CozmoLocation
from Pendulum import Pendulum


class TaskPlanner:
    def __init__(self):
        self.taskque = CozmoTasks(0, 0)
