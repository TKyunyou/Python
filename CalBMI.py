#CalBMI.py
weight,height=eval(input('请输入体重(千克)入和身高(米)并以逗号隔开(不需单位):'))
BMI=weight/height**2
print('您的BMI指数为{:.2f}'.format(BMI))
WHO,dom = '',''
if 18.5<=BMI<24:
    WHO ,dom = '正常','正常'
elif 24<=BMI<25:
    WHO,dom= '正常', '偏胖'
elif 25<=BMI<28:
    WHO,dom='偏胖','偏胖'
elif 28<=BMI<30:
    WHO,dom='偏胖','肥胖'
elif BMI>=30:
    WHO,dom='肥胖','肥胖'
else:
    WHO,dom='偏瘦','偏瘦'
print('您的身体类型为:国际:{},国内:{}'.format(WHO,dom))
