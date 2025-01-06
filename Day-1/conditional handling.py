import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will create the instance for you")
else:
    print("your input is not t2.micro, ao we canot create")