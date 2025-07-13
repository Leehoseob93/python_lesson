name=input("근무자명:")
pay=input("시급:")
hour=input("총 근무시간:")

def cal(pay,hour):
    if int(hour)<=40:
        salary=int(pay)*int(hour)
    else:
        salary=int(40+1.5*(int(hour)-40))*int(pay)
    return salary
         
print(f"{name}님 총 급여액:{cal(pay,hour):,}")
print(pay)