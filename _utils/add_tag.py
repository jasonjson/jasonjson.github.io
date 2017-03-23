 #!/Users/yuanyuanliu/miniconda3/bin/python
import sys

def write_to_file(filename, tag):
    with open(filename, 'r') as input:
        lines= input.readlines()
    del lines[4]
    lines.insert(4, "tags:\n")
    lines.insert(5, "- " + tag + "\n")
    with open (filename, 'w') as output:
        output.writelines(lines)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file_list:
        files = file_list.readlines()
    for file in files:
        write_to_file(file.strip(), 'Algorithm')
