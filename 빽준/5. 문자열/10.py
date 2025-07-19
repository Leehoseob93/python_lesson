alphabet = []
for i in range(65,90):
    alphabet.append(chr(i))

number = list(''.join(str(i)*3 for i in range(2,10)))

time = {}
for i in number:
    time[i] = int(i)+1

word = list(input('단어를 입력하세요'))
cal = []
for i in word:
    idx = alphabet.index(i)
    N = number[idx]
    sec = time[N]
    cal.append(sec)


print(f'{sum(cal)}')
