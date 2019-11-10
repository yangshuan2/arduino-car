from time import sleep
import serial
# these codes are for bluetooth
# hint: please check the function "sleep". how does it work?


class bluetooth:
    def __init__(self):
        self.ser = serial.Serial()

    def do_connect(self, port):
        self.ser.close()
        # TODO: Connect the port with Serial.
        # A clear description for exception may be helpful.
        self.ser.port = port
        self.ser.open()
        return True

    def disconnect(self):
        self.ser.close()

    def SerialWrite(self, output):
        send = output.encode("utf-8")
        self.ser.write(send)

    def SerialReadString(self):
        #TODO: Get the information from Bluetooth. Notice that the return type should be transformed into hex. 
        sleep(0.05)
        waiting = self.ser.in_waiting
        if(waiting != 0):
            rv = [chr(c) for c in self.ser.read(waiting)]
            self.ser.reset_input_buffer()
            return "".join(rv)
        return ""

    def SerialReadByte(self):
        #TODO: Get the UID from bytes. Notice that the return type should be transformed into hex. 
        if self.ser.in_waiting != 0:
            _byte = self.ser.readline()
            #sint_byte = int(_byte)
            return (_byte)
        return 0
