#多线程
import threading,time
def run(num):
    print("子线程(%s)开始"%(threading.current_thread().name))
    time.sleep(2)
    print("打印",num)
    time.sleep(2)
    print("子线程(%s)结束"%(threading.current_thread().name))

if __name__ == "__main__":
    print("主线程（%s)开始"%(threading.current_thread().name))
    #target我们这个线程所要执行的函数名字
    t=threading.Thread(target=run,name='run',args=(1,))
    t.start()
    #等待线程结束
    t.join()
    print("主线程(%s)结束"%(threading.current_thread().name))



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



