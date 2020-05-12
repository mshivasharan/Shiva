with open("data.txt", "a+") as mydata:
    mydata.seek(0)
    content = mydata.read()
    mydata.seek(0)
    mydata.write(content)
    mydata.seek(0)
    mydata.write(content)
