import string
import sys

POSITION = 0
ID = 1

# Test Case T
T = int(sys.stdin.readline())

for test_case in range(T):

    N ,L , K = sys.stdin.readline().split(' ')

    ants = []         # (개미의 좌표, ID) 로 이루어진 개미목록
    left_side = []    # x = 0 절편
    right_side = []   # x = L 절편
    
    for i in range(int(N)): 
        position, ant_id = input().split(' ')
        ants.append((int(position), int(ant_id)))
        if ants[i][ID] < 0:
            # ID 가 음수면 y = -x + p 이므로 절편은 (0,p)
            left_side.append([ants[i][POSITION],0])                 
        else:
            # ID가 양수면 y = x - p 이므로 절편은 (L, L-p)
            # 단 이쪽 절편도 오름차순으로 만들기 위해 순서를 반대로 삽입
            right_side.insert(0, [int(L) - ants[i][POSITION], 0])

    
    for i in range(len(left_side)):
        # 왼쪽 절편 매칭하는 ID 설정
        left_side[i][ID] = int(ants[i][ID])
    for i in range(len(right_side)):
        # 오른쪽 절편 매칭하는 ID 설정
        right_side[len(right_side)-i-1][ID] = int(ants[i+len(left_side)][ID])
            



    left_pivot = 0
    right_pivot = 0
    total = []
    # MergeSort 합치듯이, 두개의 이미 정렬되어 있는 리스트 두개를 합쳐서 정렬.
    while True:
        # 한쪽 절편이 이미 정렬이 끝나면 다른 한 쪽 나머지를 다 붙인다.
        if left_pivot >= len(left_side):
            total += right_side[right_pivot:]
            right_pivot = len(right_side)
        elif right_pivot >= len(right_side):
            total += left_side[left_pivot:]
            left_pivot = len(left_side)
        else:
            left = left_side[left_pivot][POSITION]
            right = right_side[right_pivot][POSITION]
            if left < right:
                total.append(left_side[left_pivot][ID])
                left_pivot += 1
            elif left > right:
                total.append(right_side[right_pivot][ID])
                right_pivot += 1
            elif abs(left_side[left_pivot][ID]) < abs(right_side[right_pivot][ID]):
                total.append(left_side[left_pivot][ID])
                left_pivot += 1
                total.append(right_side[right_pivot][ID])
                right_pivot += 1
            else :
                total.append(right_side[right_pivot][ID])
                right_pivot += 1
                total.append(left_side[left_pivot][ID])
                left_pivot += 1

        if left_pivot + right_pivot >= int(K):
            # 다 돌기 전에 K값을 찾으면 빠져나온다.
            print(total[int(K)-1])
            break



    
    
    
    
    

        

    
