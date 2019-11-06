# merge_multiple_json_files
To merge multiple json files into a single json file

The merge function takes input the folder path, input file base prefix format, output filename and the maximum size.
It reads the input file names and stores them in a list and passes the input list, output filename and maximum size to read function
The read function loads the json files and stores them into a dictionary
Before dumping into the target json file, the dictionary size is checked. If it is larger than maximum size, it throws an error. Else the dictionary is dumped into the output json file.
This code reads in any format json object like the ones shown in data4.json file also.

