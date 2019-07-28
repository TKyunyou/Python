#温度转换（这是我学习Python的开始:2019.7.5)
#{}表示填充框,{:.2f}.format(变量)表示变量按保留小数点后两位的格式
TempStr=input('请输入带单位的温度值:')
if TempStr[-1] in ['c','C']:
    F=1.8*eval(TempStr[0:-1])+32
    print('转换后的温度值为:{:.2f}F'.format(F))
elif TempStr[-1] in ['f','F']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print('转换后的温度值为:{:.2f}C'.format(C))
else:
    print('输入格式错误')
