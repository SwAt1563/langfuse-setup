#!/bin/sh
# LF Format

# Check python requirements dependencies
echo "Checking python requirements dependencies..."
pip3 install -r requirements.txt


# Start the FastAPI server conditionally based on the environment file
echo "Starting FastAPI server..."
exec uvicorn main:app --host 0.0.0.0 --port 9000 --workers 2 --reload --loop uvloop --http httptools --ws auto --lifespan on # --reload: reload the server when code changes 

# Execute the command passed to the script
exec "$@"