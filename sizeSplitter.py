
from __future__ import print_function
from __future__ import division

import argparse
import time
import sys
import os
import ROOT
import re
from array import array
import numpy as np

def getOptions(args=sys.argv[1:]):
    ###  Argument parser ###
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i","--input", nargs="+", help="Input files, expects either comma-separated or space-separated (or both)", type=str, required=True)
    parser.add_argument("-o","--output", help="Your destination output file.", type=str, required=True)
    parser.add_argument("-s","--size",help="Threshold of file size (MB)" ,type=float, default=2000)
    options = parser.parse_args(args)
    return options

def get_size(path):
    total_size = 0
    if not os.path.exists(path):
        print("Found non-existing file or path")
        print(path)
        exit(1)
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)

                if os.path.islink(fp):
                    continue

                total_size += os.path.getsize(fp)
    elif os.path.isfile(path):
        total_size += os.path.getsize(path)
                
    return total_size / (1E06) #MB


def writefile(filename, n, lines):
    name = "{}_{}.txt".format(filename,n)
    print(" Writing file ", n, name)
    with open(name,"w") as f:
        for line in lines:
            f.write(line + "\n")

if __name__ == "__main__":
    options = getOptions(sys.argv[1:])
    
    ### Collect input files
    inputFilesList = []

    if options.input:
        for inputFile in options.input:
            if ("," in inputFile ):
                for inputFileItr in inputFile.split(","):
                    inputFilesList.append(inputFileItr)
            else:
                inputFilesList.append(inputFile)
    
    ### Define output
    outFileName = options.output
    sizeThr = options.size
        
    inputFilesProcessed = []
    totalSize = 0
    nSplit = 0
    for inputFile in inputFilesList:
        thisSize = get_size(inputFile)

        ### If it's a single large file
        if thisSize > sizeThr:
            nSplit += 1
            writefile(outFileName, nSplit, [inputFile])

        else:
            ### If size will exceed threshold
            if thisSize + totalSize > sizeThr:
                ### First dump collected files
                nSplit += 1
                writefile(outFileName, nSplit, inputFilesProcessed)
                inputFilesProcessed = []
                totalSize = 0
                
            totalSize += thisSize
            inputFilesProcessed.append(inputFile)
        
    ### Check if missing some files
    if len(inputFilesProcessed) > 1:
        nSplit += 1
        writefile(outFileName, nSplit, inputFilesProcessed)
