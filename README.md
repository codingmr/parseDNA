# parseDNA
Parses a sequence of DNA code from .txt into chunk groups with associated target

## Expected output
[![Image from Gyazo](https://i.gyazo.com/d0d33f0d930c0881bf99b459827856a0.png)](https://gyazo.com/d0d33f0d930c0881bf99b459827856a0)

## Example usage
By default the script will run with a chunk size of 5, number of chunks as 3 and will look for a file name called "data1.txt"
```python parseDNA.py```

Short hand you can specify the chunk size and number of chunks.
```python parseDNA.py 10 3```

You can also specify the filename
```python parseDNA.py 7 5 C:\lever\documents\data.txt```
