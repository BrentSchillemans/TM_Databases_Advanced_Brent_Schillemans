#!/bin/bash

#mongo installeren
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

#mongo starten
sudo systemctl start mongod
sudo systemctl status mongod
sudo systemctl enable mongod

#nieuwe gebruiker aanmaken
use admin
db.createUser(
    {
        user: "superuser",
        pwd: "p@ss",
        roles: ["root"]
    }
)
show users

#sluiten
exit