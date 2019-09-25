from multiprocessing import Process, Manager

def somefunc():
    print("yes")

def f(d):
    d[1]()
    # d['2'] = 2
    # d[0.25] = None
    # l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        # l = manager.list(range(10))

        d[1] = somefunc

        p = Process(target=f, args=(d, ))
        p.start()
        p.join()

        print(d)
        # print(l)
