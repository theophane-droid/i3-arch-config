#!/bin/python
from os import system
from random import randint

def exec(cmd):
    random_name = "tmp" + str(randint(0,100000))
    system("sh -c '" + cmd + " > " + random_name + "'")
    content = ""
    with open(random_name,"r") as f:
        line = f.readline()
        content += line
        while line:
            line = f.readline()
            content += line
    system("sh -c 'rm " + random_name + "'")
    return content

if __name__ == "__main__":
    if "off" not in exec("amixer -c 1 sget Master"):
        system("amixer -c 1 sset Master mute")
    else:
        system("amixer -c 1 sset Master unmute")