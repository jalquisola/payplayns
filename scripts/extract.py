import time
import os 

def extract():
    filename = os.path.basename(__file__)
    print('%s: extracting data...' % filename)
    for i in range(10):
        print(i)
    print('%s: done...' % filename)

if __name__ == '__main__':
    extract()

