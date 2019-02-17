def solution(x):
    answer = True
    sum=0
    for i in range(len(str(x))):
        sum += int(str(x)[i])

    if x%sum:
        return False
    else:
        return answer




print(solution(11))