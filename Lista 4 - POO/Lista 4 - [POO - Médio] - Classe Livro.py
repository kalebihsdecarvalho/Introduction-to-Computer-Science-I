#implemente uma classe chamada Livro com os seguintes atributos:

#titulo: O título do livro.
#autor: O nome do autor.
#paginas: O número de páginas do livro.
#A classe deverá conter os seguintes métodos:

#exibir_informacoes(): Método que exibe as informações do livro no seguinte formato: Título por Autor
#verificar_tamanho(): Método que verifica se o livro é longo ou curto. Um livro é considerado longo se tiver mais de 500 páginas, caso contrário será considerado curto.
#O programa deverá solicitar ao usuário as informações do livro (título, autor e número de páginas) e exibir:

#As informações do livro.
#A classificação do livro, se ele é longo ou curto.
#Formato de Entrada:

#O título do livro.
#O nome do autor.
#O número de páginas.
#Formato de Saída: Exiba o título e o autor do livro no formato:

#Título por Autor Exiba se o livro é longo ou curto no formato:
#Livro Longo ou Livro Curto

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def exibir_informacoes(self):
        info = titulo + ' por ' + autor
        return(info)

    def verificar_tamanho(self):
        if self.paginas > 500:
            return('Livro Longo')
        else:
            return('Livro Curto')

titulo = input().strip()
autor = input().strip()
paginas = int(input().strip())
livro = Livro(titulo, autor, paginas)

print(f'{livro.exibir_informacoes()} \n{livro.verificar_tamanho()}')
