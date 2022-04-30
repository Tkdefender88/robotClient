import socket

class appViewModel():
    port = 6666

    def __init__(self):
        self.angle = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.socket.bind(("", appViewModel.port))

    def getAngle(self):
        return self.angle
    
    def setAngle(self, angle):
        if angle >= 0 and angle <= 360:
            self.angle = angle

    def sendAngleStart(self):
        addressPort = ('192.168.1.189', appViewModel.port)
        msg = str.encode(str(self.angle))
        self.socket.sendto(msg, addressPort)