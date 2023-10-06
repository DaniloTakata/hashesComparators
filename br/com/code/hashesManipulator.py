import os
import hashlib

# common_path = "C:\\Users\\danil\\OneDrive\\Área de Trabalho\\testeHash"

common_path = os.getcwd() + "\\filesManipulated"
words_file = []
hashes_file = []
founds = {}


# Função responsável por acessar o caminho onde está o código e encontrar os arquivos worlists e de hashes
def findFiles(file_path):
    for foundFile in os.listdir(common_path):
        if 'words' in foundFile:
            words_file.append(foundFile)
        else:
            hashes_file.append(foundFile)


# Função que recebe uma palavra e gera seu hash em md5
def createHash(word):
    return hashlib.md5(word.encode()).hexdigest()


# Função que compara uma palavra específica e uma hash específica
def compareDatas(wordc, hashc):
    if wordc == hashc:
        return True
    return False


# Função que percorre todos os arquivos encontrados e compara as palavras
def verifyDatas(words, hashes):
    for wordFile in words:
        word_file_path = common_path + "\\" + wordFile
        with open(word_file_path, 'r') as currentWordFile:
            words_content = currentWordFile.readlines()
            for currentworld in words_content:
                if '\n' in currentworld:
                    currentworld = currentworld[0:(len(currentworld) - 1)]
                currentworldhash = createHash(currentworld)
                for hashFile in hashes:
                    hash_file_path = common_path + "\\" + hashFile
                    with open(hash_file_path, 'r') as currentHashFile:
                        hash_content = currentHashFile.readlines()
                        for currentHash in hash_content:
                            if '\n' in currentHash:
                                currentHash = currentHash[0:(len(currentHash) - 1)]

                            if compareDatas(currentworldhash, currentHash):
                                founds[currentworld] = currentHash
                            else:
                                continue


# Cria um novo arquivo as palavras e suas respectivas hashes encontradas no processo, no formato palavra: hash
def createNewFile(dicts):
    newFileName = common_path + "\\hashesFounds.txt"
    with open(newFileName, 'w') as newFile:
        for chave, valor in dict(dicts).items():
            newFile.write(f"{chave}: {valor}\n")


"""
------------------------------------------------------------------------------------------------------------------------
"""

findFiles(common_path)
verifyDatas(words_file, hashes_file)
createNewFile(founds)

print(founds)
