import sys

def write_to_file(filename, tag):
    with open(filename, 'r') as input:
        lines= input.readlines()
    lines.insert(4, "tags: {0}\n".format(tag))
    with open (filename, 'w') as output:
        output.writelines(lines)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file_list:
        files = file_list.readlines()
    for file in files:
        write_to_file(file.strip(), 'algorithm')
