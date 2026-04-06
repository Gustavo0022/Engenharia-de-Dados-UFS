#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <cstring>


struct Aluno{
    std::string matricula;
    std::string nome_discente;
    std::string ano_ingresso;
    std::string periodo_ingresso;
    std::string tipo_discente;
    std::string status_discente;
    std::string nivel_ensino;
    std::string nome_curso;
    std::string modalidade_educacao;
    std::string nome_unidade;
    std::string nome_unidade_gestora;

    public:
    void getInfo(int campo, std::string dado){
        switch(campo){
            case 1: matricula = dado;
                break;
            case 2: nome_discente = dado;
                break;
            case 3: ano_ingresso = dado;
                break;
            case 4: periodo_ingresso = dado;
                break;
            case 5: tipo_discente = dado;
                break;
            case 6: status_discente = dado;
                break;
            case 7: nivel_ensino = dado;
                break;
            case 8: nome_curso = dado;
                break;
            case 9: modalidade_educacao = dado;
                break;
            case 10: nome_unidade = dado;
                break;
            case 11: nome_unidade_gestora = dado;
                break;
        }
    }

    
};


bool operator==(const Aluno& one, const Aluno& other){
    return one.matricula == other.matricula;
}
std::ifstream input;




int lerDiscentes(std::vector<Aluno>& alunos, std::string file){
    input.open(file);

    std::string line = "";
    std::getline(input,line);
    std::string token;
    std::stringstream str_stream(line);

   

 /*    while(!input.eof()){
        std::getline(input,line);
        int i = 0;
        while(i < 11){
            std::getline(str_stream,token,',');
            if(i = 8 && token.substr(token.find("(Matutino")+1))
        }
        
        
    } */
/*     while(!input.eof()){
        std::getline(input,line);
        Aluno newAl;

        int firstComma = line.find(",");
        int secondComma = line.find(",",firstComma+1);
        newAl.matricula = line.substr(1,12);

        newAl.nome_discente = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);
        newAl.ano_ingresso = line.substr(firstComma+2,4);
        
        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.periodo_ingresso = line.substr(firstComma+2,1);
        
        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.tipo_discente = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.status_discente = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.nivel_ensino = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.nome_curso = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.modalidade_educacao = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.nome_unidade = line.substr(firstComma+2,secondComma - firstComma -1);

        firstComma = secondComma;
        secondComma = line.find(",",firstComma+1);

        newAl.nome_unidade_gestora = line.substr(firstComma+2,secondComma - firstComma -1);
        
        
        alunos.push_back(newAl);
    }
 */

    
    return 0;
}


int imprimirDiscente(std::vector<Aluno> alunos){
    std::cout << "Insira a matrícula do aluno:";
    std::string matricula;
    std::cin >> matricula;

    Aluno temp;
    temp.matricula = matricula;

    //temp = std::find(alunos.begin(),alunos.end(),temp);
    
}

int main(int argc, char* argv[]){
    std::vector<Aluno> alunos;

    if(argc < 2){
        std::cout << "Erro: Arquivo não digitado.\n Forma de uso: LeituraCsv [NOME_DO_ARQUIVO]";
        return EXIT_FAILURE;
    }
    std::string file = argv[1];

    if(file.substr(file.length()-3) != ".csv"){
        std::cout << "Erro: Arquivo não é .csv. \n Forma de uso: LeituraCsv [NOME_DO_ARQUIVO]";
        return EXIT_FAILURE;
    }

    
    

    

}