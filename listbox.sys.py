def fetchRecord():
    cont = sqlite3.connect('storagetest.db')
        with cont:
        cursort = cont.cursor()
        list_loadr = cursort.execute('''SELECT name FROM content''')
        list_load = list_loadr.fetchall()
        for item in list_load:
            list.insert(END, item)

        cont.commit()

