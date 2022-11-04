def ler_credenciais():
    with open('conf.txt', 'r', encoding='utf-8') as arquivo:
        usuario, senha = arquivo.readlines()
    return usuario, senha