import random
# import matplotlib.pyplot as plt
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

name = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l = int(input('please input citys number(1~15)：'))
names = name[0:l]
# print(names)

# 随机生成0-100的xy坐标，记录到points中去
points = {}
for i in names:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    points[i] = (x, y)
print(points)


import datetime
start = datetime.datetime.now()

# 计算距离（勾股）
def len_point(x,y):
    a = (y[0] - x[0]) ** 2
    b = (y[1] - x[1]) ** 2
    c = a + b
    length = round(c ** 0.5, 2)
    return length

# 走了几次
times = len(points) - 1

points_c = points.copy()
min_p_group = [1]  # 给出一个列表存路径
min_d_group = []  # 储存每次走的距离
first_p = points_c[1]  # 给出第一个点
del points_c[1]  # 删除第一个点


# 循环times次，每一次计算该点与剩下点的距离，找到最小值
# 把该点记录到路径中，再从原列表删除该点
for i in range(0, times):
    key_points = []
    for key in points_c.keys():
        key_points.append(key)  # 计算还要走几个点
    min_p = len_point(first_p, points[key_points[0]])  # 第一步
    p_number = 0  # 重置点位置
    for i in range(0, len(points_c)):
        length = len_point(first_p, points[key_points[i]])
        if length < min_p:
            min_p = length  # 储存最短路径
            p_number = i  # 储存最短路径的位置
    min_p_group.append(key_points[p_number])  # 将最短路径的位置保存i
    min_d_group.append(min_p)
    first_p = points_c[key_points[p_number]]  # 将最短路径位置保存下一个开始
    del points_c[key_points[p_number]]  # 从字典里删除这个点
print('City shortest path: ' + str(min_p_group))  #路径
print('Distance traveled: ' + str(min_d_group))  #距离

avg = 0
for i in range(len(min_d_group)):
    avg = avg + min_d_group[i]
avg = avg/len(min_d_group)
print('Average tour length is: ' + str(avg))

end = datetime.datetime.now()
print ('The time of the run: ' + str(end-start))

points_d = points.copy()
# p_x = []  # 储存x坐标
# p_y = []  # 储存y坐标
# for value in points_d.values():
#     x = value[0]
#     p_x.append(x)
#     y = value[1]
#     p_y.append(y)
#
# plt.subplots(2,2,figsize=(10,5))#规定两张图的尺寸
# plt.subplot(121)  # 第一张图
# for key in points_d.keys():
#     plt.annotate(key, xy=points_d[key])#给每个点标注
# plt.plot(p_x, p_y, 'o')

# plt.subplot(122)  # 第二张图
# plt.title("TPS routes")
# for key in points_d.keys():
#     plt.annotate(key, xy=points_d[key])
# for i in range(0, times):
#     plt.plot([points_d[min_p_group[i]][0], points_d[min_p_group[i + 1]][0]],
#              [points_d[min_p_group[i]][1], points_d[min_p_group[i + 1]][1]], '-o')
# plt.show()

#GUI绘制图形
root =Tk.Tk()
root.title("TPS routes")
# 设置图形尺寸与质量
f = Figure(figsize=(5,5), dpi=100)
# j = Figure(figsize=(10,5), dpi=100)
a = f.add_subplot(111)
# b = j.add_subplot(122)
# for key in points_d.keys():
#     b.annotate(key, xy=points_d[key])#给每个点标注
# b.plot(p_x, p_y, 'o')
for key in points_d.keys():
    a.annotate(key, xy=points_d[key])
for i in range(0, times):
    a.plot([points_d[min_p_group[i]][0], points_d[min_p_group[i + 1]][0]],
           [points_d[min_p_group[i]][1], points_d[min_p_group[i + 1]][1]], '-o')


#把绘制的图形显示到tkinter窗口上
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
Tk.mainloop()




