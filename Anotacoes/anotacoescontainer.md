## Rodar um hello world simples no cmd

```
docker run hello-world
```

## Para encontrar imagens

hub.docker.com

## Para rodar um container interativo (continua rodando)

```
docker run -it ubuntu
```

## Para verificar os container que estão sendo executados no momento

```
docker ps
```

## Para verificar todos os containeres já executados na máquina

```
docker ps -a
```

## Para rodar container em background (datached)

```
docker run -d nginx
```

## Para expor uma porta de um container
(antes do : é a porta do pc e depois a do container)

```
docker run -d -p 80:80 nginx
```

## Para parar um container 

```
docker stop <id ou nome>
```

## Para reiniciar um container (que já foi iniciado antes)

```
docker start <id>
```

## Como atribuir nome a um container

```
docker run -d -p 80:80 --name nginx_app nginx
```

## Para verificar logs

```
docker logs nginx_app
```

## Para remover um container

```
docker rm <id>
```

## Inspecionar container

```
docker inspect <id>
```

## Autenticação no terminal

```
docker login
```

## Encerrar autenticação

```
docker logout
```