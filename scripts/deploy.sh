
#!/bin/bash

# Move to the application directory
cd /var/www/html/your-app

# Set up the virtual environment
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
