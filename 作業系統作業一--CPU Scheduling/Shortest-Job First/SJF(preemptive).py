from pprint import pprint
import json

with open("SJF.json",'r') as load_file3:
    
    load_dict = json.load(load_file3)
    #pprint(load_dict)


a=[]    #存第二個key
b=[]    #存value
c=[]    #存第一個key
d=[]

if isinstance(load_dict,dict):  #instance(object,classinfo): 判斷是否為字典類型，返回 T or F   
    for i in load_dict.keys():
        c.append(i)
        if isinstance(load_dict[i],dict):
            for j in load_dict[i].keys():
                a.append(j)
                b.append(load_dict[i][j])
    
step = 3
d = [b[i:i+step] for i in range(0,len(b),step)]  #每三個數一組 (Process, Arrive Time, Burst Time)


sum1 = 0
for i in range(len(d)):  # process 總數目
    sum1 +=1


BT = [0] * (sum1 + 1)
AT = [0] * (sum1 + 1)
BAP = [0] * (sum1 + 1)
for i in range(sum1):
	BT[i] = d[i][2]    # 放入Burst Time
	
	AT[i] = d[i][1]     # 放入Arrive Time
	
	BAP[i] = [BT[i], AT[i], i]   # 放入Burst Time, Arrive Time, Process

BAP.pop(-1)

i = 0
time = 0
total = []   #存放所有的Processes
l = []
for i in range(0, sum(BT)):
	l = [j for j in BAP  if j[1] <= i]   #find Arrive Time
	#print(l)
	l.sort(key=lambda x: x[0])  # 對Burst Time做排序,   key=lambda 元素: 元素[字段索引] ,x 可以是任意字母
	#print(l)
	#time += 1
	#print("Second:%d~%d, Process : %d"%(time-1,time,l[0][2]+1))    # Process
	
	BAP[BAP.index(l[0])][0] -= 1   # Burst Time 減一
	total.append(l[0][2]+1)
	for s in BAP:
		if s[0] == 0:   # Burst Time 歸零
			t = BAP.pop(BAP.index(s))   # 把做完的丟掉
			#print(t)
			
			

for i in range(len(total)):   # Output
    print("second %d~%d process p%s"%(i,i+1,total[i]))
    
    try:    #出現異常情況就跳到except執行
        if total[i] != total[i+1]:
            print('====================')
    except:
        break
