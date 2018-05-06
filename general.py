import os

# Store crawled website temporarily in this directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project dir ' + directory)
        os.makedirs(directory)

# Create queue and crawled file
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Creating a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete content of file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# Read file and convert to sets
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result

# Convert set to file
def set_to_file(links, file_name):
    delete_file_contents(file_name)
    for link in links:
        append_to_file(file_name, link)
