import re
import os 
from brainExtraction import extractSlicesandBoundaries

DIR_PATH = './testPatient/'
OUTPUT_PATH = './'
filenames = os.listdir(DIR_PATH)
final_names = [i for i in filenames if re.search("(thresh.(?:jpg|gif|png))", i)]

for f in final_names:
    f = f[:len(f)-4]
    os.makedirs(OUTPUT_PATH+'Slices/'+f)
    os.makedirs(OUTPUT_PATH+'Boundaries/'+f)
extractSlicesandBoundaries(final_names)
