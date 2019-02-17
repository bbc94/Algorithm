def prime_YN(n):
    mid=int(n ** 0.5)

    for i in range(1,mid+1):
        if n%i==0 and i!=1:
            return False
    return True


def solution(numbers):
    num=''
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                num+=numbers[i]

    answer = 0
    return answer


print(solution(12))