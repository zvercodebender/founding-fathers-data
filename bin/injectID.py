#!/usr/bin/python3 

import json
import uuid
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        if inputfile == '' :
            print( "Please define an input file")
            sys.exit(2)

        with open(inputfile) as json_data:
            d = json.load(json_data)
            json_data.close()
            idx=0
            for recObj in d:
                recObj['id'] = str(uuid.uuid4())
                idx = idx + 1

            json_string = json.dumps(d, indent=4)
            if outputfile != '':
                with open( outputfile, 'w') as json_file:
                    json_file.write(json_string) 
            else:
                print(json_string)


if __name__ == "__main__":
   main(sys.argv[1:])

