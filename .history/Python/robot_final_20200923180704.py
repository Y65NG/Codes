#引用一些依赖库，分别是绘图、矩阵、数学
import matplotlib.pyplot as plt
import numpy as np
import math

#这个函数用于给定中心x,y坐标和机器人方向a，画出机器人轮廓（这个函数在L9课上不会仔细讲解）
def draw_robot(x_pos,y_pos,angle):
    #机器人轮廓定义矩阵
    robot_init = [[0.5, 0.5, -0.5, -0.5, 0.5],[0.5,-0.5,-0.5,0.5,0.5]]
    #TODO 根据angle计算旋转矩阵
    rotate_matrix = [[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]]
    #TODO 根据x_pos,y_pos计算平移矩阵
    pan_matrix = [[x_pos]*5,[y_pos]*5]
    #根据旋转矩阵与平移矩阵计算所有轮廓点的新坐标
    robot = np.dot(rotate_matrix,robot_init) + pan_matrix
    #画出机器人与前端标识
    plt.plot(robot[0],robot[1],'r')
    # plt.plot((robot[0,0]+robot[0,1])/2, (robot[1,0]+robot[1,1])/2,'r-o')

def robotWheel(vx, vy, w):
    v0 = vx - vy - w # 机器人的长和宽都是1
    v1 = vx + vy + w
    v2 = vx - vy + w 
    v3 = vx + vy - w 
    return [v0, v1, v2, v3]
#给定速度v，角速度w，移动时间t，移动机器人。输入必须都是数字。
def move_robot(vx,vy,w,time):
    #时间系数
    interval = 0.01
    #运行指定的时间
    for i in range(int(time)):
        #将最新的位置与角度添加到x,y,a数组中(这里的x,y,a都是全局变量)
        x.append(x[-1] + vx * math.cos(a[-1]) * interval - vy * math.sin(a[-1]) * interval)
        y.append(y[-1] + vx * math.sin(a[-1]) * interval + vy * math.cos(a[-1]) * interval)
        a.append(a[-1] + w * interval)

        #图形操作
        plt.clf()   #清空上一帧图形
        plt.plot(x, y, 'b') #画出从0时刻到当前的轨迹
        plt.axis("equal")   #设置x,y坐标轴等比例
        # plt.xlim((-8, 8))   #设置x坐标轴范围
        # plt.ylim((-4, 14))  #设置y坐标轴范围
        draw_robot(x[-1],y[-1],a[-1])  #调用函数画出机器人当前轮廓
        plt.title('vx='+str(vx)+'vy=' + str(vy)+';w='+str(w)+';t='+str(i+1),color='blue') #将速度、方向、时间信息显示在标题栏
        plt.pause(0.01)     #停顿0.01秒

if __name__ == '__main__':
    #初始化全局变量x,y位置及a(angle)方向
    x = [0]
    y = [0]
    a = [0]

    # 根据不同的v,w,time绘制不同图形，想要体验一下改动小车移动方式的同学改下面的代码就好————L9课程
    # move_robot中()是指三个变量，第一个变量速度vx，第二个角速度w，第三个运行时间time. 半径R = v/w
    # vx, vy, w, t
    
    for i in range(1, 9): move_robot(0, 5 * math.pi * i, -5 * math.pi, 10)
    r = 8
    # move_robot(0, 0, 31.416, 20)
    while r < 50:
        move_robot(0, r / 0.01, 0, 1)
        move_robot(r / 0.01, 0, 0, 2)
        move_robot(0, -r / 0.01, 0, 2)
        move_robot(-r / 0.01, 0, 0, 2)
        move_robot(0, r / 0.01, 0, 2)
        move_robot(0, 0, -25 * math.pi, 1)
        r += (2 * r**2) ** 0.5 - r
    r += 2
    while True:
        move_robot(0, 5 * math.pi * r, -5 * math.pi, 10)
        r += r
    # for i in range(1, 9): move_robot(0, )
    # move_robot(0, 15.708, -15.708, 10)
    plt.show()  #保留最后一帧图像