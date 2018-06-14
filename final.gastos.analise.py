
# coding: utf-8

# # Aplicativo que realiza conversão dos dados do CSV em SQL
# ## Criado por Thiago da Silva Moraes

# In[ ]:





# In[ ]:


# FUNÇÕES PRINCIPAIS

# Inicializa a função que permite realizar a contagem de elementos totais a serem analizados.
#def contador(file):
 #   abc = 0
  #  asd = 0
   # for row2 in file:
    #    asd = row2.split('\t')
     #   for a in asd:
      #      abc+=1
   # return abc

# Função principal da conversão dos dados do CSV em linguagem SQL
def gastosPublicos():
    # Inicializaçõa de variáveis:
    #counted = contador(fileb) # Conta a quantidade total de itens e armazena
    dataPgto = 0 # Armazena a última data de pagamento para inserção na função
    counter = 0 # Contador que permite checar em qual parte do procedimento o programa está
    idOrgaoSuperior = '' # Armazena o último ID do Órgão Superior para poder inserir na tabela como chave estrangeira
    idOrgaoSubordinado = '' # Armazena o último ID do Órgão Subordinado para poder inserir na tabela como chave estrangeira
    idFuncao = '' # Armazena o último ID da Função para poder inserir na tabela como chave estrangeira
    idValorPago = 0 # Armazena o valor pago e posteriormente acrecenta a cada rodada para criação de ID
    idPrograma = '' # Armazena o último ID do Programa para poder inserir na tabela como chave estrangeira
    idSubFuncao = '' # Armazena o último ID da Subfunção para poder inserir na tabela como chave estrangeira
    t1 = [] # Armazena todos os dados do Órgão Superior que já foram analizados para evitar inserções duplas
    t2 = [] # Armazena todos os dados do Órgão Subordinado que já foram analizados para evitar inserções duplas
    t3 = [] # Armazena todos os dados da Função que já foram analizados para evitar inserções duplas
    t4 = [] # Armazena todos os dados da Subfunção que já foram analizados para evitar inserções duplas
    t5 = [] # Armazena todos os dados do Programa que já foram analizados para evitar inserções duplas
    
    for row in filer: # início da aplicação: para cada linha dentro do arquivo
        rowArr = row.split('\t') # Cria um vetor separando por cada tabulação na linha
        i = 1 # Define o contador do próximo loop
        for value in rowArr: # Para cada valor dentro do Vetor da Linha
            counter += 1 # Contador começa a rodar
            if i == 1 or i == 2: # Se contador for 1 ou 2
                if value not in t1: # Se valor não tiver sido gravado antes
                    t1.append(value) # Registra a gravação do valor
                    if i == 1: # Se for 1 grava o valor com sintaxe MySQL no arquivo
                        idOrgaoSuperior = value
                        filew.write("INSERT INTO orgaosuperior (idOrgaoSuperior, nomeOrgaoSuperior) VALUES (")
                        filew.write(value)
                        filew.write(", '")

                    elif i == 2: # Se for 2 grava o valor com sintaxe MySQL no arquivo
                        filew.write(value)
                        filew.write("');\n")
            elif i == 3 or i == 4: # Se contador for 3 ou 4
                if value not in t2: # Se valor não tiver sido gravado antes
                    t2.append(value) # Registra a gravação do valor
                    if i == 3: # Se for 3 grava o valor com sintaxe MySQL no arquivo
                        idOrgaoSubordinado = value
                        filew.write("INSERT INTO orgaosubordinado (idOrgaoSubordinado, nomeOrgaoSubordinado, idOrgaoSuperior) ")
                        filew.write("VALUES (")
                        filew.write(value)
                        filew.write(", '")
                    elif i == 4: # Se for 4 grava o valor com sintaxe MySQL no arquivo
                        filew.write(value)
                        filew.write("', ")
                        filew.write(idOrgaoSuperior)
                        filew.write(");\n")
            elif i == 11 or i == 12:
                if value not in t3:
                    t3.append(value)
                    if i == 11:
                        idFuncao = value
                        filew.write("INSERT INTO funcao (idFuncao, nomeFuncao) VALUES (")
                        filew.write(value)
                        filew.write(", '")
                    elif i == 12:
                        filew.write(value)
                        filew.write("');\n")

                        filew.write("INSERT INTO orgaosubordinado_funcao (idOrgaoSubordinado, idFuncao) VALUES (")
                        filew.write(idOrgaoSubordinado)
                        filew.write(", ")
                        filew.write(idFuncao)
                        filew.write(");\n")
            elif i == 13 or i == 14:
                if value not in t4:
                    t4.append(value)
                    if i == 13:
                        filew.write("INSERT INTO subfuncao (idSubFuncao, nomeSubFuncao) VALUES (")
                        filew.write(value)
                        filew.write(", '")
                        idSubFuncao = value
                    elif i == 14:
                        filew.write(value)
                        filew.write("');\n")
                        
                        filew.write("INSERT INTO subfuncao_funcao (idSubFuncao, idFuncao) VALUES (")
                        filew.write(idSubFuncao)
                        filew.write(", ")
                        filew.write(idFuncao)
                        filew.write(");\n")
            elif i == 15 or 16:
                if value not in t5:
                    t5.append(value)
                    if i == 15:
                        filew.write("INSERT INTO programa (idPrograma, nomePrograma) VALUES (")
                        filew.write(value)
                        filew.write(", '")
                        idPrograma = value
                    elif i == 16:
                        filew.write(value)
                        filew.write("');\n")
                        
                        filew.write("INSERT INTO subfuncao_programa (idSubFuncao, idPrograma) VALUES (")
                        filew.write(idSubFuncao)
                        filew.write(", ")
                        filew.write(idPrograma)
                        filew.write(");\n")
            
            if i == 24 or i == 25:
                if i == 24:
                    dataPgto = substitoi(value) # Data de pagamento passa por uma função para colocá-la no formato adequado
                if dataPgto != False: # Se o valor não for uma data, retornará falso e o valor não será registrado
                    # Há várias inserções no arquivo que suas datas foram classificadas como sigilosas e não possuem o
                    # formato de data, e sim de texto. Por isso a criação do IF anterior
                    if i == 24: # Se i for 24
                        filew.write("INSERT INTO valorpago (datapagamento, valor, idValorPago) VALUES ('")
                        filew.write(substitoi(value))
                        filew.write("', ")
                    if i == 25: # Se i for 25, o valor a ser gravado deve ser o valor pago
                        done = value.strip() # Por ser o último da linha do CSV vem com um catactér de quebra de linha
                        # Esse o motivo da função anterior
                        idV = str(idValorPago) # O id do valor pago deve ser uma string para a inserção no arquivo final
                        filew.write(done.replace(',','.')) 
                        filew.write(", ")
                        filew.write(idV) # Grava o ID
                        filew.write(");\n")

                        filew.write("INSERT INTO programa_valorpago (idPrograma, idValorPago) VALUES(")
                        filew.write(idPrograma)
                        filew.write(", ")
                        filew.write(idV)
                        filew.write(");\n")

                        idValorPago += 1 # Incrementa o ID. No arquivo o ID não é fornecido
                                         # criamos aqui apenas para inserção no banco.
            i+=1
        print(counter,'/',counted) # Imprime a quantidade atual que já foram analizadas e a quantidade total
    #tempw.write()


# In[ ]:


# Função que substitui o valor de data comum DD/MM/AAAA por AAAA-MM-DD aceito pelo MySQL
# Também detecta se o valor inserido não é uma data no formato acima.

def substitoi(valor:str):
    try: # Tente...
        data = valor.split('/') # Dividir a string por barra e armazenar
        cont = 1 # Contador inicia
        dia = '' # Cria 3 strings
        mes = ''
        ano = ''
        for i in data: # para cada i em data
            if cont == 1:
                dia = str(int(i)) # Armazene o dia. Aqui se o valor não for um número, gerará um erro
            elif cont == 2:
                mes = i # Armazene o mês
            elif cont == 3:
                ano = i # Armazene o ano
            cont+=1
        return ano + '-' + mes + '-'+ dia # Retorne a data no formato aceito
    except: # Se o erro acontecer...
        return False # Retorne falso.
    # PRINCIPAL

import os
try:
    os.mkdir('.\\output') # Cria a pasta de saída dos dados analizados
    print('Folder output created for finished files')
except:
    print('Folder output already exists')
    
# Abre os arquivos que serão utilizados
input('Hello, this is the wizard to convert "gastos" files from CSV to SQL (enter to continue)')
filer = open(input('file to be read')) # leitura
filew = open('output\\'+input('choose a name for file to be written'),'w') # Escrita
#fileb = open('GastosDiretostT.csv') # Leitura para contador


# Executa a função principal que converte dados do CSV em linguagem SQL
gastosPublicos()


# In[ ]:


# DEVE SER EXECUTADA POR ÚLTIMO
# fecha os arquivos que foram abertos para análise

filer.close()
filew.close()
#fileb.close()
input('finished successfully. Press enter to end')