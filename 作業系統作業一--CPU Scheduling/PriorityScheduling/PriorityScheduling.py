from pprint import pprint
import json

with open("test3.json",'r') as load_file:
    
    load_dict = json.load(load_file)
    #pprint(load_dict)

a=[]    #存第二個key
b=[]    #存value
c=[]    #存第一個key

if isinstance(load_dict,dict):  #instance(object,classinfo): 判斷是否為字典類型，返回 T or F   
    for i in load_dict.keys():
        c.append(i)
        if isinstance(load_dict[i],dict):
            for j in load_dict[i].keys():
                a.append(j)
                b.append(load_dict[i][j])
    
step = 4
d = [b[i:i+step] for i in range(0,len(b),step)]  #每四個數一組 (Process, Arrive Time, Burst Time,Priority)



sum1 = 0
for i in range(len(d)):  # process 總數目
    sum1 +=1


PR = [0] * (sum1 + 1)
BT = [0] * (sum1 + 1)
AT = [0] * (sum1 + 1)
ALL = [0] * (sum1 + 1)
for i in range(sum1):
    PR[i] = d[i][3]    # 放入Priority
    BT[i] = d[i][2]    # 放入Burst Time
    AT[i] = d[i][1]     # 放入Arrive Time
    ALL[i] = [i, AT[i], BT[i], PR[i]]   # 放入Process, Arrive Time, Burst Time , Priority

ALL.pop(-1)

i = 0
total = []   #存放所有的Processes
for i in range(0, sum(BT)):
        l = [j for j in ALL  if j[1] <= i]   #find Arrive Time
        #print(l)
        l.sort(key=lambda x: x[3])  # 對Priority做排序, key=lambda 元素: 元素[字段索引] ,x 可以是任意字母
        #print(l)
        
        ALL[ALL.index(l[0])][2] -= 1   # Burst Time 減一
        total.append(l[0][0]+1)
        for s in ALL:
            if s[2] == 0:   # Burst Time 歸0
                    t = ALL.pop(ALL.index(s))   # 把做完的丟掉
                    #print(t)
                    

for i in range(len(total)):   # Output
    print("second %d~%d process p%s"%(i,i+1,total[i]))
    
    try:    #出現異常情況就跳到except執行
        if total[i] != total[i+1]:
            print('====================')
    except:
        break

    

