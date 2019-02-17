def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if ord('a')<=ord(s[i])<=ord('z'):
            a=ord(s[i])+n
            if a>ord('z'):
                a-=26
            answer += chr(a)
        elif ord('A')<=ord(s[i])<=ord('Z'):
            a = ord(s[i]) + n
            if a>ord('Z'):
                a-=26
            answer+=chr(a)
        else:
            answer+=i
    return answer


print(solution("z Z", 3))