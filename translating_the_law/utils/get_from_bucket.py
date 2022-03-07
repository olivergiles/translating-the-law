from google.cloud import storage
import json
import gcsfs
import pandas as pd

def open_from_bucket():
    gcs_file_system = gcsfs.GCSFileSystem()
    gcs_json_path = "gs://law-data-ogiles/data/simplified_data.json"
    with gcs_file_system.open(gcs_json_path) as f:
        json_dict = json.load(f)
    return eval(json_dict)
#    data = pd.read_json(gcs_json_path)
#    return data

if __name__ == "__main__":
    print(open_from_bucket()[0])