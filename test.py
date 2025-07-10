#딕셔너리

person={'이름':'이호섭', '나이':'만32세'}
person['직업'] = 'Engineer'


for key, value in person.items():
    print(f"{key}:{value}")