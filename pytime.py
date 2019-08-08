#time库中以易懂方式显示系统时间的函数:ctime()
import time as t
x=t.ctime()
print(x)
#perf_counter()函数给出当前CPU级别的精确时间值,两次调用算差值可用来计时
start=t.perf_counter()
#sleep()函数能让程序休眠指定时间
t.sleep(1)
end=t.perf_counter()
dur=end-start
print('{:.5f}s'.format(dur))
