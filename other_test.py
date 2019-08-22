import numpy as numpy

class Multi_return_class():
    def __init__(self):
        self.a = 1
        self.b = 2
    
def test():
    return Multi_return_class()


def main():
    test2 = test()
    print(test2.a)
    print(test2.b)

if __name__ == "__main__":
    main()