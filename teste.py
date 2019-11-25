#Escreva um programa na sua linguagem e bibliotecas preferidas que:
#Leia a expressão (que pode ser uma frase ou apenas uma palavra) a ser usada para a criação 
# dos anagramas da linha de comando. Apenas as letras de “A” a
#  “Z” deverão ser consideradas 
# (ignore espaços e converta todas as letras minúsculas para maíusculas). Retorne erro e aborte a execução se caracteres inválidos forem encontrados na expressão (qualquer caracter não alfabético que não seja espaço, incluindo números, pontuação, ou caracteres acentuados).
#Leia uma lista de palavras válidas do arquivo palavras.txt (Download). O arquivo é formatado com uma palavra por linha, com palavras da língua inglesa (Nota: apesar de várias tentativas, o autor não conseguiu achar uma lista “limpa” de palavras da língua portuguesa).
#Imprima todas as combinações possíveis de anagramas (sem repetição de linhas ou palavras). Os anagramas devem conter apenas palavras válidas (lidas do arquivo acima).
from random import shuffle

def shuffle_word(word):
    word = list(word)
   shuffle(word)
    return ''.join(word)