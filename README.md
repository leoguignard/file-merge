# Merging files

You can run the script the following way:
```shell
python merge.py -i path/to/file1.txt path/to/file2.txt path/to/file3.txt [...] -o path/to/out.txt
```

You can access help for it:
```shell
python merge.py --help
```

You can specify the default value when not found:
```shell
python merge.py -i path/to/file1.txt path/to/file2.txt path/to/file3.txt -o path/to/out.txt -d absent 0 -1
```
Here when the data is not found in file1 it will output `absent` when not in file2 it will output `0` and when not in file3 it will output `-1`.