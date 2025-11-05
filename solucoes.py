def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass


def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            deslocamento_real = (ord(char) - base + deslocamento) % 26
            char_cifrado = chr(deslocamento_real + base)
            resultado += char_cifrado
        else:
            resultado += char
    
    return resultado


def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
