# Read CSV
from unicodecsv import DictReader

def read_csv(filename):
    try:
        with open(filename, 'rb') as f:
            reader = DictReader(f)
            csv_data = list(reader)
        return {"code": 200, "data": csv_data}
    except:
        return {"code": 400, "msg": "Missing file or filepath"}
