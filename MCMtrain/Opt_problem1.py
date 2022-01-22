#参考 https://blog.csdn.net/weixin_42644765/article/details/105125414

# https://developers.google.com/optimization/mip
from statistics import mean

from ortools.linear_solver import pywraplp



class MyDrone:
    def __init__(self,len,width,Height,Speed,FlightTime,ViedoCap=1):
        self.len= len
        self.width = width
        self.height = Height
        self.speed = Speed
        self.flightTime=FlightTime
        self.vediocap=ViedoCap

    def getV(self):
        return self.len*self.height*self.width

    def getSquare(self):
        return self.speed*self.flightTime




def main():
    # Create the mip solver with the SCIP backend.
    #'SCIP':solve Contraint Interger Programs
    #'LP' Linear Program
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # 无穷
    infinity = solver.infinity()


    ## 定义优化变量 无人机7架，药品3种
    # x and y are integer non-negative variables. (interger:整数），如果要连续，换成NumVar
    DroneNum=globals()
    MedicineNum = globals()
    for i in range(7):
        DroneNum[i] = solver.IntVar(0.0, infinity, 'd%s'%i)
    for i in range(3):
        MedicineNum[i] = solver.IntVar(0.0, infinity, 'm%s' % i)

    #初始化无人机的参数
    Drone={}
    Drone[0]=MyDrone(45,45,25,40,35)
    Drone[1] = MyDrone(30,30,22,79,40)
    Drone[2] = MyDrone(60,50,30,64,35)
    Drone[3] = MyDrone(25,20,25,60,18)
    Drone[4] = MyDrone(25,20,27,60,15)
    Drone[5] = MyDrone(40,40,25,79,24,0)
    Drone[6] = MyDrone(32,32,17,64,16)
    # 初始化药品的参数
    Medicine=[]
    Medicine.append(14*7*5)
    Medicine.append(5*8*5)
    Medicine.append(12*7*4)


    ## 定义目标函数 F=f1+f2

    #f1
    f1 = 0
    ##每一个Drone 的是否可以搭载视频设备 (开头的0无用）
    VideoCapable = [1,1,1,1,1,0,1]

    ##每一个Drone的检测范围 （开头的0无用）
    for x in range(len(Drone)):
        ScanSquare= [6088755,13438395,9612555,4729575,3974475,8152695,4477875]
    for i in range(7):
        f1 += DroneNum[i]*VideoCapable[i]*ScanSquare[i]

    #f1归一化
    V=[]
    for drone in Drone.values():
        V.append(drone.getV())
    average_v= mean(V)
    Container1_v = (20*12)*(8*12)*(8*12)+6
    average_S =mean(ScanSquare)

    f1 *= average_S*average_v/(Container1_v)

    #f2: 药品数量接近正态分布
    f2 = 0
    ##每一种药品的需求量
    need= [6,2,4]

    sigma= [i*20 for i in need]
    mu =[i*180 for i in need ]

    for i in range(3):
        x= (MedicineNum[i]-mu[i])/(2*sigma[i]*sigma[i])
        f2*= exp(x)

    #总参数
    F = 0.5*f1+0.5*f2



    # 约束条件
    #1. 整数 已经约束在Int

    #2. 装箱体积约束
    solver.add(DroneNum[1]*Drone[1].getV()<=Container1_v)


    #
    #

    #
    # # x + 7 * y <= 17.5.
    # solver.Add(x + 7 * y <= 17.5)
    #
    # # x <= 3.5.
    # solver.Add(x <= 3.5)
    #
    # print('Number of constraints =', solver.NumConstraints())
    #
    # # Maximize x + 10 * y.
    solver.Maximize(F)
    #
    status = solver.Solve()
    #
    # if status == pywraplp.Solver.OPTIMAL:
    #     print('Solution:')
    #     print('Objective value =', solver.Objective().Value())
    #     print('x =', x.solution_value())
    #     print('y =', y.solution_value())
    # else:
    #     print('The problem does not have an optimal solution.')
    #
    # print('\nAdvanced usage:')
    # print('Problem solved in %f milliseconds' % solver.wall_time())
    # print('Problem solved in %d iterations' % solver.iterations())
    # print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    #

if __name__ == '__main__':
    main()
