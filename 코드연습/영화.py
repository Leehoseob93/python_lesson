def main():
    #영화 저장용 딕셔너리
    movies={}

    def show_menu():
        print('===과제 시나리오===')
        print('1. 영화 등록')
        print('2. 평점 등록')
        print('3. 전체 영화 및 평점 목록 조회')
        print('4. 특정 영화의 평균 평점 조회')
        print('5. 종료')

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
            print(f'영화:{name} / 평균 평점:{avg}')
        else:
            print(f'등록되지 않은 영화입니다.')

    while True:
        show_menu()
        number=int(input('번호를 입력하세요:'))
        if number == 1:
            add_movie()
        elif number == 2:
            add_score()
        elif number == 3:
            show_all()
        elif number == 4:
            show_a()
        elif number == 5:
            break
if __name__ == "__main__":
    main()