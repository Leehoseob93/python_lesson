movies={'영화1':[1,2,3.5,5],'영화2':[1,3,3,5,2.5,3],'영화3':[1,1.5,1.5,2,2,3],'영화4':[3,2,3,3,4.5,4.5],'영화5':[]}

def show_top3_movies():
        rank=0
        al_movies = {k:v for k, v in movies.items() if v}
        for k1, v1 in al_movies.items():
              al_movies[k1]= sum(v1) / len(v1)
        top3 = sorted(al_movies.items(), key=lambda x : x[1], reverse=True)[:3]
        for name, score in top3:
            rank += 1
            print(f'TOP{rank}. 영화: {name} / 평점: {score:.2f}')

show_top3_movies()

# AI 찾아본거
# 1. value에 조건 걸고 가져오기 → {k:v for k, v in movies.items() if v}
# al_movies = {k:sum(v)/len(v) for k,v in movies.items() if v}로 1,2 번 한 번에도 가능.
# 2. value값 바꾸기 → dic['key'] = value
# 따로 새로운 딕셔너리를 만들어주지 않아도, dic['key'] = value를 해주면 딕셔너리의 밸류 값이 완전히 변경되는 것임.
# 3. top3 = sorted(al_movies.items(), key=lambda x : x[1], reverse=True)[:3] 줄세우기 문법
# al_movies.items()에서, lambda x : x[1] = value값으로, reverse = 내림차순, [:3] 3개까지만