#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    names = ()
    for n in range(len(names)):
        if names[n][:2] != "__":
            print("{}".format(names[n]))
