docker build -t jusan-fastapi-final:dockerized .

docker images

docker run --name jusan-dockerize -d -p 8080:8080 jusan-fastapi-final:dockerized
