
def write_to_file(file_path, content, mode='w'):
    with open(file_path, mode) as file:
        file.write(content+'\n')