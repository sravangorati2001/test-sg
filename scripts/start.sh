#!/bin/bash

# Move to the application directory
cd /var/www/html/your-app

# Activate the virtual environment
source venv/bin/activate

# Start the application (example with Flask)
nohup python app.py > app.log 2>&1 &
