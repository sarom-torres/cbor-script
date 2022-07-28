import cbor2


# decodifica o arquivo CBOR
def decode_msg(filename):
    with open(filename, 'rb') as fp:
        return cbor2.load(fp)


def decode_list_msg():
    # diretório das mensagens cbor
    path_list_cbor = "msg_files/list/cbor/"

    # caminho do arquivo cbor a ser decodificado
    files_list_cbor = ['msg0.cbor', 'msg1.cbor', 'msg2.cbor']

    msg_decoded = list()
    # lê o arquivo CBOR e o apresenta em tela // tem que mostrar em tela qual o tipo de mensagem (list, )
    for msg in files_list_cbor:
        msg_decoded.append(decode_msg(path_list_cbor + msg))

    for msg in msg_decoded:
        if msg['opcode'] == 10:
            print("Mensagem de REQUISIÇÃO do comando LIST: \n", msg)
        elif msg['opcode'] == 11:
            print("\nMensagem de RESPOSTA de SUCESSO comando LIST: \n", msg)
        elif msg['opcode'] == 5:
            print("\nMensagem de RESPOSTA de ERRO do comando LIST: \n", msg)
        else:
            print("Mensagem inválida: \n", msg)


def decode_mkdir_msg():

    # diretório das mensagens cbor
    path_mkdir_cbor = "msg_files/mkdir/cbor/"

    # caminho do arquivo cbor a ser decodificado
    files_mkdir_cbor = ['msg0.cbor', 'msg1.cbor', 'msg2.cbor']

    msg_decoded = list()
    # lê o arquivo CBOR e o apresenta em tela // tem que mostrar em tela qual o tipo de mensagem (list, )
    for msg in files_mkdir_cbor:
        msg_decoded.append(decode_msg(path_mkdir_cbor + msg))

    for msg in msg_decoded:
        if msg['opcode'] == 12:
            print("Mensagem de REQUISIÇÃO do comando MKDIR: \n", msg)
        elif msg['opcode'] == 5 and msg['errorCode'] == 0:
            print("\nMensagem de RESPOSTA do SUCESSO comando MKDIR: \n", msg)
        elif msg['opcode'] == 5 and msg['errorCode'] != 0:
            print("\nMensagem de RESPOSTA de ERRO do comando MKDIR: \n", msg)
        else:
            print("\nMensagem inválida: \n", msg)

def decode_move_msg():

    # diretório das mensagens cbor
    path_move_cbor = "msg_files/move/cbor/"

    # caminho do arquivo cbor a ser decodificado
    files_move_cbor = ['msg0.cbor', 'msg1.cbor', 'msg2.cbor', 'msg3.cbor']

    msg_decoded = list()
    # lê o arquivo CBOR e o apresenta em tela // tem que mostrar em tela qual o tipo de mensagem (list, )
    for msg in files_move_cbor:
        msg_decoded.append(decode_msg(path_move_cbor + msg))

    for msg in msg_decoded:
        if msg['opcode'] == 13 and 'novo_nome' in msg:
            print("Mensagem de REQUISIÇÃO para copiar arquivo. Comando MOVE: \n", msg)
        elif msg['opcode'] == 13:
            print("\nMensagem de REQUISIÇÃO para deletar arquivo. Comando MOVE: \n", msg)
        elif msg['opcode'] == 5 and msg['errorCode'] == 0:
            print("\nMensagem de RESPOSTA de SUCESSO do comando MOVE: \n", msg)
        elif msg['opcode'] == 5:
            print("\nMensagem de RESPOSTA de ERRO do comando MKDIR: \n", msg)
        else:
            print("\nMensagem inválida: \n", msg)


if __name__ == '__main__':

    print("..............Mensagens do comando LIST..............\n")

    decode_list_msg()

    print("\n..............Mensagens do comando MKDIR..............\n")

    decode_mkdir_msg()

    print("\n..............Mensagens do comando MOVE..............\n")

    decode_move_msg()





