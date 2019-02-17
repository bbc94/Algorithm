def solution(n, k):
    answer = ''
    tmp=list()
    count=0
    while count != k:
        for i in range(len(str(n))):
            if i==0:
                tmp.append(str(n)[:i]+str(n)[i+1:])
            else:
                if int(tmp[0])<int(str(n)[:i]+str(n)[i+1:]):
                    tmp.append(str(n)[:i] + str(n)[i + 1:])
                    tmp.pop(0)
        n=tmp[0]
        tmp.clear()
        count+=1

    return n

print(solution(923456,2))