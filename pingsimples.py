import os #Importar o modulo ou biblioteca OS (Integra os programas e recursos do S.O)

print("#" * 60) ##Imprimindo "#" 60 vezes

ip_ou_host = input("Digite o Ip ou Host a ser verificado:  ")#Criamos uma variavel que vai receber do
# usuario um ip

print("-" * 60)##Imprimindo "-" 60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host))#Chamando system da biblioteca os - comando ping -n -num
#de pacotes que serao 6 {}

print("-" * 60)##Imprimindo "-" 60 vezes