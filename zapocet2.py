#!/usr/bin/env python3
def myeval(a, b):
    if(type(a) == str):
        return b[a]
    elif(type(a) == int or type(a) == float):
        return a
    
    if(type(a[1]) == list):
        a[1] = myeval(a[1], b)
    if(type(a[2]) == list):
        a[2] = myeval(a[2], b)
        
    if(type(a[1]) == str):
        a[1] = b[a[1]]
    if(type(a[2]) == str):
        a[2] = b[a[2]]
        
    if(a[0] == "+"):
        return a[1] + a[2]
    elif(a[0] == "-"):
        return a[1] - a[2]
    elif(a[0] == "*"):
        return a[1] * a[2]
    elif(a[0] == "/"):
        return a[1] / a[2]
    
print(myeval(['/',['*','x',3],'y'],{'x':3, 'y':3}))

def myderive(f, z):
    if(type(f) == int or type(f) == float):
        return 0
    elif(type(f) == str and f == z):
        return 1
    elif(type(f) == str and f != z):
        return 0
    
    if(f[0] == "-"):
        return ["-",myderive(f[1],z), myderive(f[2],z)]
    if(f[0] == "+"):
        return ["+",myderive(f[1],z), myderive(f[2],z)]
    if(f[0] == "*"):
        return ["+",["*",myderive(f[1],z),f[2]],["*",f[1],myderive(f[2],z)]]
    if(f[0] == "/"):
        return ["/",["-",["*",myderive(f[1],z),f[2]],["*",f[1],myderive(f[2],z)]],["*",f[2],f[2]]]
    