# Criando a classe Livro que tem como os atributos título, autor, ID e os status de empréstimo
class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        # Criando um atributo para o status de empréstimos(True= Livro emprestado// False= Livro na biblioteca(disponivel para o empréstimo))
        self.statusDeEmprestimo = False

    # Status do livro
    def statusEmprestimo(self):
        if self.statusDeEmprestimo:
            return '\nLivro Emprestado'
        else:
            return '\nLivro Disponível'

# Criando a classe membro que tem como os atributos nome, número do membro e o histórico de livros emprestados
class Membro:
    def __init__(self, nome, numeroDeMembro):
        self.nome = nome
        self.numeroDeMembro = numeroDeMembro
        self.historicoDeLivrosEmprestados = []

# Criando a classe biblioteca:
class Biblioteca:
    def __init__(self):
        # Criando uma lista vazia para por o catálogo de livros
        self.catalogoDeLivros = []
        # Criando outra lista vazia pra inserir os membros
        self.membros = []
    
    # Criação de Métodos:

    # Criando um método para adcionar livros ao catálogo
    def adicionarLivro(self, livro):
        self.catalogoDeLivros.append(livro)

    # Criando um método para adcionar os membros à BIBLIOTECA
    def adicionarMembro(self, membro):
        # Verificando se o número de membro já está em uso
        for m in self.membros:
            if m.numeroDeMembro == membro.numeroDeMembro:
                print('\nNúmero de membro já em uso. Por favor, escolha outro número.')
                return
        # Caso o número de membro não esteja em uso
        self.membros.append(membro)
        print('\nMembro adcionado com Sucesso!')

    # Criando um método para remover livros do catálogo (emprestar o livro para o membro)
    def emprestarLivro(self, livro, membro):
        # Verificando se o livro está disponível para empréstimo
        if livro.statusDeEmprestimo:
            return '\nLivro já emprestado :('
        # Caso o livro esteja disponível para empréstimo
        livro.statusDeEmprestimo = True
        # Adicionando o livro ao histórico do membro
        membro.historicoDeLivrosEmprestados.append(livro)
        return '\nLivro Emprestado com Sucesso :D'

    # Criando um método de devolução do livro emprestado
    def devolverLivro(self, livro, membro):
        # Verificando se o livro está no histórico do membro
        if livro in membro.historicoDeLivrosEmprestados:
            livro.statusDeEmprestimo = False
            # Removendo o livro do histórico do membro
            membro.historicoDeLivrosEmprestados.remove(livro)
            return '\nLivro devolvido com sucesso :D'
        else:
            # Caso o livro não esteja no histórico do membro
            return '\nLivro não está no histórico do membro :('
        

    # Criando um método para conseguir encontrar o livro pelo título dele
    def pesquisarLivroPorTitulo(self, titulo):
        titulo = titulo.lower()
        return [livro for livro in self.catalogoDeLivros if livro.titulo.lower() == titulo]
    
    # Criando um método para conseguir encontrar o livro pelo autor dele
    def pesquisarLivroPorAutor(self, autor):
        autor = autor.lower()
        return [livro for livro in self.catalogoDeLivros if livro.autor.lower() == autor]
    
    # Criando um método para conseguir encontrar o livro pelo id dele
    def pesquisarLivroPorId(self, id):
        return [livro for livro in self.catalogoDeLivros if livro.id == id]

    # Criando um método para mostrar a lista de livros que tem na biblioteca
    def listaDeLivros(self):
        for livro in self.catalogoDeLivros:
            print(f'\nTítulo: {livro.titulo} \nAutor: {livro.autor} \nID: {livro.id} \nStatus: {livro.statusEmprestimo()}')    

# Criando um menu para o Usuário
def menuUsuario():
    print('\n')
    print('-----------------------------------------------')
    print('Seja Bem-Vindo a Biblioteca Raio de Sol!!')
    print('1. Adicionar Livro')
    print('2. Adicionar Membro')
    print('3. Emprestar Livro')
    print('4. Devolver Livro')
    print('5. Pesquisar Livro por Título')
    print('6. Pesquisar Livro por Autor')
    print('7. Pesquisar Livro por ID')
    print('8. Ver lista de Livros da Biblioteca')
    print('0. Sair...')
    print('------------------------------------------------')

# Criando uma função para a escolha do usuário
def main():
    biblioteca = Biblioteca()
    while True:
        # Chamando a função do menuUsuario para que o usuario escolha sua opção
        menuUsuario()
        opcao = int(input('\nDigite a opção desejada: '))

        # Adcionar Livros
        if opcao == 1:
            titulo = input('\nDigite o título do livro: ')
            autor = input('\nDigite o autor do livro: ')
            id = input('\nDigite o id do livro: ')
            livro = Livro(titulo, autor, id)
            biblioteca.adicionarLivro(livro)
            print('\nLivro adicionado com sucesso!')

        # Adcionar Membros
        elif opcao == 2:
            nome = input('\nDigite o nome do membro: ')
            numero = input('\nDigite o numero do membro: ')
            membro = Membro(nome, numero)
            biblioteca.adicionarMembro(membro)

        # Emprestar Livro
        elif opcao == 3:
            titulo = input('\nDigite o título do livro a ser emprestado: ')
            numeroMembro = input('\nDigite o número do membro: ')
            livro = biblioteca.pesquisarLivroPorTitulo(titulo)
            membro = None
            for m in biblioteca.membros:
                if m.numeroDeMembro == numeroMembro:
                    membro = m
                    break
            if membro and livro:
                resultado = biblioteca.emprestarLivro(livro[0], membro)
                print(resultado)
            else:
                print('\nLivro ou membro não encontrado :(')

        # Devolução de Livros
        elif opcao == 4:
            titulo = input('\nDigite o título do livro a ser devolvido: ')
            numeroMembro = input('\nDigite o número do membro: ')
            livro = biblioteca.pesquisarLivroPorTitulo(titulo)
            membro = None
            for m in biblioteca.membros:
                if m.numeroDeMembro == numeroMembro:
                    membro = m
                    break
            if membro and livro:
                resultado = biblioteca.devolverLivro(livro[0], membro)
                print(resultado)
            else:
                print('\nLivro ou membro não encontrado :(')

        # Pesquisar Livros por título
        elif opcao == 5:
            titulo = input('\nDigite o título do livro a ser pesquisado: ')
            livros = biblioteca.pesquisarLivroPorTitulo(titulo)
            if livros:
                for livro in livros:
                    print(f'\nTítulo: {livro.titulo} \nAutor: {livro.autor} \nID: {livro.id}')
            else:
                print("\nLivro não encontrado.")

        # Pesquisar livros por autor
        elif opcao == 6:
            autor = input('\nDigite o nome do autor: ')
            livros = biblioteca.pesquisarLivroPorAutor(autor)
            if livros:
                for livro in livros:
                    print(f'\nTítulo: {livro.titulo} \nAutor: {livro.autor} \nID: {livro.id}')
            else:
                print('\nLivro não encontrado.')

        # Pesquisar livros pelo ID
        elif opcao == 7:
            id = input('\nDigite o ID do livro: ')
            livros = biblioteca.pesquisarLivroPorId(id)
            if livros:
                for livro in livros:
                    print(f'\nTítulo: {livro.titulo} \nAutor: {livro.autor} \nID: {livro.id}')
            else:
                print('\nLivro não encontrado.')

        # Lista de Livros
        elif opcao == 8:
            biblioteca.listaDeLivros()        

        # Sair...
        elif opcao == 0:
            print('\nObrigado por utilizar a Biblioteca. Até mais!')
            break

        # Caso a opção não seja nenhuma válida
        else:
            print('\nOpção inválida. Por favor, tente')


# Chamando a função main
if __name__ == "__main__":
    main()


