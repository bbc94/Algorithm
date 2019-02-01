def solution(priorities, location):
    answer=0
    a=priorities[priorities.index(max(priorities)):]
    a.sort(reverse=True)
    b=priorities[:priorities.index(max(priorities))]
    b.sort(reverse=True)
    c=a+b
    if location>=priorities.index(max(priorities)):
        answer=a.index(priorities[location])
    else:
        answer=len(a)+b.index(priorities[location])
    return c,answer

print(solution(	[1, 3, 9, 1, 1, 2], 0))