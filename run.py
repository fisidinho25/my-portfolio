#!/usr/bin/env python
import os
import sys
# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app
if __name__ == '__main__':
    print("Starting Flask Portfolio App...")
    print("Visit: http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)