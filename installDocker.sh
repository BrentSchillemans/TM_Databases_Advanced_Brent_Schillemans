#!/bin/bash

#Mongo
docker pull mongo
docker run -p 8080:27017 --name mongoDocker mongo
docker exec -it mongoDocker mongosh

#Redis
docker pull redis
docker run -p 8081:6379 --name redisDocker redis
docker exec -it redisDocker redis-cli