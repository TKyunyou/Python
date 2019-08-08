import turtle as t
#drawLine()函数封装了绘制一段数码管的功能,以横在中间的数码管起始
def drawLine(draw):
    t.penup()
    t.fd(5)
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.penup()
    t.fd(5)
    t.right(90)
#drawDigit()函数封装了利用drawLine()函数以数码管绘制一个数字(digit)的功能
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
#drawNumbers()封装了将数字串中的数字一个个提取并利用drawDigit()函数绘制的功能
def drawNumbers(num):
    for i in num:
        drawDigit(eval(i))
#main()函数封装了绘制七段数码管的初始功能
#即"导火索",启用main()函数即可开始整个程序
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawNumbers(input('请输入想要转换为七段数码管的数字串:'))
    t.hideturtle()
    t.done()
#启用main()函数,开始整个程序
main()
