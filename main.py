from read_csv import read_csv
from database_connection import update_database
from Tkinter import *

def create_collection():

    filename = blank1.get()
    db_link = blank2.get()
    database_name = blank3.get()
    collection_name = blank4.get()

    file_data = read_csv(filename)
    if file_data["code"] == 400:
        print file_data["msg"]
    else:
        file_data = file_data["data"]
        # print file_data[:2]
        msg = update_database(db_link, database_name, collection_name, file_data)
        if msg["code"] == 400:
            print msg["msg"]
        else:
            print "Done", msg["msg"]
            blank1.delete(0, 'end')
            blank2.delete(0, 'end')
            blank3.delete(0, 'end')
            blank4.delete(0, 'end')

if __name__ == "__main__":
    # filename = raw_input('Enter filename (with path): ').strip()
    # db_link = raw_input('Enter database link : ').strip()
    # database_name = raw_input('Enter database name : ').strip()
    # collection_name = raw_input('Enter collection name : ').strip()
    # mongodb://gdgvit:gdgvit@ds133557.mlab.com:33557/subconn
    main = Tk()
    main.resizable(0, 0)
    fnt = (None, 20)
    Label(main, text="Filename", font=fnt).grid(row=0)
    Label(main, text="Database link", font=fnt).grid(row=1)
    Label(main, text="Database name", font=fnt).grid(row=2)
    Label(main, text="Collection name", font=fnt).grid(row=3)
    blank1 = Entry(main, font=fnt)
    blank1.grid(row=0, column=1)
    blank2 = Entry(main, font=fnt)
    blank2.grid(row=1, column=1)
    blank3 = Entry(main, font=fnt)
    blank3.grid(row=2, column=1)
    blank4 = Entry(main, font=fnt)
    blank4.grid(row=3, column=1)
    Button(main, text='Quit', bg='red', font=fnt, command=main.destroy).\
    grid(row=4, column=0, sticky=W, pady=4)
    Button(main, text='Create',bg='green', font=fnt, command=create_collection).\
    grid(row=4, column=1, sticky=W, pady=4)
    mainloop()
