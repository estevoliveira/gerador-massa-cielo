import random
import csv


class Usuario():
    EC =""
    nome ="teste"
    mail="teste@gmail.com.br"
    dataNascimento="1994-11-25"
    CPF=""
    agencia=""
    contaCorrente=""
    serialPrePago=""
    usuario="teste"

    def __init__(self,EC,CPF,agencia,contaCorrente,serialPrePago):
        self.EC = EC
        self.CPF = CPF
        self.agencia = agencia
        self.contaCorrente = contaCorrente
        self.serialPrePago=serialPrePago

def gerarMassa():
    tipo = ['pre-pago','domicilio']
    lista_usuario=[]
    numeroCpf=1
    print(len(lista_usuario))

    arquivo_cpf = open('C:\\Users\\estevao.oliveira\\Documents\\robo_geraMassa_multicanalidade\\cpf_20k_multicanalidade.csv')
    lista_cpf= list(csv.reader(arquivo_cpf))
    print(lista_cpf[numeroCpf])

    arquivo_pre_pago = open('C:\\Users\\estevao.oliveira\\Documents\\robo_geraMassa_multicanalidade\\ECs_pre_pago.csv')
    lista_pre_pago = csv.DictReader(arquivo_pre_pago)

    arquivo_domicilio=open('C:\\Users\\estevao.oliveira\\Documents\\robo_geraMassa_multicanalidade\\Usuarios_Stress_Test_validos.csv')
    lista_domicilio=csv.DictReader(arquivo_domicilio)
        
    for pre_pago in lista_pre_pago:
        if(numeroCpf<(len(lista_cpf)/2)):
            lista_usuario.append(Usuario(str(pre_pago['companyId']),str(lista_cpf[numeroCpf][0]),"","",str(pre_pago['companyDocument'])))
            numeroCpf+=1
        else:
            break
    
    for domicilio in lista_domicilio:
        if(numeroCpf<=len(lista_cpf)):
            lista_usuario.append(Usuario(str(domicilio['EC']),str(lista_cpf[numeroCpf][0]),str(domicilio['agencia']),str(domicilio['contaCorrente']),""))
            numeroCpf+=1
        else:
            break

    nova_massa = open('C:\\Users\\estevao.oliveira\\Documents\\robo_geraMassa_multicanalidade\\nova_massa.csv','a')
    nova_massa.write('EC;CPF;usuario;mail;nome;dataNascimento;agencia;contaCorrente;serialPrePago\n')

    while(len(lista_usuario)>0):
        aleatorio = random.randint(0,(len(lista_usuario)-1))
        nova_massa.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (lista_usuario[aleatorio].EC,lista_usuario[aleatorio].CPF,lista_usuario[aleatorio].usuario,
            lista_usuario[aleatorio].mail,lista_usuario[aleatorio].nome,lista_usuario[aleatorio].dataNascimento,lista_usuario[aleatorio].agencia,
            lista_usuario[aleatorio].contaCorrente,lista_usuario[aleatorio].serialPrePago))
        lista_usuario.pop(aleatorio)


gerarMassa()

def teste():
    lista=[1,2,3,4,5,6]
    
    while(len(lista)>0):
        print(len(lista))
        x= random.randint(0,(len(lista)-1))
        print('numero da sorte: %s' % x)
        lista.pop(x)

#teste()