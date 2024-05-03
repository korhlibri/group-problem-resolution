import random as rand

def restrictionsGroups():
    restrictions = {}

    heavyRestrictions = ["scheduleCollisionProf",
                         "scheduleCollisionStu",
                         "breakTime",
                         "noMoreTwoAndPairs",
                         "availableProf",
                         "definedSchedulesUFsAndProf",
                         "minMaxProfTotal",
                         "catProfModuleRel",
                         "oddHours"]
    
    lightRestrictions = ["noWednesday",
                         "plantProfModuleRel",
                         "minCatProf",
                         "continousSchedule",
                         "onlyEight",
                         "notAfterSeven"]
    
    for i in range(len(heavyRestrictions)):
        randomNum = rand.randint(100, 108)
        restrictions[heavyRestrictions[i]] = randomNum

    for i in range(len(lightRestrictions)):
        randomNum = rand.randint(10, 15)
        restrictions[lightRestrictions[i]] = randomNum

  

    return restrictions
        

restrictionsGroups()