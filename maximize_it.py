# Enter your code here. Read input from STDIN. Print output to STDOUT

k,m=map(lambda x : int(x),raw_input().split())
lists=[]

for i in range(k):
    lists.append(map(lambda x : int(x),raw_input().split())[1:])

from itertools import product

res=list(map(lambda x : sum(i**2 for i in x)%m, product(*lists)))

print(max(res))
