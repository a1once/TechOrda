# nginx-locations

### Полезное

- [Downloading files with curl ](http://www.compciv.org/recipes/cli/downloading-with-curl/)
- [unzip](https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal)
- [nginx: alias](http://nginx.org/en/docs/http/ngx_http_core_module.html#alias)
- [nginx location 404 not found](https://stackoverflow.com/questions/41099318/nginx-location-404-not-found)

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` равным значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html). Файл должен быть неизмененным - если будете копировать-вставлять текст из файле, то возможно может добавиться лишний символ.
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip)
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip)
6. Добавьте `location` блок для пути `/secret_word`, который возвращает строку `jusan-nginx-locations` со статусом `201`.

Чтобы проверить запрос на созданный `server` блок, запустите команду.

```bash
curl -H "Host: example.com" http://localhost:8080/
```

---

### Ответ

Меняем конфиги, добавляем новое значение сервер который слушает 8080:
```bash
sudo nano /etc/nginx/sites-available/default
```

Добавляем следующий блок:
```html
server {
    listen 8080;
    server_name example.com;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /images {
        alias /home/almas/Downloads/cats/;
    }

    location /gifs {
        alias /home/almas/Downloads/gifs/;
    }

    location /secret-word {
        return 201 'jusan-nginx-locations';
    }
}
```

Добавляем ссылку на дефолт файл внутри nginx.conf с помощью добавления строчки:
```html
include /etc/nginx/sites-enabled/*;
```

Проверяем корректность настройки:
```bash
sudo nginx -t
```

Перезагрузить nginx:
```bash
sudo systemctl restart nginx
```

Даем права доступа к домашней директории:
```bash
sudo chmod 755 /home/almas
```

Проверяем доступ на хост:
```bash
curl -H "Host: example.com" http://localhost:8080/images/flower.png
```
