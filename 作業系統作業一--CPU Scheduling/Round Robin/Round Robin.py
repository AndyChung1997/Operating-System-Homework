from pprint import pprint
import json

with open("RR.json",'r') as load_file2:
    
    dict_1 = json.load(load_file2)
    #pprint(dict_1)



a=[]    # 存第二個key
b=[]    # 存value
c=[]    # 存第一個key
d=[]    # 存Quantum的value

if isinstance(dict_1,dict):  # instance(object,classinfo): 判斷是否為字典類型，返回 T or F   
    for i in dict_1.keys():
        c.append(i)
        if isinstance(dict_1[i],dict):
            for j in dict_1[i].keys():
                a.append(j)
                b.append(dict_1[i][j])      
        else:
            d.append(dict_1[i])   # Quantum 的值
            

reg2 = []
for i in range(len(b)):
    p = 0
    reg2.append(p)

p = 0
k = 0
total = []
while True:
  
    if b != reg2:
        for i in dict_1["Order"]:  # p3, p1 ,p2
            for j in range(len(a)):   # 0~2
                if a[j] == i:
        
                    if (b[j] // d[1]) == 0 and b[j] > 0:   # 小於Quanum
                      p = b[j]
                      b[j] = 0
                      for i in range(p):
                          total.append(a[j])
                                             
                    elif (b[j] // d[1]) != 0 and b[j] > 0:
                        k2 = 0
                        k += d[1]
                        k2 += d[1]
                        b[j] -= d[1]
                        for i in range(k2):
                            total.append(a[j])                       
    else:
        break
    
for i in range(len(total)):   # Output
    print("second %d~%d process %s"%(i,i+1,total[i]))
    
    try:    #出現異常情況就跳到except執行
        if total[i] != total[i+1]:
            print('====================')
    except:
        break

