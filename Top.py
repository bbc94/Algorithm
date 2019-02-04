def solution(heights):
    answer = []
    j=0
    for i in range(len(heights)):
        answer.append(0)
    for i in range(len(heights)-1,-1,-1):
        j=i
        while j>0:
            j -= 1
            if heights[i]<heights[j]:
                print(heights[i],heights[j])
                answer[i]=j+1
                break

    return answer



print(solution([6,9,5,7,4]))