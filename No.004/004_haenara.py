"""
004. 
작성자 : HaenaraShin
날 짜 : 2018.03.14
언 어 : Python
https://www.acmicpc.net/problem/2839

"""
def get_sugar(n):
    answer = -1
    if n >= 10:
        if n % 10 == 0:
            answer = n / 5
        elif n % 10 == 1:
            answer = int(n / 5) + 1
        elif n % 10 == 2:
            answer = int(n / 5) + 2
        elif n % 10 == 3:
            answer = int(n / 5) + 1
        elif n % 10 == 4:
            answer = int(n / 5) + 2
        elif n % 10 == 5:
            answer = int(n / 5)
        elif n % 10 == 6:
            answer = int(n / 5) + 1
        elif n % 10 == 7:
            answer = int(n / 5) + 2
        elif n % 10 == 8:
            answer = int(n / 5) + 1
        elif n % 10 == 9:
            answer = int(n / 5) + 2
    elif n == 3:
        answer = 1
    elif n == 5:
        answer = 1
    elif n == 6:
        answer = 2
    elif n == 8:
        answer = 2
    elif n == 9:
        answer = 3
    return answer

n = int(input())
print(get_sugar(n))
"""
결과
8001620	hamster12345	2839
설탕 배달
맞았습니다!!	29160 KB	64 MS	Python 3 / 수정	926 B
"""

"""
피드백

"""
