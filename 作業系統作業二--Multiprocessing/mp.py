import os
from multiprocessing import Process, Queue
import multiprocessing

#-- 發送者 --
def sender(send,message1,my_pid,my_message,lock):
    lock.acquire()  # 加上鎖    
    pid = os.getpid()
    s = send.get()
    m1 = message1.get()
    print("%s %s send %s" % (pid, s, m1))
    my_pid.put(pid)
    my_message.put(m1)
    lock.release()  # 釋放鎖
    
#-- 接收者 --    
def receiver(receive,my_message,send,s_pid):
    pid = os.getpid()
    r = receive.get()
    m2 = my_message.get()
    s = send.get()
    p = s_pid.get()
    print("%s %s get %s from process %s %s" % (pid, r, m2, p, s))

#------------------------------------------------------------------
if __name__=='__main__':
    result=[]
    a = []    
    b = []    
    c = []    
    send = Queue()        # senders
    receive = Queue()     # receivers
    message1 = Queue()    # messages
    my_message = Queue()
    PID = Queue()         # sender_pid
    manager = multiprocessing.Manager()
    lock = manager.Lock()    # 初始化一個鎖
#----txt 讀檔------   
    with open('testdata.txt','r') as f:
    	for line in f:
    		result.append(list(line.strip('\n').split(',')))
    
      
    for i in range(len(result)):
        send.put(result[i][0])
        message1.put(result[i][2])
        #可以透過 Process 来建立一個 child process        
        ps = Process(target = sender, args = (send,message1,PID,my_message,lock,))
        #啟動 child process
        ps.start()
        # child process 結束後再執行 parent process
        ps.join()
    
    for i in range(len(result)):
        receive.put(result[i][1])
        send.put(result[i][0])
        pr = Process(target = receiver, args = (receive,my_message,send,PID,))
        pr.start()
        pr.join()
       
    print("All processes are done!!")  # 全部執行完畢
