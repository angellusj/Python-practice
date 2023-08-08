class Aluno():
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.matricula = 0.0
 
    def recebe(self):
        self.nome = input('Informe o nome do aluno: ')
        self.idade = int(input('Informe a idade do aluno: '))
        self.matricula = float(input('Informe a matrícula do aluno: '))
        print('Aluno cadastrado')
        print()
 
    def listar(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('Matrícula:', self.matricula)
        print()
 
def main():
    vetorAluno = []
 
    def menu():
        while True:
            print('''1-Cadastrar aluno
2-Listar alunos
3-Sair
''')
            escolha = int(input('Escolha uma opção: '))
            
            if escolha == 1:
                quantidadeAlunos = int(input('Informe a quantidade de alunos que serão cadastrados: '))
                vetorAluno.extend([Aluno() for _ in range(quantidadeAlunos)])
                for aluno in vetorAluno:
                    aluno.recebe()
            elif escolha == 2:
                print('Alunos cadastrados:')
                for aluno in vetorAluno:
                    aluno.listar()
            elif escolha == 3:
                break
 
    menu()
 
if __name__ == "__main__":
    main()
