movies={'영화1':[1,2,3.5,5],'영화2':[1,3,3,5,2.5,3],'영화3':[1,1.5,1.5,2,2,3],'영화4':[3,2,3,3,4.5,4.5],'영화5':[]}

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
      
          
recommend_movies()

# 왜 name2, avg in rank를 가져올때는 items를 쓰면 안되는거지? sorted를 쓰면 딕셔너리가 풀리는건가?
# sorted를 사용하면, 딕셔너리가 아닌 튜플을 항목으로 갖는 리스트로 변환되기 때문임 !