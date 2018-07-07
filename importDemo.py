import ListMapFile as lmf


lst2 = [1,2,3,4,5]
lst3 = [3,5,6,7,8]
f = lambda x: x**4
print(lmf.listMap(lst2,f))
print(lmf.listMap(lst3,f))


