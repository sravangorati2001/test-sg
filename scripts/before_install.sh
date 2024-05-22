#!/bin/bash

# Stop the current application if running
if pgrep -f "python app.py"; then
  pkill -f "python app.py"
fi

# Create the application directory if it doesn't exist
sudo mkdir -p /var/www/html/your-app
sudo chown -R ec2-user:ec2-user /var/www/html/your-app
