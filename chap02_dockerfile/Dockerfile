# dockerfile
# 만들고 싶은 이미지를 명령어모음(dockerfile)을 이용해 image로 만든다.
# 우분투를 베이스이미지
FROM ubuntu:20.04
RUN apt update && apt install -y python3  # apt update를 하고 python3를 설치합니다. -y로 사용자 입력을 기다리지 않습니다.
# 리눅스내에서 mkdir -p /var/www/html 의 명령을 실행하고 해당 디렉토리로 이동
WORKDIR /var/www/html
# 컨테이너에서 index.html을 만들고 싶으면...
RUN echo "Hello, <h1>Docker!</h1>" > index.html  # 위 내용으로 index.html을 만듭니다.
# 호스트에서 컨테이너로 복사하고 싶으면...
# [호스트의 파일을 , /var/www/html로] 복사
COPY ["index.html","."]
# python에 내장된 웹서버를 바로 실행시키고 싶으면...
CMD ["python3", "-u", "-m", "http.server"]