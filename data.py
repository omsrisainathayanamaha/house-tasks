import blocks
import constants as c
import json

initialStore = blocks.Store([], False)
initialStore.checkMyPeople()

people = initialStore.myPeople.copy()

taskStore = blocks.TaskStore([], False)
taskStore.checkMyTasks()

tasks = taskStore.myTasks.copy()

# people and tasks are now lists of People and Tasks respectively
# getPersonObject returns a tuple. The first element of the tuple is the Person object, while the second is the index in the array it was found. If no person with that username was found, it returns None,-1
def getPersonObject(username):
    index = 0
    for p in people:
        if username == p:
            return (p, index)
        index-=-1 #hehehe how do you like that increment
    return (None, -1)
# deep thoughts: parameters are just tuples



