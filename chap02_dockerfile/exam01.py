# image 자체는 실행할 수 없기 때문에 run 명령어로 컨테이너를 만들어서 실행한다.
# 나도 image를 만들고 싶다.

# 컨테이너를 commit으로 image를 만들 수 있다.
# dockerfile을 만들어 build 명령하면 image를 만들 수 있다.

# commit
# 이미 사용하고 있는 컨테이너를 image로 만든다. 약간 백업용의 느낌이 있다.
docker commit ws1 ws-commit  # 'ws1' 컨테이너로 'ws-commit' 이미지를 만듭니다.

# dockerfile
# 만들고 싶은 이미지를 명령어모음(dockerfile)을 이용해 image로 만든다.
FROM ubuntu:20.04  # 우분투를 베이스이미지
RUN apt update && apt install -y python3  # apt update를 하고 python3를 설치합니다. -y로 사용자 입력을 기다리지 않습니다.
WORKDIR /var/www/html  # 리눅스내에서 mkdir -p /var/www/html 의 명령을 실행하고 해당 디렉토리로 이동
# 컨테이너에서 index.html을 만들고 싶으면...
RUN echo "Hello, <h1>Docker!</h1>" > index.html  # 위 내용으로 index.html을 만듭니다.
# 호스트에서 컨테이너로 복사하고 싶으면...
COPY ["index.html","."]  # [호스트의 파일을 , /var/www/html로] 복사
# python에 내장된 웹서버를 바로 실행시키고 싶으면...
CMD ["python3", "-u", "-m", "http.server"]

# RUN과 CMD의 차이
# RUN은 build되는 시점에 실행되는 명령어 - image에 반영
# CMD는 컨테이너가 실행될 때 실행되는 명령어 - container에 반영

docker build -t ws-build .  # 'ws-build'라는 이름으로 현재 디렉토리(.)의 도커파일로 이미지를 만듭니다.
