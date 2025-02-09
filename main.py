#!/usr/bin/python3
import os 


class terminal_cor():

    erro = '\033[31m'
    verde = '\033[32m'
    padrao = '\033[0m'




def menu():

    print(f'\n{'*' * 8} GERENCIADOR DE TAREFAS {'*' * 8}\n')
    print('1. Adicionar tarefa.')
    print('2. Ver minhas tarefas.')
    print('3. Marcar tarefa como concluida.')
    print('4. Excluir tarefa.')
    print('5. Sair.')

    escolha_menu = str(input('\nInforme o que você deseja fazer: [1, 2, 3, 4, 5] ')).strip()

    if escolha_menu.isdigit():

        if escolha_menu == '1':
            limpar_terminal()
            adicionar_tarefa()

        elif escolha_menu == '2':
            limpar_terminal()
            ver_tarefas()

        elif escolha_menu == '3':
            limpar_terminal()
            tarefas_concluidas()
            
        elif escolha_menu == '4':
            limpar_terminal()
            excluir_tarefa()

        elif escolha_menu == '5':
            print(terminal_cor.verde + '\nObrigado por utilizar o nosso programa. Volte sempre!\n' + terminal_cor.padrao)
            excluir_arquivo()
            exit()    

        else:
            limpar_terminal()
            print(terminal_cor.erro + '\nOpção inválida. Escolha uma opção válida para prosseguir.' + terminal_cor.padrao)

    else:
        limpar_terminal()
        print(terminal_cor.erro + '\nValor inválido. É necessario insirir um valor numerico para prosseguir.' + terminal_cor.padrao)




def adicionar_tarefa():

    while True:
        tarefa = str(input('\nDigite a tarefa que você deseja realizar: ')).strip()

        #Verificar se o usuario inseriu um input vazio
        if tarefa.strip() == '':
            limpar_terminal()
            print(terminal_cor.erro +'\nNão é possivel criar uma tarefa "vazia". Tente novamente. ' + terminal_cor.padrao)
        
        
        else: 
            # Se o arquivo ja existir, sera apenas inserido uma nova tarefa no arquivo ja existente. Caso contrario, o arquivo sera criado
            if os.path.exists('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt'):

                with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='a') as arquivo:
                    arquivo.write('☐ ' + tarefa + '\n')
                    limpar_terminal()
                    print(terminal_cor.verde + '\nTarefa adicionda com sucesso!' + terminal_cor.padrao)
                    break
                menu()

            else:
                with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='w') as arquivo:
                    #Adicionando a tarefa no arquivo:
                    with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='r+') as arquivo:
                        arquivo.write('☐ ' + tarefa + '\n')
                        limpar_terminal()
                        print(terminal_cor.verde + '\nTarefa adicionda com sucesso!' + terminal_cor.padrao)
                        break
                    menu()
            



def ver_tarefas():

    print('\nSuas tarefas:\n')

    with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='r') as arquivo:

        conteudo_arquivo = arquivo.read()
        print(conteudo_arquivo)


    while True:
        voltar_menu = str(input('\nDigite s para voltar para o menu principal ou n para sair do programa: [s/n] ')).strip().lower()

        if voltar_menu in ('s', 'n'):

            if voltar_menu == 's':
                limpar_terminal()
                menu()

            else:
                print(terminal_cor.verde + '\nObrigado por utilizar o nosso programa. Volte sempre!\n' + terminal_cor.padrao)
                excluir_arquivo()
                exit()
        else:
            limpar_terminal()
            print(terminal_cor.erro + '\nOpção inválida. Por favor, insira uma opção válida para prosseguir.' + terminal_cor.padrao)




def tarefas_concluidas():

    with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='r') as arquivo:

        conteudo_arquivo = arquivo.read()
        print(conteudo_arquivo)

    try:
        while True:
            tarefa_concluida = str(input('\nDeseja marcar alguma tarefa como completa? [s/n] ')).strip().lower()

            if tarefa_concluida == 's':
                escolha_tarefa = str(input('\nInsira o numero da linha onde a tarefa que você deseja marcar como concluida se encontra: ')).strip()

                if escolha_tarefa.isdigit():
                    escolha_tarefa = int(escolha_tarefa)
                    break

            elif tarefa_concluida == 'n':
                print(terminal_cor.verde + '\nObrigado por utilizar o nosso programa. Volte sempre!\n' + terminal_cor.padrao)
                exit()
            
            else:
                limpar_terminal()
                print(terminal_cor.erro + '\nOpção inválida. Insira uma opção válida para prosseguir.' + terminal_cor.padrao)

    except ValueError:
        print(terminal_cor.erro + '\nInsira um valor numerico para prosseguir.' + terminal_cor.padrao)


    while True:

        with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='r+') as arquivo:

            conteudo_arquivo = arquivo.readlines()
            # Verificando se a linha que o usuario deseja acessar está presente no arquivo:
            if 1 <= escolha_tarefa <= len(conteudo_arquivo):
                
                # Verificando se a tarefa ja foi marcada como concluida
                if '✔' in conteudo_arquivo[escolha_tarefa - 1]:
                    print(terminal_cor.erro + '\nEssa tarefa já foi marcada como concluida antes. Tente outra tarefa.' + terminal_cor.padrao)
                    break

                else:
                
                    #Modificando a linha para colocar o efeito de concluido
                    conteudo_arquivo[escolha_tarefa - 1] = conteudo_arquivo[escolha_tarefa - 1].strip() + ' ✔ \n'

                    # Volta para o inicio do arquivo para reescrever
                    arquivo.seek(0)

                    # Reescreve o arquivo com as alterações
                    arquivo.writelines(conteudo_arquivo)

                    limpar_terminal()
                    print(terminal_cor.verde + '\nTarefa marcada como concluída!' + terminal_cor.padrao)
                    break

            else:
                print(terminal_cor.erro + '\nNumero de linha inválido.' + terminal_cor.padrao)
               



def excluir_tarefa():

    print('\nSuas tarefas:\n')

    with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='r') as arquivo:

        conteudo_arquivo = arquivo.read()
        print(conteudo_arquivo)

    try:
        while True:
            excluir_tarefa = str(input('\nInsira o numero da linha onde a tarefa que você deseja excluir se encontra: ')).strip()
            
            if excluir_tarefa.isdigit():
                excluir_tarefa = int(excluir_tarefa)
                break
            else:
                print(terminal_cor.erro + '\nInsira um valor numerico para prosseguir.' + terminal_cor.padrao)

    except ValueError:
        print(terminal_cor.erro + '\nValor inválido. Insira apenas valores numericos para prosseguir.' + terminal_cor.padrao)
        

    with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='r') as arquivo:
        
            linhas = arquivo.readlines()

            # Validando se a linha que o usario digitou esta presente no arquivo:
            if 1 <= excluir_tarefa <= len(linhas):
                # Remove a linha escolhida comecando com indice 1
                del linhas[excluir_tarefa - 1]
                print(terminal_cor.verde + '\nTarefa excluida com sucesso!' + terminal_cor.padrao)
            
            else:
                print(terminal_cor.erro + '\nNão foi possivel excluir a tarefa. Verifique se o numero da linha da tarefa está correto.' + terminal_cor.padrao)
        
    # Salvando as alterações no arquivo
    with open('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt', mode='w') as arquivo:

        arquivo.writelines(linhas)
        


def excluir_arquivo():

    if os.path.exists('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt'):
        os.remove('/home/samuka/Área de Trabalho/Projetos_Python/Gerenciador_Tarefas/teste.txt')
    



def limpar_terminal():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




if __name__ == '__main__':

    while True:
        menu()
