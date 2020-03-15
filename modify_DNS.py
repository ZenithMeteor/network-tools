








def read_data(input_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()
    return lines


def prune_list(lines):
    for line in lines:
        



DNS_path = ""



if __name__ == '__main__':

    _, filename = os.path.split(DNS_path)
    # bfn, ext = os.path.splitext(filename)
    # if ext.lower() not in ['.txt']:
        # continue
        
    DNS_list = read_data(DNS_path)
    input = raw_input()
    
    for line in DNS_list:
        splitted_line = line.strip().split(' ')
        if input == splitted_line[0]:
            print('find the same!!!')
            print('old data is ' + splitted_line[1])
    
    # backup
    with open( DNS_path.replace(filename, filename + "_bk", 1), "w") as f:
        f.writelines(DNS_list)
