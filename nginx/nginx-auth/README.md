# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---

Шифруем пароли для пользователей с помощью openssl:
openssl passwd SteveJobs1955
openssl passwd marketingP@ssword

Полученные кодированные пароли сохраняем в файл:
sudo nano /etc/nginx/conf.d/passwd

в следующем формате:
design:$1$vsRhOcQA$BjYSOORcfdoIkpdC9X8wT.
marketing:$1$7vzR98Kt$8wN6nl/X9vHBovjakfb47/

Устанавливаем права доступа к файлу:
sudo chmod 755 /etc/nginx/conf.d/passwd

Следующий шаг, настраиваем nginx чтобы установить аутентификацию, для этого в файле

sudo nano /etc/nginx/sites-available/default

Меняем конфиги сервера на следующее:

server {
    listen 8080;
    server_name example.com;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /images {
                alias /home/almas/Downloads/cats/;
                auth_basic "Private page";
                auth_basic_user_file /etc/nginx/conf.d/passwd;
    }


    location /gifs {
                alias /home/almas/Downloads/gifs/;
                auth_basic "Private page";
                auth_basic_user_file /etc/nginx/conf.d/passwd;
        }
}

Проверяем конфигурацию:
sudo nginx -t

Перезагружаем nginx:
sudo systemctl restart nginx

Далее отправляем запросы на адреса и получаем картинки:

curl -u design:SteveJobs1955 http://localhost:8080/images/
curl -u marketing:marketingP@ssword http://localhost:8080/gifs/