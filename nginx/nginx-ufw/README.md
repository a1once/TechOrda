# nginx-ufw

На вашем сервере может быть запущено несколько сервисов помимо nginx. Оставлять доступ к ним открытым из Интернета может быть очень опасно.
Злоумышленники могут этим воспользоваться и взломать один из открытых сервисов.

Для безопасности, нужно закрыть к ним доступы и оставить только доступ к веб-серверу nginx. Одним из способов это сделать является команда `ufw`.

На данном уроке, мы научимся как обезопасить свой сервер.

### Полезные ссылки

- [UFW - Uncomplicated Firewall](https://help.ubuntu.com/community/UFW)
- [Hello Linux: Nginx & UFW Firewall](https://www.codingforentrepreneurs.com/blog/hello-linux-nginx-and-ufw-firewall)

### Задание

1. На своем компьютере запустите nginx. Скачайте `ufw` и настройте доступ извне только на порты 80 и 443.
2. Отправьте выполненные команды.

---

### Ответ
Выполняем следующие команды для установки ufw:
```bash
sudo apt update
sudo apt install ufw
```

Включаем ufw и добавляем правила:
```bash
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw default deny incoming
sudo ufw default allow outgoing
```
Проверяем статус:
```bash
sudo ufw status
```
Результат:
```html
Status: active

To                         Action      From
--                         ------      ----
8080/tcp                   ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
443/tcp                    ALLOW       Anywhere                  
8080/tcp (v6)              ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
443/tcp (v6)               ALLOW       Anywhere (v6)
```
