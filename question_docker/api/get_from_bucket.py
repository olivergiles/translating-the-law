import json
import gcsfs
import re

def cleaner(text, **kwargs):
  """params is a list of things to remove: codec, acronyms, numbers, brackets, page, para, legal formatting """
  if not 'params' in kwargs:
    kwargs['params'] = ['codec', 'acronyms', 'numbers', 'brackets', 'page', 'para', 'legal formatting']
  if 'codec' in kwargs['params']:
    text_encoded = text.encode('ascii', errors = 'ignore')
    text_decode = text_encoded.decode()
    clean_text = " ".join([word for word in text_decode.split()])
    text = clean_text
  if 'numbers' in kwargs['params']:
    pattern = r'[0-9]'
    text = re.sub(pattern, '', text)
  if 'brackets' in kwargs['params']:
    text = re.sub('\(.*?\)', '', text)
    text = re.sub('\[.*?\]', '', text)
  if 'acronyms' in kwargs['params']:
    text = text.split()
    clean_text = []
    for word in text:
      if any(l.islower() for l in word):
        clean_text.append(word)
    text = ' '.join(clean_text)
  if 'page' in kwargs['params']:
      text = re.sub('Page [0-9]+', '', text)
  if 'para' in kwargs['params']:
      text = re.sub('Para [0-9]+', '', text)
  if 'legal formatting' in kwargs['params']:
      text = re.sub('Civ', '', text)
      text = re.sub('On appeal from:', '', text)
  return text

def open_from_bucket():
    gcs_file_system = gcsfs.GCSFileSystem()
    gcs_json_path = "gs://law-data-ogiles/data/simplified_data.json"
    with gcs_file_system.open(gcs_json_path) as f:
        json_dict = json.load(f)
    data = eval(json_dict)
    clean_data = [case for case in data if not case["press summary"].get('error')]
    clean_data = cleaner(clean_data)
    return clean_data