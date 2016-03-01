class Time:
    pass
def printTime(time):
    print "%d : %1d : %1d" %(time.hours, time.minutes, time.seconds)
def addTime(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    if sum.seconds >= 60:
        sum.seconds = sum.seconds - 60
        sum.minutes = sum.minutes + 1
    if sum.minutes >= 60:
        sum.minutes = sum.minutes - 60
        sum.hours = sum.hours + 1
    return sum
currentTime = Time();
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30
breadTime = Time()
breadTime.hours = 3
breadTime.minutes = 35
breadTime.seconds = 0
doneTime=addTime(currentTime,breadTime)
printTime(doneTime)
