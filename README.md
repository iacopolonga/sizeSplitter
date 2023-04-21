# sizeSplitter

sizeSplitter.py is a useful macro which helps in splitting a (long) list of files in N shorter lists, using the maximum disk occupancy as a criterion.  

It works with an arbitrary long list of files and/or folders (which are explored recursively). Symlinks are not followed.  

## Example usage, input files provided as command line arguments
```
pyhton3 sizeSplitter.py -i [COMMA OR SPACE SEPARATED INPUTS] -o my_list -s 2000 [MB]

[ COMMA OR SPACE SEPARATED INPUTS ] can be something like `find /path/to/my/dir/with/ntuples/ -type f -name "*.root" | tr "\n" " "`

will process inputs passed with -i and create files named
my_list_1.txt
my_list_2.txt
my_list_###.txt

each containing a list of files not larger than 2000 MB
```

## Example usage, input files listed in a txt file
This case is useful for when the list of input files is larger than the maximum number of arguments that can be passed to a command in your terminal.
```
pyhton3 sizeSplitter.py -t inputFile.txt -o my_list -s 2000 [MB]

where inputFile.txt contains the list of input files that has to be splitted (one per line)
```





