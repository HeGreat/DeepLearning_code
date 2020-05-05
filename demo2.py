import threading,time

# num=0
# def run(n):
#     global num
#     for i in range(1000000):
#         num=num+n
#         num=num-n

# if __name__ == "__main__":
#     t1=threading.Thread(target=run,args=(6,))  
#     t2=threading.Thread(target=run,args=(9,))    
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('num=',num)


# 加锁，一个线程操作数据的时候，其他线程就不允许操作
lock=threading.Lock()
num=0

def run(n):
    global num
    for i in range(100000):
        #自动上锁，自动解锁
        with lock:
            num=num+n
            num=num-n
if __name__ == "__main__":
    t1=threading.Thread(target=run,args=(6,))
    t2=threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('num=',num)



