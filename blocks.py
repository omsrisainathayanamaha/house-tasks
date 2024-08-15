import os.path
import constants as c
import json
class Person:
    def __init__(self, name, hrsReqCleaning, hrsReqKitchen):
        self.name = name
        self.weeklyHoursCleaningRequired = hrsReqCleaning
        self.weeklyHoursKitchenRequired = hrsReqKitchen
        self.currentTotalHours = 0
        self.weeklyHoursCleaningRemaining = hrsReqCleaning
        self.weeklyHoursKitchenRemaining = hrsReqKitchen
        self.assignedTasks = [] # list of assigned tasks

class Task:
    def __init__(self, name, minReq, date):
        self.name = name
        self.time = minReq
        self.isComplete = False
        self.date = date # this is a string
        self.timeRemaining = minReq
    def setCompleteStatus(self):
        if self.timeRemaining == 0:
            self.isComplete = True

class Store:
    def __init__(self, data, isParsed):
        self.myPeople = data
        self.isParsed = isParsed
    def checkMyPeople(self):
        if(self.isParsed):
            return
        if(not os.path.isfile('data.txt')):
            self.myPeople = [Person("Sahanav", c.SAHANAV_CLEANING_HOURS, c.SAHANAV_KITCHEN_HOURS), Person("Priya", c.PRIYA_CLEANING_HOURS, c.PRIYA_KITCHEN_HOURS), Person("Ramesh", c.RAMESH_CLEANING_HOURS, c.RAMESH_KITCHEN_HOURS), Person("Vimarsha", c.VIMARSHA_CLEANING_HOURS, c.VIMARSHA_KITCHEN_HOURS)]
            return
        fileToRead = open('data.txt', 'r')
        for x in fileToRead:
            stuff = x.split(";")
            currentPerson = Person(stuff[0], int(stuff[1]), int(stuff[2]))
            currentPerson.currentTotalHours = int(stuff[3])
            currentPerson.weeklyHoursKitchenRemaining = int(stuff[5])
            currentPerson.weeklyHoursCleaningRemaining = int(stuff[4])
            tasks = stuff[6].split(',')
            for n in tasks:
                props = n.split('/')
                currentTask = Task(props[0], int(props[1]), props[3])
                currentTask.isComplete = bool(props[2])
                currentTask.timeRemaining = int(props[4])
                self.assignedTasks.append(currentTask)
            
            self.myPeople.append(currentPerson)
        self.isParsed = True
    def storeMyPeople(self):
        fileToWrite = open('data.txt', 'w')
        for i in self.myPeople:
            fileToWrite.write(self.myPeople.name+";"+self.myPeople.weeklyHoursCleaningRequired+";"+self.myPeople.weeklyHoursKitchenRequired+";"+self.myPeople.currentTotalHours+";"+self.myPeople.weeklyHoursCleaningRemaining+";"+self.myPeople.weeklyHoursKitchenRemaining+";")
            for j in i.assignedTasks:
                fileToWrite.write(j.name+'/'+j.time+'/'+j.isComplete+'/'+j.date+'/'+j.timeRemaining)
                if not (i.assignedTasks[len(i.assignedTasks)-1] == j):
                    fileToWrite.write(',')
            fileToWrite.write('\n')
class TaskStore:
    def __init__(self, tasks, isParsed):
        self.myTasks = tasks
        self.isParsed = isParsed
    def checkMyTasks(self):
        if(self.isParsed):
            return
        if(not os.path.isfile('tasks.txt')):
            self.myTasks = []
            return
        fileToRead = open('tasks.txt', 'r')
        
        for x in fileToRead:
                props = x.split('/')
                currentTask = Task(props[0], int(props[1]), props[3])
                currentTask.isComplete = bool(props[2])
                currentTask.timeRemaining = int(props[4])
                self.assignedTasks.append(currentTask)
    def storeMyTasks(self):
        fileToWrite = open('tasks.txt', 'w')
        for j in self.myTasks:
            fileToWrite.write(j.name+'/'+j.time+'/'+j.isComplete+'/'+j.date+'/'+j.timeRemaining)
            if not (self.myTasks[len(self.myTasks)-1] == j):
                fileToWrite.write(',')
        fileToWrite.write('\n')
    
def convertTaskToJSON(t: Task):
    return json.dumps(t.__dict__)
def convertPersonToJSON(p: Person):
    return json.dumps(p.__dict__)