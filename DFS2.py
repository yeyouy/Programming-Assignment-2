# #coding=utf-8
import random
import Tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import math
import mpmath
import datetime
from pandas.core.frame import DataFrame

name = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l = int(input('please input citys number(1~15)：'))
names = name[0:l]
# print(names)

# 随机生成0-100的xy坐标，记录到points中去
points = {}
for i in names:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    points[i] = (x, y)
point=DataFrame(points)
# print(points)

start = datetime.datetime.now()

distance = pd.DataFrame(np.random.randn(l,l))
for i in range(l):
    for j in range(l):
        distance.iloc[i, j] = math.sqrt(
            (point.iloc[0,i] - point.iloc[0,j]) ** 2 + (point.iloc[1,i] - point.iloc[1,j]) ** 2)
# print(distance)

min_d_group = []  # 储存每次走的距离
p = []
for i in range(l):
    p.append(i)
curMinPath = mpmath.inf
d = 0

times = len(points) - 1

path = []
for i in range(0, times):
    def DFS(distance, l, layer):
        global d,curMinPath,path
        # 如果所有城市都遍历完成，则记录最小
        if (layer == l):
            if (distance[p[l - 1]][p[0]] != 0 and (d + distance[p[l - 1]][p[0]] < curMinPath)):
                path = p[:]
                # print('City :' +  str(p))
                min_d_group.append(distance[p[l - 1]][p[0]])
                curMinPath = d + distance[p[l - 1]][p[0]]
        # 否则递归回溯
        else:
            for i in range(layer, l):
                if (distance[p[i - 1]][p[i]] != 0 and d + distance[p[i - 1]][i] < curMinPath):
                    p[i], p[layer] = p[layer], p[i]
                    d = d + distance[p[layer - 1]][p[layer]]
                    DFS(distance, l, layer + 1)
                    d = d - distance[p[layer - 1]][p[layer]]
                    p[i], p[layer] = p[layer], p[i]
    DFS(distance, l, 1)

print('City shortest path:'+ str(path))
print('Distance traveled: ' + str(min_d_group))

d = 0
avg = 0
for i in range(len(min_d_group)):
    d = d + min_d_group[i]
avg = d/len(min_d_group)
print('Average tour length is: ' + str(avg))
print('Distance is: ' + str(d))  #距离
end = datetime.datetime.now()
print ('The time of the run: ' + str(end-start))

points_d = points.copy()

# GUI绘制图形
root =Tk.Tk()
root.title("DFS TPS Routes")
# 设置图形尺寸与质量
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

for key in points_d.keys():
    a.annotate(key, xy=points_d[key])
for i in range(0, times):
    a.plot([points_d[path[i]][0], points_d[path[i + 1]][0]],
           [points_d[path[i]][1], points_d[path[i + 1]][1]], '-o')

#把绘制的图形显示到tkinter窗口上
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
Tk.mainloop()