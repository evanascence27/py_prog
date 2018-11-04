#lambda functions
def show(n,j):
    return n*j#normal func
n=5
j=6
x=lambda :n*j#x=lambda n,j:n*j  or x=lambda n,j=0:n*j number of arg optional
print(x)
print(x())
print(show(n,j))
