def solution(n, words):
    answer = []
    tmp=''
    temp=list()
    for i,j in enumerate(words):
        if words.count(j)>1:
            k= words[i+1:].index(j)
            k+=(i+1)
            temp.append(k)
            pass
        if i !=0:
            if tmp[-1] != j[0]:
                temp.append(i)
                break
            else:
                tmp=j
        else:
            tmp=j
    temp.sort()
    if len(temp)==0:
        answer.append(0)
        answer.append(0)
    else:
        k =temp[0]
        turn = ((k + 1) // n)
        seq = (k % n) + 1
        if seq != n:
            turn += 1
        answer.append(seq)
        answer.append(turn)
    return answer


print(solution(2, ["hn", "ne", "ne", "ow", "ow", "world", "world"]))