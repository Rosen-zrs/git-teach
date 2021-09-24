'''
Author: Rosen
Date: 2021-09-24 10:01:23
LastEditTime: 2021-09-24 10:21:06
Description: Git example
FilePath: /home/rosen/下载/git-example/main.py
'''

def add(a, b):
    try:
        return a+b
    except:
        raise TypeError

def multiply(a, b):
    try:
        return a*b
    except:
        raise TypeError

if __name__ == "__main__":
    x = add(1, 2)
    print(x)
