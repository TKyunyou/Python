#数字形式转换(2019.7.24)
#for in结构解释:使m遍历x中的元素,每次执行一次下面的语句
#如,输入49,即x=49,第一次循环m为4,执行结果为打印四,第二次循环m为9,执行结果为打印九
#print()中增加end=""参数表示输出后不增加换行，多个print()可以连续输出
template="零一二三四五六七八九"
x=input()
for m in x:
    print(template[eval(m)],end="")
