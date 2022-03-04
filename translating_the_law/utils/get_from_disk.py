import os
import json

def open_from_disk():
    base_path = os.path.dirname(os.path.realpath(__file__))
    open_path = os.path.join(base_path, "..","..", "raw_data", "data.json")
    with open(open_path, 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    return eval(obj)

if __name__ == "__main__":
    print("Running test")
    print(open_from_disk()[0])