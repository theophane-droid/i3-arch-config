#!/bin/python
import sys

def get_value():
    v=-1
    with open("/sys/class/backlight/amdgpu_bl0/brightness", "r") as f:
        v = int(f.readline())
    return v
def set_value(value):
    with open("/sys/class/backlight/amdgpu_bl0/brightness", "w") as f:
        f.write(str(value))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        actual = get_value()
        delta = int(sys.argv[2])
        if sys.argv[1]=="up":
            if actual+delta<=255:
                set_value(actual+delta)
            else:
                set_value(255)
        if sys.argv[1]=="down":
            if actual-delta>=0:
                set_value(actual-delta)
            else:
                set_value(0)
    pourcentage = int(get_value()/255*100)
    print(" ",str(pourcentage)+"% ")
