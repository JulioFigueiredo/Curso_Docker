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