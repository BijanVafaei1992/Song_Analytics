#!/bin/sh

# Use this shell script to execute the model. 


echo ###READING DATA AND MAKING THE ANSWERS READY###
python Model_run.py

echo ###NOW STARTING THE SERVER###
python server.py
echo SEND POST REQUEST TO http://localhost:5000/api/predict