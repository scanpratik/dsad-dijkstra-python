def read_input_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.isspace():
            continue
        if line.strip().startswith("Hospital"):
            print(line)
        elif line.strip().startswith("Airport"):
            print(line)
        else:
            print(line)


read_input_file("inputPS6.txt")
