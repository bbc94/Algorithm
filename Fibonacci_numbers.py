def solution(n):
    me=[]

    for i in range(0,n):
        if i == 0:
            me.append(0)
        elif i == 1:
            me.append(1)
        else:
            me.append(me[i-1]+me[i-2])
    return me[-1]

print(solution(5))