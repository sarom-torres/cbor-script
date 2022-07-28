import json
import cbor2

# diretório das mensagens do comando LIST
path_list_json = "msg_files/list/json/"
path_list_cbor = "msg_files/list/cbor/"

# diretório das mensagens do comando MKDIR
path_mkdir_json = "msg_files/mkdir/json/"
path_mkdir_cbor = "msg_files/mkdir/cbor/"

# diretório das mensagens do comando MKDIR
path_move_json = "msg_files/move/json/"
path_move_cbor = "msg_files/move/cbor/"


def read_from_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)


def encode_msg(filemane, output):
    obj = read_from_json(filemane)
    with open(output, 'wb') as fp:
        cbor2.dump(obj, fp)


if __name__ == '__main__':

    # caminho do arquivo json contendo a mensagem
    files_list_json = ['msg0.json', 'msg1.json', 'msg2.json']

    # caminho do arquivo cbor
    files_list_cbor =  ['msg0.cbor', 'msg1.cbor', 'msg2.cbor']

    print("===========Mensagens do comando LIST===========")

    # lê do arquivo json
    for msg in files_list_json:
        print(read_from_json(path_list_json + msg))

    print("Codificando mensagens utilizando CBOR...")

    # codifica a mensagem em CBOR
    i = 0
    for msg in files_list_json:
        encode_msg(path_list_json + msg, path_list_cbor + 'msg' + str(i) + '.cbor')
        i += 1

    print("Mensagens codificadas!")

    # -----------------------------------------------------------------------------------------|
    print("\n===========Mensagens do comando MKDIR===========")

    # caminho do arquivo json contendo a mensagem
    files_mkdir_json = ['msg0.json', 'msg1.json', 'msg2.json']

    # caminho do arquivo cbor
    files_mkdir_cbor = ['msg0.cbor', 'msg1.cbor', 'msg2.cbor']

    # lê do arquivo json
    for msg in files_mkdir_json:
        print(read_from_json(path_mkdir_json + msg))

    print("Codificando mensagens utilizando CBOR...")

    # codifica a mensagem em CBOR
    i = 0
    for msg in files_mkdir_json:
        encode_msg(path_mkdir_json + msg, path_mkdir_cbor + 'msg' + str(i) + '.cbor')
        i += 1
    print("Mensagens codificadas!")

    # -----------------------------------------------------------------------------------------|
    print("\n===========Mensagens do comando MOVE===========")

    # caminho do arquivo json contendo a mensagem
    files_move_json = ['msg0.json', 'msg1.json', 'msg2.json', 'msg3.json']

    # caminho do arquivo cbor
    files_move_cbor = ['msg0.cbor', 'msg1.cbor', 'msg2.cbor', 'msg3.cbor']

    # lê do arquivo json
    for msg in files_move_json:
        print(read_from_json(path_move_json + msg))

    print("Codificando mensagens utilizando CBOR...")

    # codifica a mensagem em CBOR
    i = 0
    for msg in files_move_json:
        encode_msg(path_move_json + msg, path_move_cbor + 'msg' + str(i) + '.cbor')
        i += 1
    print("Mensagens codificadas!")





