import saveFile
datas = saveFile.datas


while True:
    dataUser = input('')

    if dataUser == "":
        print("bye...")
        break

    if dataUser == '\\train':
        while True:
            trainData = input('Nyam? > ')
            value = 0
            if trainData == '':
                break

            if ":" in trainData:
                value = trainData.split(':')[1]
                trainData = trainData.split(':')[0]

            if trainData not in datas:
                datas[trainData] = value
                print('Thanks :)')

            else:
                print(f'there is "{trainData}" in my brain :)')

    elif dataUser == '\\del':
        while True:
            dataToDel = input('your input? : ')

            if dataToDel == '':
                break

            if dataToDel in datas:
                del datas[dataToDel]

    elif dataUser == "\\save":
        dir = 'D:\Dev\Python\Codev2\AI\saveFile.py'
        with open(dir, 'w+') as f:
            f.write(f'datas = {datas}')

    elif dataUser == "\\data":
        for index, data in enumerate(datas.keys()):
            print(str(index + 1)+". "+data)

    else:
        print("------------------------------")
        print("RESULT : ")
        thereIs = False
        for data in datas:
            if str(data).startswith(dataUser):
                print("-"+data)
                thereIs = True

        if not thereIs:
            print("Result Not Found")
        print("------------------------------")


















