from functools import wraps
import time


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("time:%s s" % (str(t1 - t0)))
        return result

    return function_timer