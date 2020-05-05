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
