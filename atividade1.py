import csv
import subprocess
import platform
import os

COLUNAS_ESPERADAS = ["matricula", "nome_discente", "ano_ingresso", "periodo_ingresso",
                     "tipo_discente", "status_discente", "nivel_ensino", "nome_curso",
                     "modalidade_educacao", "nome_unidade", "nome_unidade_gestora"]


class Aluno:
    def __init__(self, matricula, nome_discente, ano_ingresso, periodo_ingresso,
                 tipo_discente, status_discente, nivel_ensino, nome_curso,
                 modalidade_educacao, nome_unidade, nome_unidade_gestora):
        self.matricula = matricula
        self.nome_discente = nome_discente
        self.ano_ingresso = ano_ingresso
        self.periodo_ingresso = periodo_ingresso
        self.tipo_discente = tipo_discente
        self.status_discente = status_discente
        self.nivel_ensino = nivel_ensino
        self.nome_curso = nome_curso
        self.modalidade = modalidade_educacao
        self.unidade = nome_unidade
        self.unidade_gestora = nome_unidade_gestora

alunos = []

def clear():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"])


def listar_csvs():
    pasta = os.path.dirname(os.path.abspath(__file__))
    csvs = [f for f in os.listdir(pasta) if f.lower().endswith(".csv")]
    return sorted(csvs), pasta


def validar_estrutura(cabecalho):
    colunas_arquivo = [col.strip().lower() for col in cabecalho]

    if len(colunas_arquivo) < len(COLUNAS_ESPERADAS):
        return False, (
            f"O arquivo tem {len(colunas_arquivo)} coluna(s), "
            f"mas são esperadas {len(COLUNAS_ESPERADAS)}."
        )

    faltando = [col for col in COLUNAS_ESPERADAS if col not in colunas_arquivo]

    if faltando:
        return False, "Colunas ausentes: " + ", ".join(faltando)

    return True, None


def selecionar_csv():
    csvs, pasta = listar_csvs()

    if not csvs:
        print("Nenhum arquivo CSV encontrado na pasta do projeto.")
        print(f"Pasta verificada: {pasta}")
        input("Pressione enter para voltar")
        return None

    print("Arquivos CSV disponíveis:")
    print()
    for i, nome in enumerate(csvs, start=1):
        print(f"  {i}. {nome}")
    print()

    escolha = input(f"Selecione o número do arquivo (1-{len(csvs)}): ").strip()

    if not escolha.isdigit() or not (1 <= int(escolha) <= len(csvs)):
        print("Opção inválida.")
        input("Pressione enter para voltar")
        return None

    return os.path.join(pasta, csvs[int(escolha) - 1])


def carregarCSV():
    clear()
    caminho = selecionar_csv()
    if not caminho:
        return

    try:
        with open(caminho, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            cabecalho = next(reader)

            valido, erro = validar_estrutura(cabecalho)
            if not valido:
                print()
                print("ERRO: O arquivo CSV não segue a estrutura esperada.")
                print(f"Detalhe: {erro}")
                print()
                print("Estrutura esperada (colunas):")
                for col in COLUNAS_ESPERADAS:
                    print(f"  - {col}")
                print()
                input("Pressione enter para voltar")
                return

            alunos.clear()
            for linha in reader:
                aluno = Aluno(
                    matricula=linha[0],
                    nome_discente=linha[1],
                    ano_ingresso=linha[2],
                    periodo_ingresso=linha[3],
                    tipo_discente=linha[4],
                    status_discente=linha[5],
                    nivel_ensino=linha[6],
                    nome_curso=linha[7],
                    modalidade_educacao=linha[8],
                    nome_unidade=linha[9],
                    nome_unidade_gestora=linha[10]
                    )
                alunos.append(aluno)

        print(f"\n{len(alunos)} discente(s) carregado(s) com sucesso.")
        input("Pressione enter para voltar")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        input("Pressione enter para voltar")
    except UnicodeDecodeError:
        print("Erro de codificação. Tente salvar o CSV como UTF-8.")
        input("Pressione enter para voltar")


def imprimirAluno(aluno):
    print("------------------------------------------------------")
    print("MATRÍCULA: " + aluno.matricula)
    print("Aluno:" + aluno.nome_discente);
    print("ANO DE INGRESSO: " + aluno.ano_ingresso);
    print("PERIODO DE INGRESSO: "+ aluno.periodo_ingresso);
    print("TIPO DISCENTE: "+ aluno.tipo_discente);
    print("STATUS DISCENTE: " + aluno.status_discente);
    print("NIVEL ENSINO: " + aluno.nivel_ensino);
    print("NOME CURSO: "+ aluno.nome_curso);
    print("MODALIDADE EDUCAÇÃO: " + aluno.modalidade);
    print("NOME DA UNIDADE: " + aluno.unidade);
    print("NOME DA UNIDADE GESTORA: "+ aluno.unidade_gestora);
    print("------------------------------------------------------");
    input("Pressione enter para voltar")

def pesquisarAluno():
    clear()
    matricula = input("digite a matrícula do discente:")
    for item in alunos:
        if(item.matricula == matricula):
            imprimirAluno(item);
            return;
    print("Discente não enontrado");
    input("Pressione enter para voltar");

def exportarTexto():
    clear()
    if not alunos:
        print("Nenhum dado carregado. Carregue um CSV primeiro.")
        input("Pressione enter para voltar")
        return

    arquivo = input("Digite o nome do arquivo de saída (ex: discentes.txt): ")
    with open(arquivo, 'w', encoding='utf-8') as f:
        for aluno in alunos:
            f.write("------------------------------------------------------\n")
            f.write("MATRÍCULA: " + aluno.matricula + "\n")
            f.write("Aluno: " + aluno.nome_discente + "\n")
            f.write("ANO DE INGRESSO: " + aluno.ano_ingresso + "\n")
            f.write("PERIODO DE INGRESSO: " + aluno.periodo_ingresso + "\n")
            f.write("TIPO DISCENTE: " + aluno.tipo_discente + "\n")
            f.write("STATUS DISCENTE: " + aluno.status_discente + "\n")
            f.write("NIVEL ENSINO: " + aluno.nivel_ensino + "\n")
            f.write("NOME CURSO: " + aluno.nome_curso + "\n")
            f.write("MODALIDADE EDUCAÇÃO: " + aluno.modalidade + "\n")
            f.write("NOME DA UNIDADE: " + aluno.unidade + "\n")
            f.write("NOME DA UNIDADE GESTORA: " + aluno.unidade_gestora + "\n")
            f.write("------------------------------------------------------\n\n")

    print(f"Arquivo '{arquivo}' salvo com {len(alunos)} discentes.")
    input("Pressione enter para voltar")


#print(alunos[2])
def main():
    while True:
        clear()
        print("1. Ler CSV");
        print("2. Pesquisar discente");
        print("3. Escrever CSV em texto");
        print("4. sair");
        escolha = input("Escolha uma opção: ");
        if escolha == "1":
            carregarCSV();
        elif escolha == "2":

            pesquisarAluno();
        elif escolha == "3":
            exportarTexto();
        elif escolha == "4":
            return
        else:
            print("ESCOLHA UMA DAS OPÇÕES");

if __name__ == "__main__":
    main()
