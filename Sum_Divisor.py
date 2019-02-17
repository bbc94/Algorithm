def solution(n):
    answer = 0
    mid=int(n ** 0.5)

    for i in range(1,mid+1):
        if n%i==0:
            answer+=i
            answer+=(n//i)
            if i==(n//i):
                answer-=i
    return answer


print(solution(10z0))