def solution(s):
    answer = True
    count=0
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] in '0123456789':
                count+=1
    if count==len(s):
        return answer
    return False


print(solution(''))