
import glob # permite leer contenido de directorios
import fileinput # permite iterar y operar en archivos 


def load_input(input_directory):
    sequence=[] # lista vacia 
    filenames = glob.glob(input_directory + "/*") # lee el contenido del directorio

    with fileinput.input (files=(filenames)) as f: # abre los archivos y con el with cierra los archivos
        for line in f:
            sequence.append((fileinput.filename(),line))# concatena el nombre del archivo y su linea correspondiente en una tupla

    return sequence

def mapper(sequence):
    new_sequence=[] # lista vacia
    for _, text in sequence: # raya el piso sirve para que deje el ultimo valor de la dupla 
        words=text.split() # separa las palabras y quedan alojadas  en una lista 
        for word in words:
            word=word.replace(",","")
            word=word.replace(".","")
            word=word.lower()
            new_sequence.append((word,1))# aloja la dupla en una lista, en este caso la palabra y el numero 1
    return new_sequence


def shuffle_and_sort(sequence):
    sorted_sequence=sorted(sequence, key=lambda x: x[0])
    return sorted_sequence


def reducer(sequence):
    diccionario={}
    for key,value in sequence:
        if key not in diccionario.keys():
            diccionario[key]=0
        diccionario[key]+=value
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key,value)
        new_sequence.append(tupla)
    return new_sequence
        

import os.path

def create_output_directory(output_directory):
    
    if os.path.exists(output_directory):
        raise FileExistsError(f"The directory '{output_directory} 'alredy exists.")
    os.makedirs(output_directory)


def save_output(output_directory, sequence):
    with open(output_directory + "/part-00000", "w") as file:
        for key, value in sequence:
            file.write(f"{key}\t{value}\n")
   

def create_market(output_directory):
    with open(output_directory + "/_SUCCESS","w") as file:
        file.write("")


def job(input_directory, output_directory):
    
    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_output_directory(output_directory)
    save_output(output_directory, sequence)
    create_market(output_directory)

if __name__ == "__main__":
    job(
        "input",
        "output",
    )
