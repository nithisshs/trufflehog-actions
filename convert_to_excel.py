import pandas as pd 
import os 
 
frame = pd.DataFrame() 
for filename in os.listdir(os.getcwd()): 
    root, ext = os.path.splitext(filename) 
    if ext == '.json': 
        tmp_frame = pd.read_json(filename) 
        frame = frame.append(tmp_frame, ignore_index=True) 
         
frame.to_csv('secret-scanner-results.csv', index=False) 
