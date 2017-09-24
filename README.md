# mjai Server in Docker

[mjai](http://gimite.net/pukiwiki/index.php?Mjai%20%E9%BA%BB%E9%9B%80AI%E5%AF%BE%E6%88%A6%E3%82%B5%E3%83%BC%E3%83%90) is a server for Japanese mahjong AI. This repository contains [a forked version of mjai](https://github.com/mahjong-server/mahjong-server) that the most popular battleground for Japanese mahjong AI, [floodgate for mahjong](http://mjai.hocha.org/) uses.

## Getting Started

Below are tested on Docker CE `17.06.1-ce` on Ubuntu 14.04 trusty.

```bash
$ docker build -t mjai-server .
$ docker run -p 11600 --name mjai -itd mjai-server 
```

You can pull the latest image from Docker Hub instead of building the image locally. 

```bash
$ docker run -p 11600 --name mjai -itd geduld/mjai-server
```
Confirm the server is working.

```bash
$ docker ps
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                      NAMES
58302d58122g        geduld/mjai-server:latest   "/bin/sh -c 'ruby ..."   1 minutes ago       Up 2 minutes        0.0.0.0:32768->11600/tcp   mjai

$ curl localhost:32768
{"type":"hello","protocol":"mjsonp","protocol_version":1}
{"type":"error","message":"invalid join"}
```

Also run examples to understand how this works. [Docker Compose](https://docs.docker.com/compose/) needs to be installed. It takes approximately 5 minutes to start the game.

```bash
$ cd exmaples/
$ docker-compose up 
```

## Documents

### Abount mjai

* [Protocols](docs/protocols.md)

### About Mahjong(Riichi mahjong, Japanese mahjong)

* You can find basic rule [here](http://mahjong-europe.org/) - European Mahjong Association
* [Tiles](docs/tiles.md)
* [Yaku](docs/yaku.md)
* [Scoring tables](docs/scoring_tables.md)
