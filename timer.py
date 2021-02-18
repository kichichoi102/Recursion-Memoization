import time
import sys

def tic():
    import time
    global t_start
    t_start = time.time()

def toc():
    import time
    if 't_start' in globals():
        print("Elapsed time is " + str(time.time() - t_start))
    else:
        print('Error: Method, tic(), was not called')


