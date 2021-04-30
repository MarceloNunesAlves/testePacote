Criação do projeto 01

```
docker build --file=DockerProj1 -t mna/proj01:latest .
```

Criação do projeto 02

```
docker build --file=DockerProj2 -t mna/proj02:latest .
```

Executando

```
docker run -d --name=pro1 mna/proj01:latest
docker run -d --name=pro2 mna/proj02:latest
```