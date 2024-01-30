# 어떤 프로그램을 설치할 때...

# 애플의 app store의 역할을 하는 것이 docker hub
# 애플리케이션은 program... docker에서는 'pull'을 통해 image를 다운로드
# 프로그램이 실행될 때 process가 실행... docker에서는 'run'을 통해 container를 생성하고 container가 실행

# docker pull 명령어
docker pull httpd  # docker hub에서 'httpd'라는 이미지를 가져옵니다.

# docker images 명령어
docker images  # 보유한 docker image의 목록을 보여줍니다.