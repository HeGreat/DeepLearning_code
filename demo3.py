import threading,time

bar=threading.Barrier(3)
def run():
    print("%s----start\n"%(threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    print('%s---end\n'%(threading.current_thread().name))


if __name__ == "__main__":
    for i in range(6):
        threading.Thread(target=run).start()
