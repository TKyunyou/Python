#HelloWorld的条件输出
#判断是否相等用两个等号,即==
#\n表示回行
x=eval(input())
if x==0:
    print("HelloWorld")
elif x>0:
    print("He\nll\no \nWo\nrl\nd")
else:
    for c in "Hello World":
        print(c)
