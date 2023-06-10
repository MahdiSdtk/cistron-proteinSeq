import numpy as np
import json
import colorama


def simpleError():
    print(f'{colorama.Fore.RED}\nsomething went wrong.\n')


def transcript(sequence):
    sequence = sequence.uppercase()
    sequence = sequence.replace('A', '1')
    sequence = sequence.replace('T', '2')
    sequence = sequence.replace('U', '2')
    sequence = sequence.replace('C', '3')
    sequence = sequence.replace('G', '4')
    print(sequence)
    #  incomplete numbers to mRNA


with open('pro-letter.json', mode='r', encoding='utf8') as file:
    file = file.read()
    pro_letter = json.loads(file)  # 3 letter protein to letter dict

while(True):
    lst = np.array([])  #  what is this for?:o
    input1 = input('\ninput a cistron sequence.\n1)from a file\n2)enter it as a text\n')
    if input1 == 1:  # seq from  file input (could be a txt, fasta or ...)
        print('allocate the intended sequence')
        file_loc = input(': ')
        try:
            with open(file_loc, mode='r', encoding='utf8') as file:
                file = file.read()
                # incomplete sequence2str
        # incomplete seq str to mRNA then protein
        except:
            simpleError()
            continue
    elif input1 == 2:  #  seq from text input
        # incomplete protein seq from text input
        pass
    else:
        simpleError()
        continue
