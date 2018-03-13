"""
001. 별찍기1
작성자 : HaenaraShin
날 짜 : 2018.03.13
언 어 : Python
https://www.acmicpc.net/status/?from_mine=1&problem_id=2438
입력받은 숫자만큼 별을 찍는 문제
어떤식으로 입력받고 어떤식으로 출력하면 되는지 파악하기 위해 선정
"""

# 파이썬에서 입력은 String으로만 받으므로, int로 형변환 해줘야 한다.
n = int(input())

def printStars(n): # 함수 선언
    for i in range(n):
        print("*" * (i+1)) # 반복문 없이 i+1를 곱하면 그만큼 출력한다. 역시 편리한 파이썬

printStars(n)

"""
결과
7989721	hamster12345	2438	맞았습니다!!	29160 KB	64 MS	Python 3 / 수정	121 B
"""

"""
피드백

"""
