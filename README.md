# movie-noti

 원하는 URL에서 필요한 부분을 크롤링해 텔레그렘 봇으로 결과를 보내준다.
 
     ex) 대전CGV에서 다음주 월요일 IMAX관 예매 가능하면 알려줘 

 movie_crawler.py를 사용하며 crawling_first.py와 telegram_bot.py를 통해 연습 할 수 있다.
 
 텔레그렘 봇을 사용하기 위한 토큰값과 채팅아이디는 확인후 빈칸을 채워 넣어야 한다.
 
--------------------------------------------------------------------------------------

1. 가상환경 설치 원하는 폴더로 이동 

        ex) cd python, E:

2. python -m venv movie_noti

        가상환경 movie_noti 폴더 생성

3. movie_noti 폴더 내 /Sctips/activat.bat 실행하여 가상환경 실행

4. pip install bs4 requests 사용

        bs4-0.0.1 requests-2.22.0

5. movie_noti 폴더에 movie_crawler.py 파일 생성

6. aws 인스턴스 시작 

7. 우분투 업데이트

8. apschedular 설치

9. 깃 또는 파일질라를 이용해 서버에 파일 업로드

10. nohup python3 movie_crawler.py를 우분투에서 실행

        서버 연결이 끊겨도 정삭적으로 백그라운드에서 실행

--------------------------------------------------------------------------------------
원하는 URL에서 필요한 부분을 찾아오는 방법은 검색
