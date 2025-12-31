#!/bin/bash

echo "Starting rollback..."

docker stop backend || true
docker rm backend || true

docker run -d \
  --name backend \
  -p 5000:5000 \
  vempatisriram2004/capstone-backend:previous

echo "Rollback completed successfully"
