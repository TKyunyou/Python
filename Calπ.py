#蒙特卡罗方法计算π值,即利用圆和正方形的面积关系
import random as r
import time as t
hits=0
n=eval(input('请输入想要抛撒的点的数量:'))
start=t.perf_counter()
for i in range(1,n+1):
    x=r.random()
    y=r.random()
    if x**2+y**2<=1:
        hits+=1
    π=4*hits/n
end=t.perf_counter()
dur=end-start
print('在模拟抛撒{}次的试验中,圆周率的计算值为{:.10f},程序运行时间为{:.2f}s'\
      .format(n,π,dur))

