def solution(n):
    answer = -1
    sqrt = n ** (1 / 2)
    for i in range(1,(n//2)+2):
        if (n/i)==i:
            return (i+1) ** 2
    return answer,sqrt

print(solution(6))


