H, M = map(int, input('시:분 >>').split(':'))

if 45 > M >=0:
    if H == 0:
        print(f'알람시각 23시 {60-(45-M)}분')
    else:
        print(f'알람시각 {H-1}시 {60-(45-M)}분')
else:
    print(f'알람시각 {H}시 {M-45}분')

