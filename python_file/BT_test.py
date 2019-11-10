import BT
from time import sleep


def main():
    bt = BT.bluetooth()
    # print(serial.tools.list_ports.comports())
    bt.do_connect('COM3')

    _quit = False

    while _quit is False:
        #bt.re_connect('COM3')
        cmd = bt.SerialReadString()
        #print(cmd)
        if cmd == 'R\n':
            sleep(0.2)
            #print('ya')
            word = bt.SerialReadString()
            #if(word != 0):
            UID = []
            for i in range(8):
                UID.append(word[i])
            print(UID)


            #_quit = True
        # cmd = cmd + '\n'
        #bt.SerialWrite(cmd)
        #a=bt.SerialReadString()

        #if(a != 0):
        #print(a)
    print(bt.ser.isOpen())
    bt.disconnect()


if __name__ == '__main__':
    main()
