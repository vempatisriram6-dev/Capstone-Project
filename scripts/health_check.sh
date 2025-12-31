#!/bin/bash

URL="http://localhost:80"
RETRIES=5
SLEEP=3

echo "Ì¥ç Checking container health at $URL"

for i in $(seq 1 $RETRIES); do
  if curl -fs $URL > /dev/null; then
    echo "‚úÖ Frontend is healthy"
    exit 0
  fi

  echo "‚è≥ Attempt $i failed. Retrying in $SLEEP seconds..."
  sleep $SLEEP
done

echo "‚ùå Frontend health check failed"
exit 1



