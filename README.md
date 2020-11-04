# sizeSplitter

sizeSplitter.py is a useful macro when you need to split a list of files/directories according to file/directori sizes.

```
Usage:
pyhton3 sizeSplitter.py -i [COMMA OR SPACE SEPARATED INPUTS] -o my_list -s 2000 [MB]

will process inputs passed with -i and create files named
my_list_1.txt
my_list_2.txt
my_list_###.txt

each containing a list of files not larger than 2000 MB

```


