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
        self.addressPort = ('192.168.0.106', appViewModel.port)

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
        msg = msg.format(command=165, angle=self.angle, speed=self.speed)
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
        self.socket.sendto(msg, self.addressPort)