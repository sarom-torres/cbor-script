## Encoder

O script `Encoder` codifica as mensagens extras do protocolo TFTP2 de um arquivo JSON utilizando CBOR.

As mensagens **json** estão em `msg_files/[nome_do_comando]/json`. Após a codificação elas são armazenadas em 
`msg_files/[nome_do_comando]/cbor`.

Execução:

```
$ python3 encoder.py
```

## Decoder

O script `Decoder` decodifica as mensagens codificadas em CBOR do protocolo TFTP2.

As mensagens **cbor** estão em `msg_files/[nome_do_comando]/cbor`. 

Execução:

```
$ python3 decoder.py
```