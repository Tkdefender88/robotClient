import socket

class appViewModel():
    port = 6666

    def __init__(self):
        self.angle = 0
        self.speed = 100
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addressPort = ('192.168.0.106', appViewModel.port)

    def getAngle(self):
        return self.angle
    
    def setAngle(self, angle):
        if angle >= 0 and angle <= 360:
            self.angle = angle
        
    def zeroArm(self):
        msg = "{command} {angle} {speed}"
        msg = msg.format(command=46, angle=0, speed=50)
        msg = str.encode(msg)
        self.socket.sendto(msg, self.addressPort)

    def sendAngleStart(self):
        msg = "{command} {angle} {speed}"
        msg = msg.format(command=165, angle=self.angle, speed=self.speed)
        msg = str.encode(msg)
        print(msg)
        self.socket.sendto(msg, self.addressPort)