def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

# Tu lengthy code lines likhne se better hai ke functions use kare agar calculator create karna hai tu jo niche hai code wese banaye
# tu functions readiblity aur re-usablity(modularity) aur debugging ke liye use hota

num1 = 10 
num2 = 5

def addition():
    add = num1 +  num2
    print(add)

def sub():
    s = num1 - num2
    print(s)

def mul():
    m = num1 * num2
    print(m)

addition()
sub()
mul()


