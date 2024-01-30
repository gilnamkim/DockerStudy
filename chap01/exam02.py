# docker run 명령어
docker run --name ws1 httpd  # httpd 이미지로 'ws1'의 이름을 가진 컨테이너를 생성합니다.

# docker ps 명령어
docker ps  # 현재 실행되고 있는 컨테이너 목록
docker ps -a  # stop시킨 컨테이너까지 목록

# docker stop 명령어
docker stop ws1  # 'ws1'의 컨테이너를 정지합니다.

# docker start 명령어
docker start ws1  # 'ws1'의 컨테이너를 실행합니다. 컨테이너목록에 없는 이름은 실행이 안됩니다.

# docker log 명령어
docker logs ws1  # 'ws1'의 로그를 확인합니다.
docker logs -f ws1  # 'ws1'의 로그를 계속 확인합니다.

# docker rm 명령어
docker rm ws1  # 'ws1' 컨테이너를 삭제합니다. 단, 컨테이너가 동작하지 않을 때만 가능합니다.
docker rm --force ws1  # 'ws1' 컨테이너를 강제로 삭제합니다. 동작여부 상관없습니다.

# docker rmi 명령어
docker rmi httpd  # httpd 이미지를 삭제합니다.