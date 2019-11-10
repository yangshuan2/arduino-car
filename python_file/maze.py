import node
import numpy as np
import csv
import pandas
from enum import IntEnum


class Action(IntEnum):
    ADVANCE     = 1
    U_TURN      = 2
    TURN_RIGHT  = 3
    TURN_LEFT   = 4
    HALT        = 5


class Maze:
    def __init__(self, filepath):
        self.raw_data = pandas.read_csv(filepath).values
        # print(self.raw_data)
        self.nodes = []
        #ddList is a list of deadends
        self.nd_dict = dict(zip([1, 2, 3, 4, 5, 6, 7, 8, 9], self.raw_data[0]))
        # key: index, value: the correspond node
        print(self.nd_dict)
        self.explored = set()
        self.ndList = []
        for dt in self.raw_data:
            # TODO: Update the nodes with the information from raw_data
            self.nodes.append(node.Node(dt[0]))
            print(dt)

        for i in range(len(self.nodes)):
            for j in range(1, 5):
                # TODO: Update the successors for each node
                if np.isnan(self.raw_data[i][j + 4]):
                    self.nodes[i].setSuccessor(self.raw_data[i][j], j)
                else:
                    self.nodes[i].setSuccessor(self.raw_data[i][j], j,
                                               self.raw_data[i][j + 4])
                # print(self.raw_data[i][j - 1])
            print('node%d index:%f, successor: %s' %
                  (i + 1, self.nodes[i].getIndex(),
                   self.nodes[i].getSuccessors()))
        self.dd_List = self.deadends()
        print (self.dd_List)

    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def BFS(self, nd):
        """ return a sequence of nodes from the node to the nearest unexplored deadend"""
        nodevalue = []
        nodefrom = []
        for i in range(len(self.nodes)):
            if (i == nd-1):
                nodevalue.append(0)
                # 0 means the origin 
            nodevalue.append(-1)
            # -1 meas value is infinity 
        for i in range(len(self.nodes)):
            if(i == (int)(nd-1)):
                nodefrom.append(-4)
            nodefrom.append(-3)
            # -3 means have not been walked
        value = self.walkonestep(nd-1,nodevalue,nodefrom)
        sum = 0
        for i in range(len(self.dd_List)):
            sum = sum + self.dd_List[i]
        if(sum == 0):
            #print(self.ndList)
            return self.ndList

        ndList_copy = self.BFS(value)
        return ndList_copy


    def walkonestep(self,nd,nodevalue,nodefrom):
        nodelist = []
        
        intnode = (int)(nd)
        for i in range(len(self.dd_List)):
            if((int)(self.dd_List[i]) == (int)(nd+1)):
                self.dd_List[i] = 0
                nodelist.append(nd+1)
                while(1):
                    #print("nodefrom")
                    #print(nodefrom[intnode]+1)
                    if(nodefrom[intnode] == -4):
                        break
                    nodelist.append(nodefrom[(int)(intnode)]+1)
                    intnode = nodefrom[(int)(intnode)]
                    #print(intnode+1)
                nodelist.reverse()
                #print(nodelist)
                for j in range(len(nodelist)):
                    self.ndList.append(nodelist[j])
                return (nd+1)
        for i in range(1,5):
            k = (int)(self.nodes[(int)(nd)].getSuccessor(i))
            if(k != 0):
                m = self.nodes[(int)(nd)].getLength(self.nodes[(int)(k)-1])
                if(nodevalue[k-1] == -1):
                    nodevalue[k-1] = nodevalue[(int)(nd)]+m
                    nodefrom[k-1] = intnode
                if(nodevalue[k-1] >0):
                    if (nodevalue[k-1] > nodevalue[(int)(nd)]+m):
                        nodevalue[k-1] = nodevalue[(int)(nd)]+m
                        nodefrom[k-1] = intnode
                    #nd is the index -1.
        nodevalue[(int)(intnode)] = -2
        #-2 means the node has been the center to walk
        mini = 0
        mini_node = 0
        for j in range(len(self.nodes)):
            if(nodevalue[j]>0):
                if(mini == 0):
                    mini = nodevalue[j]
                    mini_node = j
                else:
                    if(mini > nodevalue[j]):
                        mini = nodevalue[j]
                        mini_node = j
        #print(mini_node+1)
        #print("hey")
        return self.walkonestep(mini_node,nodevalue,nodefrom)

    def BFS_2(self, nd_from,nd_to):
        """ return a sequence of nodes from the node to the nearest unexplored deadend"""
        self.ndList.clear()
        nodevalue = []
        nodefrom = []
        for i in range(len(self.nodes)):
            if (i == nd_from-1):
                nodevalue.append(0)
                # 0 means the origin 
            nodevalue.append(-1)
            # -1 meas value is infinity 
        for i in range(len(self.nodes)):
            if(i == (int)(nd_from-1)):
                nodefrom.append(-4)
            nodefrom.append(-3)
            # -3 means have not been walked
        value = self.walkonestep_2(nd_from-1,nd_to,nodevalue,nodefrom)
        print(self.ndList)
        return self.ndList
    
    def walkonestep_2(self,nd,nd_to,nodevalue,nodefrom):

        nodelist = []        
        intnode = (int)(nd)
        if((int)(nd+1)==(int)(nd_to)):
            nodelist.append(nd+1)
            while(1):
                #print("nodefrom")
                #print(nodefrom[intnode]+1)
                if(nodefrom[intnode] == -4):
                    break
                nodelist.append(nodefrom[(int)(intnode)]+1)
                intnode = nodefrom[(int)(intnode)]
                #print(intnode+1)
            nodelist.reverse()
            #print(nodelist)
            for j in range(len(nodelist)):
                self.ndList.append(nodelist[j])
            return (nd+1)
        for i in range(1,5):
            k = (int)(self.nodes[(int)(nd)].getSuccessor(i))
            if(k != 0):
                m = self.nodes[(int)(nd)].getLength(self.nodes[(int)(k)-1])
                if(nodevalue[k-1] == -1):
                    nodevalue[k-1] = nodevalue[(int)(nd)]+m
                    nodefrom[k-1] = intnode
                if(nodevalue[k-1] >0):
                    if (nodevalue[k-1] > nodevalue[(int)(nd)]+m):
                        nodevalue[k-1] = nodevalue[(int)(nd)]+m
                        nodefrom[k-1] = intnode
                    #nd is the index -1.
        nodevalue[(int)(intnode)] = -2
        #-2 means the node has been the center to walk
        mini = 0
        mini_node = 0
        for j in range(len(self.nodes)):
            if(nodevalue[j]>0):
                if(mini == 0):
                    mini = nodevalue[j]
                    mini_node = j
                else:
                    if(mini > nodevalue[j]):
                        mini = nodevalue[j]
                        mini_node = j
        #print(mini_node+1)
        #print("hey")
        return self.walkonestep_2(mini_node,nd_to,nodevalue,nodefrom)

    def getAction(self, car_dir, nd_from, nd_to):
        """ return an action and the next direction of the car """
        if nd_from.isSuccessor(nd_to):
            nd_dir = nd_from.getDirection(nd_to)
            #TODO: Return the action based on the current car direction and the direction to next node
            print("Error: Failed to get the action")
            return 0
        else:
            print("Error: Node(",nd_to.getIndex(),") is not the Successor of Node(",nd_from.getIndex(),")")
            return 0

    def strategy(self, nd):
        return self.BFS(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)

    def test(self, nd, dire, nd_succ):
        print("Successor in", node.Direction(dire),
              ":", self.nodes[nd - 1].getSuccessor(dire))
        print("Direction of", nd_succ, ":",
              node.Direction(self.nodes[nd - 1].
                             getDirection(self.nodes[nd_succ - 1])))
    def deadends(self):
        ddList = []
        for i in range(len(self.nodes)):
            if(self.nodes[i].isEnd()):
                ddList.append(i+1)
        return ddList
    def dircheck(self,dir_last,dir_next):
        if(dir_last == dir_next):
            return 'U'
        elif(dir_next == 0):
            return 'S'
        elif(dir_last == 0):
            return 'D'
            #S:stop
            #D:迴轉
        elif(dir_last == 1 and dir_next == 3):
            return 'L'
        elif(dir_last == 1 and dir_next == 4):
            return 'R'
        elif(dir_last == 2 and dir_next == 3):
            return 'R'
        elif(dir_last == 2 and dir_next == 4):
            return 'L'
        elif(dir_last == 3 and dir_next == 2):
            return 'L'
        elif(dir_last == 3 and dir_next == 1):
            return 'R'
        elif(dir_last == 4 and dir_next == 1):
            return 'L'
        elif(dir_last == 4 and dir_next == 2):
            return 'R'

    def getdir(self,nd_last,nd_now,nd_next):
        if(nd_last != nd_now):
            dir_last = self.nodes[(int)(nd_last)-1].getDirection(self.nodes[(int)(nd_now)-1])
        else:
            dir_last = 0
        if(nd_now != nd_next):
            dir_next = self.nodes[(int)(nd_now)-1].getDirection(self.nodes[(int)(nd_next)-1])
        else:
            dir_next = 0
        return 10*dir_last+dir_next