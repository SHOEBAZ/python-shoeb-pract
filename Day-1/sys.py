# agar hume similar modules use karna hai tu pypi aur python installtion me sab mil jaate aur agar jo intalltion par use karne usko use karte as (sys)
# ye command line argument ka section hai (sys.agv[1])


import sys

def add():
    add = num1 +  num2
    return add

def sub():
    s = num1 - num2
    return s

def mul():
    m = num1 * num2
    return m

num1 = int (sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if  operation == "add":
    output = add(num1, num2)
    print(output)

# env vars wo hai jo sesisitive dtata jo hard coded hai usko encryt karkne use hoti
# command (env) aur agar create karna hai tu (export password="shoeb") aur code me write import os.getenv("password)

import os
print(os.getenv("apitokeen"))