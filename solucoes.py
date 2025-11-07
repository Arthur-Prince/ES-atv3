def sao_anagramas(string1, string2):
    x = [0] * len(string1)
    for i in range(len(string1)):
        found = False
        for j in range(len(string2)):
            if string1[i] == string2[j] and x[j] == 0:
                x[j] = 1
                found = True
                break
        if not found:
            return False
    return True

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
