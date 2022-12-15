'''
LIS 라는 친구에 관련된 문제
아주 기본 예제인것 같더군요
DP를 사용해서 가장 긴 증가하는 부분 수열의 길이'만' 알아내는 코드
'''


# 전체 수열의 길이
N = int(input())
# 수열을 받아주고
nums = list(map(int, input().split()))
# 수열의 길이와 같은 리스트를 만들어준다
# 이 친구의 역할은 해당 인덱스를 기준으로 만들수 있는 LIS의 최대 길이를 기록해준다.
length = [0 for _ in range(N)]
# 전체 수열을 순회를 한번 해준다
for k in range(N):
    # 해당 수열의 위치에 친구는 그 친구 하나만으로도 1개의 증가 수열을 만족하기 때문에 
    # 해당 인덱스의 길이값을 1로 초기화해준다
    length[k] = 1
    # 그 친구 앞에 나왔던 친구들을 순회한다
    for i in range(k):
        # 현재 기준점 앞에 있는 친구들중에 기준점보다 작은 친구 하나가 나온다면
        if nums[i] < nums[k]:
            # 지금 이친구 기점으로 만들어진 수열의 길이와 
            # i번째 인덱스를 기점으로 만들어진 최대 수열의 길이 +1과 비교해서 최대값으로 k번째 인덱스 길이 값을 최신화
            length[k] = max(length[k], length[i] + 1)
# 전체 길이들 중에서 최댓값 출력하기
print(max(length))