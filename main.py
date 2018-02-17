from read_csv import read_csv
from database_connection import update_database

if __name__ == "__main__":
    filename = raw_input('Enter filename (with path): ').strip()
    db_link = raw_input('Enter database link : ').strip()
    database_name = raw_input('Enter database name : ').strip()
    collection_name = raw_input('Enter collection name : ').strip()
    file_data = read_csv(filename)
    if file_data["code"] == 400:
        print file_data["msg"]
    else:
        file_data = file_data["data"]
        print file_data[:2]
        msg = update_database(db_link, database_name, collection_name, file_data)
        if msg["code"] == 400:
            print msg["msg"]
        else:
            print "Done", msg["msg"]
