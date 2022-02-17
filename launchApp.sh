#! /bin/sh

# To run this script, type ./launchApp.sh to run the script in the current directory

npm run build || { print "Error in npm run build"; exit 2; }
python3 app.py || { print "Error in app.py"; exit 2;}