def GCD(n,m):
    tmp=0
    if n<m:
        tmp=m
        m=n
        n=tmp
    if n%m==0:
        return m
    return GCD(m,n%m)
def LCM(n,m,a):
    if a==1:
        return n*m
    else:
        return (n//a)*(m//a)*a

def solution(n, m):
    answer = []
    a=GCD(n, m)
    b=LCM(n,m,a)
    answer.append(a)
    answer.append(b)
    return answer


print(solution(10,5))
print(LCM(7,5,GCD(7,5)))