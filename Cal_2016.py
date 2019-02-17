import calendar
def solution(a, b):
    a = calendar.weekday(2016, a, b)
    week={0:'MON',1:'TUE',2:'WED',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    answer = week[a]
    return answer


print(solution(2,10))