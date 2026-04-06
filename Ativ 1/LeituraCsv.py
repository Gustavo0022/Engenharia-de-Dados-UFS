import csv
import subprocess
import platform


class Aluno:
    terminar = "depois"

alunos = []

def clear():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"])


def carregarCSV():
    arquivo = input("Digite o nome ou caminho do arquivo:");
    with open(arquivo) as csvfile:
        reader = csv.reader(csvfile,delimiter=',',quotechar='"')
        
        for row in reader:
            alunos.extend([row]);
        


def imprimirAluno(aluno):
    print("------------------------------------------------------")
    print("MATRÍCULA: " + aluno[0])
    print("Aluno:" + aluno[1]);
    print("ANO DE INGRESSO: " + aluno[2]);
    print("PERIODO DE INGRESSO: "+ aluno[3]);
    print("TIPO DISCENTE: "+ aluno[4]);
    print("STATUS DISCENTE: " + aluno[5]);
    print("NIVEL ENSINO: " + aluno[6]);
    print("NOME CURSO: "+ aluno[7]);
    print("MODALIDADE EDUCAÇÃO: " + aluno[8]);
    print("NOME DA UNIDADE: " + aluno[9]);
    print("NOME DA UNIDADE GESTORA: "+ aluno[10]);
    print("------------------------------------------------------");
    input("Pressione enter para voltar")

def pesquisarAluno():
    clear
    matricula = input("digite a matrícula do discente:")
    for item in alunos:
        if(item[0] == matricula):
            imprimirAluno(item);
            break;
    print("Discente não enontrado");
    input("Pressione enter para voltar");

def exportarTexto():
    clear()
    print("W.I.P.")
    input("Pressione enter para voltar");
    

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