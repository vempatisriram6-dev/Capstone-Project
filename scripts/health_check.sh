#!/bin/bash

URL="http://localhost:80"
RETRIES=5
SLEEP=3

echo " Checking container health at $URL"

for i in $(seq 1 $RETRIES); do
  if curl -fs $URL > /dev/null; then
    echo " Frontend is healthy"
    exit 0
  fi

  echo " Attempt $i failed. Retrying in $SLEEP seconds..."
  sleep $SLEEP
done

echo " Frontend health check failed"
exit 1



