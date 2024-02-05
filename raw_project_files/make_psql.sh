#!/bin/bash

DB_USER="postgres"
DB_NAME=""
DB_USER_PROJECT=""
DB_PASSWORD_PROJECT=""

CREATE_DB_CMD="CREATE DATABASE $DB_NAME;"
CREATE_USER_CMD="CREATE USER $DB_USER_PROJECT WITH PASSWORD '$DB_PASSWORD_PROJECT';"
GRANT_PRIVILEGES_CMD="GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER_PROJECT;"

sudo -u $DB_USER psql -c "$CREATE_DB_CMD"
sudo -u $DB_USER psql -c "$CREATE_USER_CMD"
sudo -u $DB_USER psql -c "$GRANT_PRIVILEGES_CMD"

if [ $? -eq 0 ]; then
  echo "База данных '$DB_NAME' и пользователь '$DB_USER_PROJECT' успешно созданы и настроены."
else
  echo "Ошибка при создании базы данных и пользователя."
fi
