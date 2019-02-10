def solution(s):
    answer = ''
    cout = 1
    for i in range(len(s)):
        if cout%2==1:
            answer+=s[i].upper()
            cout+=1
        elif cout%2==0:
            answer += s[i].lower()
            cout += 1
        if s[i]==' ':
            cout=1

    return answer


print(solution(	"tr hello world"))