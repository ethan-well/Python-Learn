def read_file():
    with open('./test.txt') as file_object:
        for line in file_object:
            print(line.rstrip())

read_file()

def read_file2():
    with open('./test.txt') as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line)

read_file2()