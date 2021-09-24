n = int(input()) # 68 입력
num = n
cnt = 0

while True:
    a = num // 10 # 6이 나왔다.
    b = num % 10 # 몫은 8이 나왔다.
    c = (a + b) % 10 # 몫이 4가 나온다.
    num = (b * 10) + c

    cnt += 1
    if(num == n):
        break

print(cnt)