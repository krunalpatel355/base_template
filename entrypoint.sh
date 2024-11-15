#!/bin/bash
set -e

# Function to wait for MongoDB
wait_for_mongodb() {
    echo "Waiting for MongoDB to be ready..."
    timeout=60
    counter=0
    until mongo --host ${MONGO_HOST} --eval "print(\"waited for connection\")" >/dev/null 2>&1; do
        sleep 1
        counter=$((counter + 1))
        if [ $counter -ge $timeout ]; then
            echo "Failed to connect to MongoDB within $timeout seconds"
            exit 1
        fi
        echo "Still waiting for MongoDB... ($counter seconds)"
    done
    echo "MongoDB is ready!"
}

# Wait for MongoDB if MONGO_HOST is set
if [ ! -z "$MONGO_HOST" ]; then
    wait_for_mongodb
fi

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:5000 \
    --workers 4 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    wsgi:app