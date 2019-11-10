import BT
from time import sleep


def main():
    bt = BT.bluetooth()
    # print(serial.tools.list_ports.comports())
    bt.do_connect('COM2')

    _quit = False

    while _quit is False:
        cmd = input("input: ")
        if cmd == 'Node':
            _quit = True
        bt.SerialWrite(cmd)
        sleep(0.05)
        print(bt.SerialReadString())
        #prevent stupid(me)
        #sleep(1)
    print(bt.ser.isOpen())
    bt.disconnect()


if __name__ == '__main__':
    main()
