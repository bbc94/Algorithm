def solution(n):
    answer=''
    ls = list(str(n))
    for i in range(len(ls)):
        answer+=str(ls[i])
    return answer,ls
print(solution(312))
