#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    import uncurl

# def remove_chars(str, chars):
#     fs = str
#     for char in chars:
#         fs = fs.replace(char, '')

#     return str

@atheris.instrument_func
def fuzzUncurlParse(input_data):
    query_str = ""
    
    # ensure errors are not from just missing args

    fdp = atheris.FuzzedDataProvider(input_data)
    data = fdp.ConsumeString(fdp.remaining_bytes())
    replace = ['-', '"', "'", " ", "\n", "`"]
    b = False
    for c in replace:
        if c in data:
            b = True

    if b:
        pass
    else:
        query_str = "curl \'https://" + data + "\'"
        uncurl.parse(query_str)

def main():
    
    atheris.Setup(sys.argv, fuzzUncurlParse)
    atheris.Fuzz()
    
if __name__ == "__main__":
    main()
