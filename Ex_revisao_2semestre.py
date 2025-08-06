#Ex 01

def filtrar_filmes(filmes: list, filtro: str) -> list:
    filmes_filtrados = []

    for filme in filmes:
        if filme["Genero"] == filtro:
            filmes_filtrados.append(filme)

        elif filme["Ano"] == filtro:
            filmes_filtrados.append(filme)

    return filmes_filtrados

filmes = [
    {"Nome": "Onde os fracos não tem vez", "Genero": "Suspense", "Ano": "2006"},
    {"Nome": "Taxi Driver", "Genero": "Drama", "Ano": "1976"},
    {"Nome": "Forrest Gump", "Genero": "Drama", "Ano": "1994"},
    {"Nome": "Os Imperdoaveis", "Genero": "Western", "Ano": "1992"},
]

filmes_filtrados = filtrar_filmes(filmes, "Suspense")

print(filmes_filtrados)

#Ex 02

candidatos = [
    {"Nome": "João", "num_votos": 0},
    {"Nome": "Pedro", "num_votos": 0},
    {"Nome": "Vitor", "num_votos": 0},
]

while True:
    print("----Sistema de votação----")
    print("1 - Candidato João")
    print("2 - Candidato Pedro")
    print("3 - Candidato Vitor")
    print("4 - Sair")

    escolha = input("Digite o número do seu candidato para votar: ")

    match escolha:
        case "1":
            print("Você votou no João!")
            for candidato in candidatos:
                if candidato["Nome"] == "João":
                    candidato["num_votos"] += 1
                else:
                    pass

        case "2":
            print("Você votou no Pedro!")
            for candidato in candidatos:
                if candidato["Nome"] == "Pedro":
                    candidato["num_votos"] += 1
                else:
                    pass

        case "3":
            print("Você votou no Vitor!")
            for candidato in candidatos:
                if candidato["Nome"] == "Vitor":
                    candidato["num_votos"] += 1
                else:
                    pass
        case "4":
            break

print(candidatos)

#Ex 03

tarefas = [];

while True:
    print("----Organizador de Tarefas----")
    print('1 - Adicionar Tarefa')
    print('2 - Remover Tarefa')
    print('3 - Listar Tarefas')
    print('4 - Sair')

    escolha = input("Digite sua opção: ")

    match escolha:
        case "1":
            tarefa_titulo = input("Digite o título da sua tarefa: ")
            print("----Menu de prioridade----")
            print("1 - Alta")
            print("2 - Média")
            print("3 - Baixa")
            print("4 - Sem prioridade")

            prioridade_escolha = input("Digite sua opção: ")

            match prioridade_escolha:
                case "1":
                    tarefa_prioridade = "Alta"
                case '2':
                    tarefa_prioridade = "Média"
                case '3':
                    tarefa_prioridade = "Baixa"
                case _:
                    tarefa_prioridade = ""

            print("----Menu de conclusão----")
            print("1 - Foi concluida")
            print("2 - Não Foi concluida")

            conclusao_escolha = input("Digite sua opção: ")

            match conclusao_escolha:
                case "1":
                    tarefa_conclusao = "Concluida"
                case "2":
                    tarefa_conclusao = "Pendente"
                case _:
                    tarefa_conclusao = "Pendente"

            tarefa = {"Titulo": tarefa_titulo, "Prioridade": tarefa_prioridade, "Status": tarefa_conclusao}
            tarefas.append(tarefa)

        case "2":
            tarefa_deletar = input("Digite o nome da tarefa que deseja deletar: ")

            for tarefa in tarefas:
                if tarefa["Titulo"] == tarefa_deletar:
                    tarefas.remove(tarefa)
                    print("Tarefa deletada com sucesso")

        case "3":
            print("----Todas as tarefas----")
            print(tarefas)

        case "4":
            break