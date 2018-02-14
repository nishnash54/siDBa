from read_csv import read_csv
from database_connection import connection, update_database

if __name__ == "__main__":
    filename = raw_input('Enter filename (with path): ').strip()
    db_link = raw_input('Enter database link : ').strip()
    database_name = raw_input('Enter database name : ').strip()
    collection_name = raw_input('Enter collection name : ').strip()
    
