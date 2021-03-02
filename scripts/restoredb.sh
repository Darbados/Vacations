#!/usr/bin/env bash

set -x -e

sudo whoami
sudo mysql -u root -e "CREATE USER '`whoami`'; GRANT ALL PRIVILEGES ON *.* TO '`whoami`' WITH GRANT OPTION;"
mysql -e "DROP DATABASE IF EXISTS vacations; CREATE DATABASE vacations;"
  mysql -e "DROP USER IF EXISTS vacationsuser; CREATE USER vacationsuser IDENTIFIED BY 'dbpassword'; GRANT ALL PRIVILEGES ON vacations.* TO vacationsuser; GRANT ALL PRIVILEGES ON \`test_vacations%\`.* TO vacationsuser;"
