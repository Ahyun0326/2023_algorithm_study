def solution(array, commands):

    answer = []

    #commands의 범위만큼 array 리스트 자르기
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        pos = commands[i][2] - 1

        # array의 start-1번째부터 end번째 까지 리스트 자르기
        result = array[start - 1:end]
        
        # pos가 result 리스트의 범위를 벗어난 경우 프로그램 종료
        if pos > len(result):
            print("범위를 벗어났습니다.")
            return
            
        #print(result)

        # array 오름차순 정렬
        result.sort()
        #print(result)

        # pos 위치의 값 answer에 저장
        answer.append(result[pos])
    
    return answer
