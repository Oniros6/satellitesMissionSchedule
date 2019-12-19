#satStateTable被定义为全局变量方便各个部分调用
#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from interval import Interval
import copy
#satStateTable [label storage timeWindow nextTask]

# def initsatState():
#
#     global satStateTable
#
#     satStateTable = pd.DataFrame(
#         np.zeros((1, 3)),
#         columns=['Storage','TaskNumber','label'])
#
#     satStateTable.loc[0, 'Storage'] = 5
#     satStateTable.loc[0, 'TaskNumber'] = 1
#     satStateTable.loc[0, 'label'] = 0 #状态label从零开始编号，代表不同的状态
#     # 最后的label确保了状态不会重叠编成一样的。

def initTasklist():
    # global satStateTable
    # global  Task
    # global RemainingTimeTotal
    global taskList
    # satStateTable = pd.DataFrame(
    #     np.zeros((1, 3)),
    #     columns=['Storage','TaskNumber','label'])
    # taskList=[1,2,3,4,5,0]
    # taskList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    #             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 0]
    taskList=[3,7,2,16,1,8,6,9,15,4,10,17,5,11,18,0]
    # Task[startTime, endTime, engergyCost, reward, angle]


def initTask():

    global Task





    Task = {'3': [65, 65, 1, 100, -7.45724275766466],
            '7': [68, 68, 1, 40, -7.89969417530144],
            '2': [69, 69, 1, 100, 13.6399007451127],
            '16': [118, 118, 1, 10, -10.3682107759176],
            '1': [124, 124, 1, 100, 11.6271525374774],
            '8': [150, 150, 1, 40, -1.84496651971562],
            '6': [218, 218, 1, 100, -4.59939101003146],
            '9': [258, 258, 1, 40, -10.9580854925028],
            '15': [272, 272, 1, 10, -2.47942644716451],
            '4': [300, 300, 1, 100, 12.1725862458616],
            '10': [392, 392, 1, 40, 7.43455315035822],
            '17': [406, 406, 1, 10, 2.10370861521673],
            '5': [446, 446, 1, 100, 1.90096462779665],
            '11': [446, 446, 1, 40, 3.09407087944975],
            '18': [473, 473, 1, 10, -6.84203655806705]
            }







    # Task = {'1': [43305.3561578704, 43305.3571734722, 1, 2,7],
    #         '2': [43305.3563003472, 43305.3571645717, 1, 2,-2],
    #         '3': [43305.356455, 43305.3571811574, 1, 2,3],
    #         '4': [43305.3566809838, 43305.3574698727, 1, 2,4],
    #         '5': [43305.3570707755, 43305.3580831713, 1, 2,8],
    #         '6': [43305.3574095023, 43305.3584093981, 1, 2,-12],
    #         '7': [43305.3577584606, 43305.3587445718, 1, 2,4],
    #         '8': [43305.357945787, 43305.3584505324, 1, 2,9],
    #         '9': [43305.360321886605, 43305.361314710695, 1,2,1],
    #         '10': [43305.3743262153, 43305.3753106481, 1, 2,5],
    #         '11': [43305.374400659704, 43305.3753651389, 1,2,-3],
    #         '12': [43305.375476412, 43305.3764784259, 1, 2,-10],
    #         '13': [43305.3756235185, 43305.3765711227, 1, 2,1],
    #         '14': [43305.3761551273, 43305.3770963194, 1, 2,7],
    #         '15': [43305.4220622685, 43305.422864027794, 1, 2,0],
    #         '16': [43305.4230962616, 43305.4240546296, 1, 2,12],
    #         '17': [43305.4233630671, 43305.4241646296, 1, 2,-5],
    #         '18': [43305.4235491667, 43305.423813541696, 1, 2,8],
    #         '19': [43305.4242881019, 43305.4252466667, 1, 2,5],
    #         '20': [43305.42438875, 43305.4253734491, 1, 2,-14],
    #         '21': [43305.4243952778, 43305.4251186111, 1, 2,3],
    #         '22': [43305.4287461227, 43305.4295118056, 1, 2,2],
    #         '23': [43305.4292404745, 43305.4302022338, 1, 2,0],
    #         '24': [43305.4400880093, 43305.4410830903, 1, 2,5],
    #         '25': [43305.4404341898, 43305.4409515046, 1, 2,-4],
    #         '26': [43305.4679798958, 43305.4688193171, 1, 2,-3],
    #         '27': [43305.4689053241, 43305.4697312037, 1, 2,-2],
    #         '28': [43305.4898499537, 43305.4908466204, 1, 2,-5],
    #         '29': [43305.4899502083, 43305.4904528472, 1, 2,-9],
    #         '30': [43305.491817905095, 43305.4927570602, 1, 2,-4],
    #         '31': [43305.4925221759, 43305.4933020486, 1, 2,-8],
    #         '32': [43305.4925519444, 43305.4933894676, 1, 2,0]}


# def initRemainingTimeTotal():
#
#     global RemainingTimeTotal
#     global Task
#
#     RemainingTimeTotal = [[Interval(Task['1'][0], Task['5'][1], closed=True)]]


# def updateRemainTimeTotal(RemainingTime):
#
#     global RemainingTimeTotal
#
#     RemainingTimeTotal.append(RemainingTime)





# def set_value(name, value):
#
#     _global_dict[name] = value


# def addNewState(storage,nextTask,label):
#     global satStateTable
#     global Task
#
#
#
#     # Tasklist_Initial = [1, 2, 3, 4, 5, 0]
#
#
#     new = pd.DataFrame({'Storage':storage ,
#                         'TaskNumber':nextTask ,
#                         'label': label},
#                        index=[0])#设置行初始index
#
#     satStateTable = satStateTable.append(new, ignore_index=True)

def get_value_taskList():

    global taskList

    return taskList.copy()


def get_value_Task(number):

    #number为str类型数值
    global Task

    return Task[number].copy()

def get_value_TaskTotal():
    global Task

    return copy.deepcopy(Task)




# def get_value_RemainingTime(label):
#
#     global RemainingTimeTotal
#
#     RemainingTime=RemainingTimeTotal[label].copy()
#     # storage=satStateTable.loc[label, 'storage']
#     # nextTask=satStateTable.loc[label, 'nextTask']
#
#
#     return RemainingTime


# def get_value_RemainingTimeTotal():
#
#     global RemainingTimeTotal
#
#
#     # storage=satStateTable.loc[label, 'storage']
#     # nextTask=satStateTable.loc[label, 'nextTask']
#
#
#     return copy.deepcopy(RemainingTimeTotal)
#     #为了防止把地址传出去误改了，确保所有改变值的操作都在本文件的变量空间中进行





#
# def get_value_satState():
#
#     global satStateTable
#
#     return satStateTable






def taskListMove(number):

    global taskList

    taskList.remove(number)

def taskListPop():

    global taskList

    taskList.pop(0)




