# docker exec 명령어로 컨테이너 내부파일을 수정하면 위험하다...
# 컨테이너를 사용하는 이유는 필요할 때 언제든 생성하고 필요없으면 언제든 지울 수 있는 장점을 활용하려면...
# 실행환경은 컨테이너에게 맡기고 파일수정작업은 호스트에서 진행해보자

docker run -p 8888:80 -v ~/Desktop/htdocs:/usr/local/apache2/htdocs/ httpd
# -v @@@:%%%  '@@@'과 '%%%' 두 디렉토리를 연결

# 호스트 단에서 파일 수정이 이루어지기 때문에 버전관리하기 좋다...