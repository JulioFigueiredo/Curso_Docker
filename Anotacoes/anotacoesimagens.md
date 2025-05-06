## Criando uma imagem

### Necessário:
- Arquivo Dockerfile
- Instruções: FROM(imagem base), WORKDIR(diretório), EXPOSE(porta), COPY(quais arquivos precisam ser copiados)

## Rodando a imagem em um container (build)

Entrar no diretório onde está o Dockerfile, rodar:
```
docker build .
```

## Para listar imagens

```
docker images
```

## Para fazer download de imagens
```
docker pull nome
```

## Para nomear imagens (já criada)
```
docker tag <tag> nome
```
## Para atribuir uma tag (já criada)
```
docker tag <tag> nome:nometag
```

## Para criar imagem com nome
```
docker build -t teste .
```

## Para criar imagem com nome e tag
```
docker build -t nometeste:tagteste .
```

## Para remover imagens 
```
docker rmi <nome ou id>
```

## Para criar a imagem para subir no dockerHub

```
docker build -t username/nomerepositorio .
```

## Para subir pro hub

```
docker push username/nomerepositorio
```

## Para puxar do hub

```
docker pull username/nomerepositorio
```

## Atualizar imagem no hub

```
docker build -t juliooamorim/nodeteste:novaversao .
```