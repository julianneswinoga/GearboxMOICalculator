# Written by Cameron Swinoga

class gear:
    def __init__(self, teeth, inertia, s_inertia):
        self.teeth = teeth
        self.MOI = inertia
        self.ShaftMOI = s_inertia
    def inertia(self):
        return self.MOI + self.ShaftMOI

def calculateInertiaofGears(gearsArr):
    if (len(gearsArr) <= 2):
        return gearsArr[0].inertia()+gearsArr[1].inertia()
    else:
        return gearsArr[0].inertia()+gearsArr[1].inertia()+(pow(gearsArr[1].teeth/gearsArr[2].teeth, 2)*(calculateInertiaofGears(gearsArr[2:])))

print "All input must be in kg*m^2"
gearNum = int(raw_input("Number of gears: "))
loadI = float(raw_input("Inertia of load: "))
motI = float(raw_input("Inertia of motor: "))

shaftNum = 1
gears = []
tempG = gear(0, motI, 0.0)
gears.append(tempG)

for i in range(gearNum):
    T = float(raw_input("Teeth of gear " + str(i+1) + ": "))
    I = float(raw_input("Inertia of gear " + str(i+1) + ": "))
    if (i % 2 == 0 or i == gearNum-1):
        SI = float(raw_input("Inertia of shaft " + str(shaftNum) + ": "))
        shaftNum += 1
    else:
        SI = 0.0
    tempG = gear(T, I, SI)
    gears.append(tempG)
tempG = gear(0, loadI, 0.0)
gears.append(tempG)

totalI = calculateInertiaofGears(gears)
print "Inertia of gear system: " + str(totalI) + "kg*m^2"
    
