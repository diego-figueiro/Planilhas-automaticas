import openpyxl

# Criando Planilha
book = openpyxl.Workbook()

# Criando a Página
book.create_sheet('computadores')

# Selecionando a página
pagina = book['computadores']

# Inserindo o nome das colunas via .append usando uma lista
pagina.append(['Eletrônica', 'memória ram', 'preço'])

# Inserindo Dados
pagina.append(['Computador 1', '8gb Ram', 'R$2500'])
pagina.append(['Computador 2', '16gb Ram', 'R$5500'])
pagina.append(['Computador 3', '32gb Ram', 'R$8500'])
# Salvando Planilha
book.save('C:\\Users\\diego.figueiro\\Desktop\\diegorepo\\Planilhas Automáticas\\meus computadores.xlsx')