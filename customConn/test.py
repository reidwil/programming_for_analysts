def create_generator():
    def __enter__():
        mylist = range(3)
        for i in mylist:
            yield i*i
    def __exit__(traceback, ):
        return


with create_generator() as mygenerator:
    for i in mygenerator:
        print(i)
