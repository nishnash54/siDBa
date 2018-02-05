# Read CSV
from unicodecsv import DictReader

def read_csv(filename):
    try:
        with open(filename, 'rb') as f:
            reader = DictReader(f)
            csv_data = list(reader)
        return csv_data
    except:
        return "Missing file or filepath"

filename = "test_data/devfest2017.csv"
print read_csv(filename)[0]
