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

class Store:
    def __init__(self, data, isParsed):
        self.myPeople = data
        self.isParsed = isParsed
    def checkMyPeople(self):
        if(self.isParsed):
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
                self.assignedTasks.append(currentTask)
            
            self.myPeople.append(currentPerson)
            