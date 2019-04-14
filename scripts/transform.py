import time
import os 

def transform():
    filename = os.path.basename(__file__)
    print('%s: tranforming data...' % filename)

    time.sleep(5)
    for i in range(10):
        print(i)

    print('%s: done...' % filename)

if __name__ == '__main__':
    transform()

