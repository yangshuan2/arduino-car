from node import *
import maze as mz
import score
import student

import numpy as np
import pandas
import time
import sys
import os
import BT
from time import sleep
  
def main():

    nd_list=[]
    dir_List = []
    maze = mz.Maze("test_dis.csv")
    next_nd = maze.getStartPoint()
    car_dir = Direction.SOUTH
    point = score.Scoreboard("UID_405.csv")
    #interface = student.interface()         the part of calling student.py was commented out.

    
    ############################connect#########################################################

    
    
   ############################Game1###############################################
    if(sys.argv[1] == '0'):
        nd_list = maze.BFS(1.0)
        print(nd_list)
        breakcheck_ = 0
        check_read = 1
        while(1):
            for i in range(len(maze.dd_List)):
                if(maze.dd_List[i]!=0):
                    nd_list_tmp = maze.BFS(nd_list[(len(nd_list)-1)])
                    for j in range(len(nd_list_tmp)):
                        nd_list.append(nd_list_tmp[j])
                    break 
                if(i==len(maze.dd_List)-1):
                    breakcheck_=1
            if(breakcheck_): 
                break

        dir_List.append('U')
        for i in range(len(nd_list)-1):
            if(i==0):
                dir_last = 2
                dir_next = maze.nodes[(int)(nd_list[0])-1].getDirection(maze.nodes[(int)(nd_list[1])-1])
            else:
                dir_sum = maze.getdir(nd_list[i-1],nd_list[i],nd_list[i+1])
                dir_last = (int)(((int)(dir_sum)) / 10)
                dir_next = ((int)(dir_sum)) % 10
            direction = maze.dircheck(dir_last,dir_next)
            #if((direction == 'R') or (direction == 'L')):
                #dir_List.append('S')
            if(direction!='S'):
                dir_List.append(direction)
        dir_List.append('D')
        print(dir_List)
    

        bt = BT.bluetooth()
        bt.do_connect('COM3')
        _quit = False
        count = 0
        bt.SerialWrite('U')
        #for i in range (100):
            #bt.SerialWrite('U')
            #sleep(0.05)
        #print('U')
        bt.SerialReadString()

        while _quit is False:
            #readstring = bt.SerialReadString()
            readstring = bt.SerialReadString()
            print(readstring)
            if ('N\n' in readstring):
                print("i read it")
                count = count+1
                if(count<len(dir_List)):
                    cmd = dir_List[count]
                    bt.SerialWrite(cmd)
                    print(cmd)
                    if cmd != 'D':
                        sleep(1.2)
                    else:
                        sleep(0.2)
                else:
                    bt.SerialWrite('S')
                bt.SerialReadString()
            elif(readstring == ''):
                continue
            elif('R\n' in readstring):
                sleep(0.2)
                word = bt.SerialReadString()
                UID = ''
                for i in range(8):
                    UID+=word[i]
                #UID = str(UID)
                print(UID)
                point.add_UID(UID)
             
            if count == len(dir_List):
                _quit = True
        bt.SerialWrite('S')
        print(bt.ser.isOpen())
        bt.disconnect()

            #TODO: Impliment your algorithm here and return the UID for evaluation function
            # ================================================
            # Basically, you will get a list of nodes and corresponding UID strings after the end of algorithm.
			# The function add_UID() would convert the UID string score and add it to the total score.
			# In the sample code, we call this function after getting the returned list. 
            # You may place it to other places, just make sure that all the UID strings you get would be converted.
            # ================================================

        #for i in range(1, len(ndList)):
         #   node = 0
          #  get_UID = "just a test"
           # point.add_UID(get_UID)

############Game2###################################################
    
    elif(sys.argv[1] == '1'):
        next_nd =  1
        now_nd = 1
        count = 0

        while (1):
            #TODO: Implement your algorithm here and return the UID for evaluation function
            now_nd = next_nd
            next_nd = int(input("destination: "))
            count = count+1
            nd_list_tmp = maze.BFS_2(now_nd,next_nd)
            for i in range(len(nd_list_tmp)):
                nd_list.append(nd_list_tmp[i])
            if(count == 5):
                break       
        dir_List.append('U')
        for i in range(len(nd_list)-1):
            if(i==0):
                dir_last = 2
                dir_next = maze.nodes[(int)(nd_list[0])-1].getDirection(maze.nodes[(int)(nd_list[1])-1])
            else:
                dir_sum = maze.getdir(nd_list[i-1],nd_list[i],nd_list[i+1])
                dir_last = (int)(((int)(dir_sum)) / 10)
                dir_next = ((int)(dir_sum)) % 10
            direction = maze.dircheck(dir_last,dir_next)
            #if((direction == 'R') or (direction == 'L')):
                #dir_List.append('S')
            dir_List.append(direction)
        dir_List.append('S')
        print(dir_List)

        bt = BT.bluetooth()
        bt.do_connect('COM1')
        _quit = False
        count = 0
        while _quit is False:
            readstring = bt.SerialReadString()
            if readstring == 'Node encountered.':
                print("i read it")
                count = count+1
                cmd = dir_List[count]
                bt.SerialWrite(cmd)
                if count == len(dir_List):
                    _quit = True
            else:
                print("ya")
                point.add_UID(readstring)

        print(bt.ser.isOpen())
        bt.disconnect()
             



            #for i in range(1, len(ndList)):
             #   get_UID = "just a test"
             #   point.add_UID(get_UID)

    """
    node = 0
    while(not node):
        node = interface.wait_for_node()

    interface.end_process()
    """
    print("complete")
    print("")
    a = point.getCurrentScore()
    print("The total score: ", a)

if __name__=='__main__':
    main()
