def solution(pn):
    answer ='*'*(len(pn)-4)
    answer +=pn[-4:]
    return answer

print(solution('01033334444'))