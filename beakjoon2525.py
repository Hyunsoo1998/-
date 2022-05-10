# + 는 더하기
#
# - 는 빼기
#
# *는 곱하기
#
# / 는 나누기
#
# % 는 나머지
#
# // 는 몫  **는거듭제곱

H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)
