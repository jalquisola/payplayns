import time
import os 

def load():
    filename = os.path.basename(__file__)
    print('%s: loading data...' % filename)

    time.sleep(5)
    for i in range(10):
        print(i)

    print('%s: done...' % filename)

if __name__ == '__main__':
    load()

