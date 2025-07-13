import calendar
from datetime import datetime

day_map = {"월":0, "화":1, "수":2, "목":3, "금":4, "토":5, "일":6, "평일":[0,1,2,3,4], "주말":[5,6]}
base_pay=input("기본시급:")

#class를 생성하여 근무자들의 속성을 입력해줌
class Worker:
    def __init__ (self, name, period, day, schedule, overtime):
        self.name = name # 근무자 이름
        self.period = period # 근속 기간 (n개월)
        self.day = day # 주말/평일/요일
        self.schedule = schedule # 파트 시간 (OP, MD, CL)
        self.overtime = overtime # 월 O.T 시간
    
    def cont_pay(self):
        t_pay = base_pay + (self.period//3) * 100 # 3개월 근무당 시급 100원 상승 '//' 버림 나누기
        return t_pay
    
    def schedule_pay(self):# 근무파트 당 일급
        t_pay = self.cont_pay
        if self.schedule == "closer":
            s_pay = t_pay * (5 + 1.5*(7-5))
            return s_pay
        else:
            s_pay = t_pay * 7
            return s_pay

def count_days(worker, month, year=None): # 올해의 월 캘린더를 가져오고 입력된 값을 기반으로 일 수를 계산함함
    if year == None:
        year = datetime.now().year # 올해를 인식하는 방법 -> def에 넣으면 함수가 정의될때의 날짜로 고정됨 -> 내년에 써도 2025년
    
    cal = calendar.monthcalendar(year,month)
    indexes = [day_map[d] for d in worker.day]
    print(indexes)

    count = 0
    for week in cal:
        count += sum(1 for i in indexes if week[i] !=0) # 여기 잘 모르겠음 이해가 안됨
    return count

def Total_salary(t_pay,s_pay,count,overtime):
    salary=int(s_pay * count + 1.5 * overtime * t_pay)
    return salary


def main():
    month = int(input("계산할 월"))
    num = int(input("근무자 수:"))
    workers=[]

    for i in range(num):
        name = input("근무자명:")
        period = int(input("근무기간:"))
        day=input("근무요일(예: 월/수/금 / 평일 / 주말):").split("/")
        schedule=input("근무스케줄(OP/MD/CL):")
        overtime=int(input("OT시간:"))
                    
        w = Worker(name, period, day, schedule, overtime)
        workers.append(w)

    all_salary=0

    for w in workers:
        count = count_days(w, month)
        s_pay = Worker.schedule_pay(base_pay)
        salary = Total_salary(s_pay,count)
        all_salary+=salary
        print(f"이름:{w.name} {month}월 급여:{salary}")
        print(f"이번달 총 인건비:{all_salary}")


main()