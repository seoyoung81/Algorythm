number = int(input()) # 스위치 개수 (100이하)
switch = list(input().split())  # 스위치 상태 1 켜짐 0 꺼짐
students = int(input()) # 학생 수
gender, switch_number = map(int, input().split()) # 학생 성별 남 1 여 2, 받은 수

if gender == 2:
    for order in switch:
        for i in range(1, len(switch)):
            if switch[switch_number - i] != switch[switch_number + i]:
                print(f'{i+3} 스위치를 바꾸겠습니다. ')
            

