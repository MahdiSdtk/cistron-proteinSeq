import numpy as np
import json
import csv
import pathlib
import colorama



def simpleError():
    print(f'{colorama.Fore.RED}\nsomething went wrong.\n')


def transcript(sequence):
    sequence = sequence.strip()
    sequence = sequence.uppercase()
    sequence = sequence.replace('A', '1')
    if sequence.find('T') is True: sequence = sequence.replace('T', '2')
    else: sequence = sequence.replace('U', '2')
    sequence = sequence.replace('C', '3')
    sequence = sequence.replace('G', '4')
    sequence = sequence.replace('1', 'U')
    sequence = sequence.replace('2', 'A')
    sequence = sequence.replace('3', 'G')
    sequence = sequence.replace('4', 'C')
    print(sequence)
    #  incomplete numbers to mRNA


with open('pro-letter.json', mode='r', encoding='utf8') as file:
    file = file.read()
    pro_letter = json.loads(file)  # 3 letter protein to letter dict

while(True):
    lst = np.array([])  #  what is this for?:o
    input1 = input('\ninput a cistron sequence.\n1)from a file\n2)enter it as a text\n3)locate the root folder\n')
    if input1 == '1':  # seq from  file input (could be a txt, fasta or ...)
        print('locate the intended sequence')
        seq_loc = pathlib.Path(input(': '))

        try:
            with open(seq_loc, mode='r', encoding='utf8') as file:
                file = file.read()
                # incomplete sequence2str
        # incomplete seq str to mRNA then protein
        except:
            simpleError()
            continue
    elif input1 == '2':  #  seq from text input
        # incomplete protein seq from text input
        pass
    elif input1 == '3':
        print('enter the root folder location')
        root_folder = pathlib.Path(input(': ')) # 'data' folder
        data_set = root_folder/'dataset_catalog.json' # contains the file names
        with open(data_set, mode='r') as file:
            data_set = file.read()
        data_setdic = json.loads(data_set)
        data_set_paths = {} # file paths
        for i in range(len(data_setdic['genes']['files'])):
            data_set_paths[data_setdic['genes']['files'][i]['fileType']] = data_setdic['genes']['files'][i]['filePath']
        # analyse each file (directories stored in data_set_paths)
        gene_file_path = root_folder/data_set_paths[data_setdic['genes']['files'][0]['fileType']]
        # store the content of each file in a dictionary with file names as the keys
        with open(gene_file_path) as file:
            gene_file = file.read()
        try:
            print(root_folder)
            print(data_set_paths)
            print(gene_file)
            pass
            #with open()
            # incomplete root folder access
        except:
            simpleError()
            continue
    else:
        simpleError()
        continue
