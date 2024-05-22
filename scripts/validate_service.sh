#!/bin/bash

# Check if the application is running
if ! pgrep -f "python train.py"; then
  echo "Application is not running!"
  exit 1
fi
