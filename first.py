list = [x* x for x in range(5)]
def fun(lst):
    del [lst[2]]
    return lst
print(fun(list))
