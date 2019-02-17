def solution(n):
    n_bi = bin(n).count('1')
    a=n+1
    while a>n:
        b=str(bin(a)).count('1')
        if b==n_bi:
            return a
        else:a+=1


print(solution(78))