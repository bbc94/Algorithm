def solution(bl, w, tw):
    tw.sort()
    answer = 0
    while len(tw)>0:
        a=tw.pop(0)
        print(a)
        if len(tw)==0:
            break
        if (a+tw[0])<w:
            answer+=1
            a=tw.pop(0)
            for i in range(bl):
                answer+=1
        else:
            for i in range(bl):
                answer+=1




    return answer



print(solution(2, 10, [7, 4, 5, 6]))