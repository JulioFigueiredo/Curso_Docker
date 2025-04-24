## Comando cd avançado

Para voltar ao último diretório:

```
cd -
```

Para voltar a raíz

```
cd /
```

Concatenar comandos (cd && ls)

```
cd nomedapasta && ls
```

## Comandos ls

Mostra a data da última modificação de cada arquivo

```
ls -ltr
```

## Comandos cat

Mostra o conteúdo dentro do arquivo

```
cat nomedoarquivo
```

Juntar dois arquivos em um só

```
cat teste teste2 > teste3
```

Ver número de linhas

```
cat -n teste
```

## Comandos touch

Muda a data da última alteração do arquivo

```
ls -ltr
touch teste.txt
ls -ltr
```
Também é possível criar um novo arquivo a partir do touch

```
touch nomedoarquivo
```