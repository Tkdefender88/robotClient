import socket

ZERO_SPEED = 10

class appViewModel():
    port = 6666

    def __init__(self):
        self.angle = 0
        self.speed = 0 
        self.pMult = 0
        self.pDiv  = 0
        self.iMult = 0
        self.iDiv  = 0
        self.dMult = 0
        self.dDiv  = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addressPort = ('192.168.0.105', appViewModel.port)

    def setIMult(self, value):
        self.iMult = value

    def setIDiv(self, value):
        self.iDiv= value

    def setPMult(self, value):
        self.pMult = value

    def setPDiv(self, value):
        self.pDiv= value

    def setDMult(self, value):
        self.dMult = value

    def setDDiv(self, value):
        self.dDiv= value
    
    def getIMult(self):
        return self.iMult

    def getIDiv(self):
        return self.iDiv

    def getPMult(self):
        return self.pMult

    def getPDiv(self):
        return self.pDiv

    def getDMult(self):
        return self.dMult

    def getDDiv(self):
        return self.dDiv

    def getAngle(self):
        return self.angle
    
    def setAngle(self, angle):
        if angle >= 0 and angle <= 360:
            self.angle = angle

    def setSpeed(self, speed):
        if speed >= 0 and speed <= 100:
            self.speed = speed
    
    def getSpeed(self):
        return self.speed
        
    def zeroArm(self):
        msg = "{command} {angle} {speed}"
        msg = msg.format(command=46, angle=0, speed=ZERO_SPEED)
        msg = str.encode(msg)
        self.socket.sendto(msg, self.addressPort)

    def sendAngleStart(self):
        msg = "{command} {angle} {speed}"
        msg = msg.format(command=165, angle=(round(self.angle // 0.6)), speed=self.speed)
        msg = str.encode(msg)
        self.socket.sendto(msg, self.addressPort)

    def setPID(self):
        msg = "{command} {pm} {pd} {im} {id} {dm} {dd}"
        msg = msg.format(
            command=5,
            pm=self.pMult,
            pd=self.pDiv,
            im=self.iMult,
            id=self.iDiv,
            dm=self.dMult,
            dd=self.dDiv
        )
        print(msg)
        msg = str.encode(msg)
        self.socket.sendto(msg, self.addressPort)