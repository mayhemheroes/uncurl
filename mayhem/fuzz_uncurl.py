#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    import uncurl

def remove_chars(str, chars):
    fs = str
    for char in chars:
        fs = fs.replace(char, '')

    print("final str: " + fs)
    return str

@atheris.instrument_func
def test_input(input_data):
    # query_str = ""
    
    # ensure errors are not from just missing args
    fdp = atheris.FuzzedDataProvider(input_data)
    data = fdp.ConsumeString(4096)
    replace = ['-', '"', "'", " ", "\n", "`"]
    b = False
    for c in replace:
        if c in data:
            b = True

    if b:
        pass
    else:
        # try:
        query_str = "curl https://" + data
        uncurl.parse(query_str)
        # except SystemExit:
        #     print(data)

    return

def main():
    try:
        atheris.Setup(sys.argv, test_input)
        atheris.Fuzz()
    except:
        pass

if __name__ == "__main__":
    main()
