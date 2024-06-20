import datetime
import openpyxl
from tabulate import tabulate

tarefas = []

def adicionar_tarefa():
    tarefa = input('Qual tarefa? ')
    descricao = input('Qual a descrição da tarefa? ')    
    while True:
        data = input('Qual a data máxima de realizar dessa tarefa? dd/mm/aaaa ')
        try:
            data_formatada = datetime.datetime.strptime(data, '%d/%m/%Y').date()
            if data_formatada >= datetime.date.today():
                break
            else:
                print('A data de vencimento deve ser maior do que a data de hoje.')
        except ValueError:
            print('Formato de data inválido. Digite a data no formato dd/mm/aaaa')
    while True:
        prioridade = input('Qual a prioridade dessa terefa? (baixa, media, alta) ')
        if prioridade.lower() in ('baixa', 'media', 'alta'):
            break
        else:
            print('Prioridade inválida. Digite: baixa, media ou alta')    
    dic = {'Titulo': tarefa, 'Descrição': descricao, 
           'Data de Vencimento': data_formatada, 'Prioridade': prioridade
           }
    tarefas.append(dic)
    print('Tarefa adicionada com sucesso!')

def listar_tarefas():
    tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: tarefa['Data de Vencimento'])
    
    tabela_tarefas = []
    for i, v in enumerate(tarefas_ordenadas):
        data_formatada = v['Data de Vencimento'].strftime('%d/%m/%Y')
        tabela_tarefas.append({
            'Índice': i,
            'Vencimento': data_formatada,
            'Tarefa': v['Titulo'],
            'Prioridade': v['Prioridade']            
        })
    print(tabulate(tabela_tarefas, headers='keys', tablefmt='grid'))
    
def editar_tarefas():
    if tarefas:
        listar_tarefas()   
        while True:
            try:
                indice = int(input('Qual o índice da tarefa que você deseja editar? '))
                if 0<= indice < len(tarefas):
                    tarefas[indice]['Descrição'] = input('Qual a nova descrição da tarefa? ')
                    while True:
                        tarefas[indice]['Prioridade'] = input('Qual a nova prioridade? (baixa, media, alta) ')
                        if tarefas[indice]['Prioridade'].lower() in ('baixa','media','alta'):   
                            print('Tarefa editada com sucesso!.')
                            break
                        else:
                            print('Prioridade inválida. Digite: baixa, media ou alta') 
                    break  
                else:
                    print('Índice não localizado.')
            except ValueError:
                print('Digite apenas números.')
    else:
        print('A lista está vazia')
            
def excluir_tarefas():
    if tarefas:
        listar_tarefas()
        while True:
            try:
                indice = int(input('Qual o índice da tarefa que você deseja remover? '))
                if 0 <= indice < len(tarefas):
                    tarefas.pop(indice)
                    print('Tarefa removida com sucesso')
                    break
                else:
                    print('Índice inválido. Tente novamente')
            except ValueError:
                print('Digite apenas números.')
    else:
        print('A lista está vazia')
        
def exportar_para_excel():
    if tarefas:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        
        worksheet['A1'] = 'Índice'
        worksheet['B1'] = 'Tarefa'
        worksheet['C1'] = 'Descrição'
        worksheet['D1'] = 'Data de Vencimento'
        worksheet['E1'] = 'Prioridade'
        
        row = 2
        for i, tarefa in enumerate(tarefas):
            worksheet[f'A{row}'] = i
            worksheet[f'B{row}'] = tarefa['Titulo']
            worksheet[f'C{row}'] = tarefa['Descrição']
            worksheet[f'D{row}'] = tarefa['Data de Vencimento'].strftime('%d/%m/%Y')
            worksheet[f'E{row}'] = tarefa['Prioridade']
            row +=1
            
        workbook.save('tarefas.xlsx')
        print('Tarefas exportadas para o arquivo com sucesso.')  
    else:
        print('A lista está vazia')          
        
while True:
    print("""
          =-=-=-=-=-=--=-=-=-=-=-=-=-=-=
          Sistema Gerenciador de Tarefas
          =-=-=-=-=-=--=-=-=-=-=-=-=-=-=
          
          [1] Adicionar Tarefas
          [2] Listar Tarefas
          [3] Editar Tarefas
          [4] Excluir Tarefas
          [5] Exportar para excel
          [6] Sair
          """)
    
    opc = int(input('Escolha uma opção: '))
    
    if opc == 1:
        adicionar_tarefa()
    elif opc == 2:
        listar_tarefas()
    elif opc == 3:
        editar_tarefas()
    elif opc == 4:
        excluir_tarefas()
    elif opc == 5:
        exportar_para_excel()
    elif opc == 6:
        break
    else:
        print('Opção inválida!.')