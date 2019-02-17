def solution(s):
    answer = ''
    tmp=list(ord(s[i]) for i in range(len(s)))
    tmp.sort()
    answer=''.join(list(map(chr,tmp)))
    return answer

print(solution('ZBCSscas'))