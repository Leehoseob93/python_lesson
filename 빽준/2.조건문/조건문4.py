x, y = map(float,(input().split(' ')))

if x>0 and y>0:
    print(f'Quadrant #1')
elif x<0 and y>0:
    print(f'Quadrant #2')
elif x<0 and y<0:
    print(f'Quadrant #3')
elif x>0 and y<0:
    print(f'Quadrant #4')