#!/bin/bash

#redis installeren
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
make test

#paswoord aanmaken
redis-cli
AUTH PASSWORD
CONFIG SET requirepass "p@ss"
AUTH p@ss

#redis installeren voor python
pip install redis