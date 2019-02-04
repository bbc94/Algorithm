def solution(s, k):
    answer = 0
    s.sort(reverse=True)
    count = 0
    while len(s)>0:
        m1 = s.pop()
        if len(s) == 0:
            return -1
        m2=s.pop()
        if m1<k:
            count +=1
            comb=m1+(m2*2)
            s.append(comb)
            s.sort(reverse=True)
            print(s)
            if s[-1]>k:
                break
        else:
            return 0

    return count

def solutio(s, k):
    count = 0
    while len(s)>0:
        m1 = min(s)
        s.remove(m1)
        if len(s) == 0:
            return -1
        m2= min(s)
        s.remove(m2)
        if m1<k:
            count +=1
            comb=m1+(m2*2)
            s.append(comb)
            print(s)
            if min(s)>k:
                break
        else:
            return 0

    return count




print(solutio([1, 2, 3, 9, 10, 12], 11))