#!/bin/bash

APP_NAME=frontend
BACKUP_IMAGE_FILE=/tmp/last_image.txt

if [ ! -f $BACKUP_IMAGE_FILE ]; then
  echo " No previous image found to rollback"
  exit 1
fi

PREVIOUS_IMAGE=$(cat $BACKUP_IMAGE_FILE)

echo " Rolling back to $PREVIOUS_IMAGE"

docker stop $APP_NAME || true
docker rm $APP_NAME || true

docker run -d \
  --name $APP_NAME \
  -p 80:80 \
  $PREVIOUS_IMAGE

echo " Rollback completed"




