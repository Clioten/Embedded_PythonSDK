from clioten import IDevice, Device
from time import sleep

class LiveDevice (IDevice):
    def oncomm(self,data,objId):
        print("received: "+data+" "+objId)
        if Device.mode == 1:
            Device.mode = 0
            data =  "Data sent"
            Device.Updateresult(Device.who, "result data" ,data)
            print("result sent: " + data )
            sleep(0.1)

if __name__ == '__main__':
    device = LiveDevice
    deviceId =  "0U7kUy3lCG"
    Device.createDevice(device,"www.clioten.com" , "App Id", "client Key" ,deviceId)
