# 웹서버를 사용하기 위해선...
# 2대의 컴퓨터에 웹브라우저, 웹서버를 각각 설치해야 한다.

# docker를 이용하여 웹서버를 사용하고 싶다...
# 웹서버가 컨테이너에 설치된다...
# 웹서버가 설치된 컨테이너의 운영체제는 docker host라 부른다.
# host와 컨테이너는 각각 독립적인 포트를 가지고 있다.

# host의 포트와 컨테이너의 포트를 연결해 주어야 사용 가능하다.
docker run -p 8080:8080 httpd  # 포트포워딩 입니다 -p는 port가 아니고 publish입니다.


