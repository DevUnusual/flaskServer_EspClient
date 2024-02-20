def readData():
    database = []
    with open('base.txt', 'r') as f:
        data = f.readlines()
        data = [i.replace('\n', '') for i in data]
        for d in data:
            frag = d.strip().split(' ')
            database.append([int(frag[0]),frag[1],int(frag[2])])
    return database