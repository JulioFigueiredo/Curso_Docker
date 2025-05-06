## Para criar um volume anônimo:

Flag -v

```
docker run -d -p 80:80 --name php_messages_container --rm -v /data phpmessages
```

## Listar volumes

```
docker volume ls
```

## Para criar um volume nomeado:

```
docker run -v nomedovolume:/data
docker run -d -p 80:80 --name php_messages_container -v phpvolume:/var/www/html/messages --rm phpmessages
```