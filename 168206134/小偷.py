#考试题 
#A：我没有偷钻石。 
#B：D就是罪犯。 
#C：B是盗窃这块钻石的罪犯。 
#D：B有意诬陷我。 
#假定只有一个人说的是真话，编程序判断谁偷走了钻石。


def find(list,man):
    flag = 0   
    for i in range(len(list)):     #遍历所有情况
        sum = (list[i]!="A") + (list[i]=="D") + (list[i]=="B") + (list[i]!="D")
        if ( sum == man ):
            flag = 1
            print("%s is a thief" %list[i])
    if(flag == 0):
        print("Can not find")
 
man = 1    #说真话的人数 
list = ["A", "B", "C", "D"]    #初始嫌疑人 
find(list,man)

