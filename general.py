import os


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


#  Create queue and crawled files
def create_data_files(project_name, data):
    queue = project_name
    if not os.path.isfile(queue):
        write_file(queue, data)



# Create a new file
def write_file(path, data):
    f = open(path, 'w')
#    f.write(data)
#    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(str(data) + '\n')


# Delete the content of a file
def delete_file_content(path):
    with open(path, 'w') as file:
        pass


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate throught a set, each item will be a new line in the file
def set_to_file(lista_prod, file):
    delete_file_content(file)
    for prod in lista_prod:
        append_to_file(file, lista_prod)

# Read a file and convert each line to set items
def file_to_list(file_name):
    results = []
#    with open(file_name, 'rt') as f:

    return results


# Iterate throught a set, each item will be a new line in the file
def list_to_file(lista_prod, file):
    delete_file_content(file)
    for prod in lista_prod:
        append_to_file(file, lista_prod)


