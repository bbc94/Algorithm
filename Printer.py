def solution(priorities, location):
    tmp = list()
    for i,j in enumerate(priorities):
        tmp.append([j,i])
    answer=0
    a=tmp[priorities.index(max(priorities)):]
    for i in range(len(a)):
        a = tmp[priorities.index(max(priorities))+i:]
        print(a)
    b=tmp[:priorities.index(max(priorities))]
    b.sort(reverse=True)

    c=a+b
    for i in range(0,len(c)):
        if location == c[i][1]:
            return c,i


print(solution([1, 1, 9, 1, 1, 1], 0))