'''
MissionControl directly controls Cozmo:
Maintains a priority queue of Tasks for Cozmo to complete
Inject charging Tasks as needed
Inject canned routines when no Tasks are available
Populates a queue of Actions for Cozmo when a task is started:
Actions needed between Tasks
Move from endAngle to startAngle
Cross the danger zone
A sentinel Action to trigger injection of next Task
Actions defined in the next Task which does not place Cozmo in the danger zone
Feeds Actions from queue to Cozmo for execution

'''
