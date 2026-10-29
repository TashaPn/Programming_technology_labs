class Singleton(object):
    i = None

    def __init__(self, a):
        print(id(self))
        print(a)

    def __new__(cls, a): 
        if cls.i == None:
            instance = super().__new__(cls)
            cls.i = instance
            return instance
        else:
            return cls.i
        


a1 = Singleton(1)
a2 = Singleton(2)

