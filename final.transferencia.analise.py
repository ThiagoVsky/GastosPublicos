
# coding: utf-8

# # Aplicativo que realiza conversão dos dados do CSV em SQL
# ## Criado por Thiago da Silva Moraes

# In[3]:


# PRINCIPAL
# Deve ser executado após iniciadas as funções

import os
try:
    os.mkdir('.\\output') # Cria a pasta de saída dos dados analizados
    print('Folder output created for finished files')
except:
    print('Folder output already exists')
    
# Abre os arquivos que serão utilizados
#filer = open('brutos\\GastosDiretos.csv') # leitura
#filew = open('output\\GastosDiretos.txt','w') # Escrita
#fileb = open('brutos\\GastosDiretos.csv') # Leitura para contador

filer = open('TransferenciastT.csv') # leitura
filew = open('output\\testeTranf.txt','w') # Escrita
fileb = open('TransferenciastT.csv') # Leitura para contador


# Executa a função principal que converte dados do CSV em linguagem SQL
transferenciaPublica()


# In[4]:


# DEVE SER EXECUTADA POR ÚLTIMO
# fecha os arquivos que foram abertos para análise

filer.close()
filew.close()
fileb.close()


# In[1]:


# FUNÇÕES PRINCIPAIS

# Inicializa a função que permite realizar a contagem de elementos totais a serem analizados.
def contador(file):
    abc = 0
    asd = 0
    for row2 in file:
        asd = row2.split('\t')
        for a in asd:
            abc+=1
    return abc

# Função principal da conversão dos dados do CSV em linguagem SQL
def transferenciaPublica():
    anoInd = '2018'
    mesInd = '01'
    # Inicializaçõa de variáveis:
    #counted = contador(fileb) # Conta a quantidade total de itens e armazena
    dataPgto = 0 # Armazena a última data de pagamento para inserção na função
    counter = 0 # Contador que permite checar em qual parte do procedimento o programa está
    idEstado = '' # Armazena o último ID do Órgão Superior para poder inserir na tabela como chave estrangeira
    idMunicípio = '' # Armazena o último ID do Órgão Subordinado para poder inserir na tabela como chave estrangeira
    idFuncao = '' # Armazena o último ID da Função para poder inserir na tabela como chave estrangeira
    idValorPago = 10000000 # Armazena o valor pago e posteriormente acrecenta a cada rodada para criação de ID
    idPrograma = '' # Armazena o último ID do Programa para poder inserir na tabela como chave estrangeira
    idSubFuncao = '' # Armazena o último ID da Subfunção para poder inserir na tabela como chave estrangeira
    t1 = [] # Armazena todos os dados do estado que já foram analizados para evitar inserções duplas
    t2 = [] # Armazena todos os dados do município Subordinado que já foram analizados para evitar inserções duplas
    t3 = [] # Armazena todos os dados da Função que já foram analizados para evitar inserções duplas
    t4 = [] # Armazena todos os dados da Subfunção que já foram analizados para evitar inserções duplas
    t5 = [] # Armazena todos os dados do Programa que já foram analizados para evitar inserções duplas
    
    for row in filer: # início da aplicação: para cada linha dentro do arquivo
        rowArr = row.split('\t') # Cria um vetor separando por cada tabulação na linha
        i = 1 # Define o contador do próximo loop
        for value in rowArr: # Para cada valor dentro do Vetor da Linha
            counter += 1 # Contador geral começa a rodar
            if i == 1: # Se contador i for 1
                estado = qualEstado(value)
                idEstado = idDoEstado(value)
                if value not in t1: # Se valor não tiver sido gravado antes
                    t1.append(value) # Registra a gravação do valor
                    filew.write("INSERT INTO estado (idEstado, nomeEstado, SUFEstado) VALUES (")
                    filew.write(str(idEstado))
                    filew.write(", '")
                    filew.write(estado+"', '")
                    filew.write(value+"');\n")
            elif i == 2 or i == 3: # Se contador for 2
                if value not in t2: # Se valor não tiver sido gravado antes
                    if i == 2: # Se for 3 grava o valor com sintaxe MySQL no arquivo
                        t2.append(value) # Registra a gravação do valor
                        idMunicípio = value
                        filew.write("INSERT INTO municipio (idMunicipio, nomeMunicipio, idEstado) ")
                        filew.write("VALUES (")
                        filew.write(value)
                        filew.write(", '")
                    elif i == 3: # Se for 4 grava o valor com sintaxe MySQL no arquivo
                        nomeMun = value.replace("'","\\'")
                        filew.write(nomeMun)
                        filew.write("', ")
                        filew.write(idEstado)
                        filew.write(");\n")
            elif i == 4 or i == 5:
                if value not in t3:
                    t3.append(value)
                    if i == 4:
                        idFuncao = value
                        filew.write("INSERT INTO funcao (idFuncao, nomeFuncao) VALUES (")
                        filew.write(value)
                        filew.write(", '")
                    elif i == 5:
                        filew.write(value)
                        filew.write("');\n")
            elif i == 6 or i == 7:
                if value not in t4:
                    t4.append(value)
                    if i == 6:
                        filew.write("INSERT INTO subfuncao (idSubFuncao, nomeSubFuncao) VALUES (")
                        filew.write(value)
                        filew.write(", '")
                        idSubFuncao = value
                    elif i == 7:
                        filew.write(value)
                        filew.write("');\n")
                        
                        filew.write("INSERT INTO subfuncao_funcao (idSubFuncao, idFuncao) VALUES (")
                        filew.write(idSubFuncao)
                        filew.write(", ")
                        filew.write(idFuncao)
                        filew.write(");\n")
            elif i == 8 or 9:
                if value not in t5:
                    t5.append(value)
                    if i == 8:
                        filew.write("INSERT INTO programa (idPrograma, nomePrograma) VALUES (")
                        filew.write(value)
                        filew.write(", '")
                        idPrograma = value
                    elif i == 9:
                        filew.write(value)
                        filew.write("');\n")
                        
                        filew.write("INSERT INTO subfuncao_programa (idSubFuncao, idPrograma) VALUES (")
                        filew.write(idSubFuncao)
                        filew.write(", ")
                        filew.write(idPrograma)
                        filew.write(");\n")
            
            dataPgto = anoInd+'-'+mesInd+'-01'
            if i == 18: # Se i for 18
                filew.write("INSERT INTO valorpago (datapagamento, valor, idValorPago) VALUES ('")
                filew.write(dataPgto)
                filew.write("', ")
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

                idValorPago += 1 # Incrementa o ID. No arquivo o ID não é fornecido,
                                 # criamos aqui apenas para inserção no banco.
            i+=1
        #print(counter,'/',counted) # Imprime a quantidade atual que já foram analizadas e a quantidade total
    #tempw.write()
    print('finished')


# In[2]:


# Função que testa qual estado pertence à sigla indicada
def qualEstado(estado:str):
    estado = estado.upper()
    if estado == 'AC':
        return 'Acre'
    elif estado == 'AL':
        return 'Alagoas'
    elif estado == 'AP':
        return 'Amapá'
    elif estado == 'AM':
        return 'Amazonas'
    elif estado == 'BA':
        return 'Bahia'
    elif estado == 'CE':
        return 'Ceará'
    elif estado == 'DF':
        return 'Distrito Federal'
    elif estado == 'ES':
        return 'Espírito Santo'
    elif estado == 'GO':
        return 'Goiás'
    elif estado == 'MA':
        return 'Maranhão'
    elif estado == 'MT':
        return 'Mato Grosso'
    elif estado == 'MS':
        return 'Mato Grosso do Sul'
    elif estado == 'MG':
        return 'Minas Gerais'
    elif estado == 'PA':
        return 'Pará'
    elif estado == 'PB':
        return 'Paraíba'
    elif estado == 'PR':
        return 'Paraná'
    elif estado == 'PE':
        return 'Pernambuco'
    elif estado == 'PI':
        return 'Piauí'
    elif estado == 'RJ':
        return 'Rio de Janeiro'
    elif estado == 'RN':
        return 'Rio Grande do Norte'
    elif estado == 'RS':
        return 'Rio Grande do Sul'
    elif estado == 'RO':
        return 'Rondônia'
    elif estado == 'RR':
        return 'Roraima'
    elif estado == 'SC':
        return 'Santa Catarina'
    elif estado == 'SP':
        return 'São Paulo'
    elif estado == 'SE':
        return 'Sergipe'
    elif estado == 'TO':
        return 'Tocantins'
    else:
        return 'NE'
    
    ###
    
# Função que testa qual idEstado pertence à sigla indicada
def idDoEstado(estado:str):
    estado = estado.upper()
    if estado == 'AC':
        return '01'
    elif estado == 'AL':
        return '02'
    elif estado == 'AP':
        return '03'
    elif estado == 'AM':
        return '04'
    elif estado == 'BA':
        return '05'
    elif estado == 'CE':
        return '06'
    elif estado == 'DF':
        return '07'
    elif estado == 'ES':
        return '08'
    elif estado == 'GO':
        return '09'
    elif estado == 'MA':
        return '10'
    elif estado == 'MT':
        return '11'
    elif estado == 'MS':
        return '12'
    elif estado == 'MG':
        return '13'
    elif estado == 'PA':
        return '14'
    elif estado == 'PB':
        return '15'
    elif estado == 'PR':
        return '16'
    elif estado == 'PE':
        return '17'
    elif estado == 'PI':
        return '18'
    elif estado == 'RJ':
        return '19'
    elif estado == 'RN':
        return '20'
    elif estado == 'RS':
        return '21'
    elif estado == 'RO':
        return '22'
    elif estado == 'RR':
        return '23'
    elif estado == 'SC':
        return '24'
    elif estado == 'SP':
        return '25'
    elif estado == 'SE':
        return '26'
    elif estado == 'TO':
        return '27'
    else:
        return '00'
    
    ###

