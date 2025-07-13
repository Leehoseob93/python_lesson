def main():
    #영화 저장용 딕셔너리
    movies={'영화1':[1,2,3.5,5],'영화2':[1,3,3,5,2.5,3],'영화3':[1,1.5,1.5,2,2,3],'영화4':[3,2,3,3,4.5,4.5],'영화5':[]}

    def show_menu():
        print('===과제 시나리오===')
        print('1. 영화 등록')
        print('2. 평점 등록')
        print('3. 영화 TOP3')
        print('4. 추천 영화')
        print('5. 전체 영화 및 평점 목록 조회')
        print('6. 특정 영화의 평균 평점 조회')
        print('7. 종료')

    def add_movie():
        name=input('영화 이름을 입력하세요: ')
        if name in movies:
            print(f'이미 등록된 영화입니다.') #영화 이름 / 평균 평점 보여주기(?)
        else:
            movies[name] = []
            print(f' {name} 이/가 등록되었습니다')
        return name
    
    def add_score():
        print(f'등록된 영화 목록')
        for movie in movies.keys():
            print(f'{movie}')
        name = input('영화이름을 입력하세요')
        if name in movies:
            score = int(input('평점을 입력하세요(1~5점):'))
            movies[name].append(score)
            print(f'{score}점이 등록되었습니다.')
        else:
            print(f'등록된 영화이름을 입력해주세요')

    def show_top3_movies():
            rank=0
            al_movies = {k:v for k, v in movies.items() if v}
            for k1, v1 in al_movies.items():
                al_movies[k1]= sum(v1) / len(v1)
            top3 = sorted(al_movies.items(), key=lambda x : x[1], reverse=True)[:3]
            for name, score in top3:
                rank += 1
                print(f'TOP{rank}. 영화: {name} / 평점: {score:.2f}')

    def recommend_movies():
        print(f'등록된 영화 목록')
        score_lst={}
        for movie, score in movies.items():
                if len(score)>0:
                    score_lst[movie] = sum(score)/len(score)
        for movie1, score1 in score_lst.items():
                print(f'영화명:{movie1}/평점:{score1:.2f}') 

        rec={}
        name = input('평점 기준 영화를 입력하세요:')
        if name in score_lst:
                for name2, avg in score_lst.items():
                    if name2 == name:
                            continue
                    if abs(round(score_lst[name],1) - round(avg,1)) <= 0.5:
                            rec[name2]=avg
                
                print(f'추천영화 목록')
                rank=sorted(rec.items(), key=lambda x : x[1], reverse=True)
                for name2, avg in rank:
                    print(f'{name2} : {avg:.2f}점')
        
        else:
                print(f'등록된 영화가 아닙니다.')
    

    def show_all():
        print(f'전체 영화 및 평점 목록')
        print(f"{movies}")

    def show_a():
        print(f'등록된 영화 목록')
        for movie in movies.keys():
            print(f'{movie}')
        name=input('영화 이름을 입력하세요:')
        if name in movies:
            for name, score in movies.items():
                total = 0
                for s in score:
                    total += s
                    avg = total / len(score)
            print(f'영화:{name} / 평균 평점:{avg:.2f}')
        else:
            print(f'등록되지 않은 영화입니다.')

    show_menu()

    while True:
        number=int(input('번호를 입력하세요:'))
        if number == 1:
            add_movie()
        elif number == 2:
            add_score()
        elif number == 3:
            show_top3_movies()
        elif number == 4:
            recommend_movies()
        elif number == 5:
            show_all()
        elif number == 6:
            show_a()
        elif number == 7:
            break
        show_menu()

if __name__ == "__main__":
    main()