import json
import cbor2

path_command_list = "msgFiles/List/"


def read_from_file(filename):
    with open(filename, 'rb') as fp:
        return fp.read()


def read_from_json(filename):
    with open(filename,'r') as json_file:
        return json.load(json_file)


def encode_msg(filemane, output):
    obj = read_from_json(filemane)
    with open(output, 'wb') as fp:
        cbor2.dump(obj, fp)


if __name__ == '__main__':

    # caminho do arquivo json contendo a mensagem
    filename = path_command_list +'json/msg0.json'

    # caminho do arquivo cbor
    output = path_command_list+'cbor/msg0.cbor'

    # codifica a mensagem em CBOR
    encode_msg(filename, output)

    # lê o arquivo CBOR e o apresenta em tela
    cbor_data = read_from_file(output)
    print("Arquivo serializado: \n ", cbor_data)

    # decodifica o arquivo CBOR e apresenta em tela
    with open(path_command_list+'cbor/msg0.cbor', 'rb') as fp:
        data = cbor2.load(fp)
        print("Arquivo desserializado: \n ", data)


