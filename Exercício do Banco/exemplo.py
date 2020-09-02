class Livro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return f'{self.titulo} por {self.autor} com {self.paginas} páginas'
    def __len__(self):
        return self.paginas
    def __del__(self):
        print('O objeto do livro foi deletado!')
liv = Livro('Python', 'Prof Max', 534)
print(liv)
print(len(liv))
del liv