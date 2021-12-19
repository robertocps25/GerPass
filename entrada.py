#receber nome do ambiente
#receber login do ambiente
#receber senha do ambiente
import time
from os import listdir
from os.path import isfile

def mostrarDados(ambiente, login, senha):
    print(ambiente)
    print(login)
    print(senha)

def pegarDados():
    ambiente = input("Digite o ambiente: \n")
    login = input("Digite o login: \n")
    senha = input("Digite a senha: \n")
    mostrarDados(ambiente, login, senha)
    salvar(ambiente, login, senha)
    
def salvar(ambiente, login, senha):
    with open(ambiente + '.txt', 'w') as arquivo:
        arquivo.write(login + "\n")
        arquivo.write(senha)
        print("Dados salvos com sucesso, a aplicação está reiniciando")
    menu()
        

def menu():
    print("-------------------------------[MENU]-------------------------------")
    escolha = int(input("[1] - Cadastrar senha\n[2] - Ler senha \n"))
    if escolha == 1:
        pegarDados()
    elif escolha == 2:
        mostrarAmbientes()
    else:
        print("Não existe está opção.")
        menu()
def mostrarAmbientes():
    index = 0
    for a in listdir():
        if isfile(a) and '.txt' in a:
            print('[' + str(index) + '] - ' + a.replace('.txt', ''))
            index += 1

    escolha = int(input("Digite o ambiente desejado "))
    mostrarSenha(escolha)

def mostrarSenha(escolha):
    index = 0
    linhas = []
    for a in listdir():
        if isfile(a) and '.txt' in a:        
            if index == escolha:
                with open(a, 'r') as arquivo:
                    linhas = arquivo.readlines()
                    print("Login: " + linhas[0])
                    print("Senha: " + linhas[1] + "\n") 
                    time.sleep(3)
            index += 1
    menu()

menu()      