import os,sys
from pathlib import Path
import json
import ast
output={'employees':[]}
def read_files(inp_files,merged_file,s):
    max_size=s
    key=""
    for i in inp_files:
        d = json.load(open(i))
        size=json.dumps(d)
        #print(len(size))
        
        for i in d:
            key=i
            obj=d[i]
            for o in obj:
                #print(o)
                #x=json.dumps(o)
                #print(x)
                str_size=len(json.dumps(o).encode('utf-8'))
                
                output["employees"].append(o)
    print("the contents to be merged are going to be saved as:")
    print(output)
    print("\n")
    with open('merged_file.json', 'w') as json_file:
        l=len(json.dumps(output))
        print("Size of the merged_data:")
        print(l)
        if l>max_size:
            print("ERROR..!!Merged data size larger than maximum size given.Cannot dump into json file...")
        else:
            json.dump(output, json_file,indent=4)
            print("Merge successful..!!Saved in merged_file.json")
    
    
        
        #jdata = ast.literal_eval(json.dumps(output))
                
        #json.dump(jdata, json_file)

def merge_files(fpath,inp,merged_file,size):
    files=os.listdir(fpath)
    inp_files=[]
    for f in files:
        if f.startswith(inp) and f.endswith('.json'):
            inp_files.append(f)
    print("The input files are:")
    print(inp_files)
    print("\n")

    inp_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    read_files(inp_files,merged_file,size)


merge_files("C:\\Users\\rkbha\\OneDrive\\Desktop\\merge_json_files","data","merged_file",1024)
