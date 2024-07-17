## Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números

def numerosPares():
    for i in range(2, 21, 2):  
        print(i)


numerosPares()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def letMaiusc():
    texto = "O amor é um artifício"
    texto_upper = texto.upper()
    print(texto_upper)

letMaiusc()


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

lista_inicial = ["Amor", "Sentimento", "Mais", "Lindo"]

def adicionar_elementos(lista):
    lista.extend(["Que", "Existe"])
    print(lista)
    
adicionar_elementos(lista_inicial)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def addElementos(arg, *elementos):
    arg.extend(["Olá"])
    arg.extend(elementos)
    print(arg)

# Primeira chamada da função com apenas 1 elemento
lista1 = []
addElementos(lista1, "Mundo")

# Segunda chamada da função com 4 elementos
lista2 = []
addElementos(lista2, "Sou", "Eu", "Wilmara")

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

soma = lambda x, y: x + y
resultado = soma(3, 5)
print(resultado) 

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)+ 32


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(coloque_aqui_sua_função_lambda)
print (list(Fahrenheit))

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit =  map(lambda temp: (9/5) * temp + 32, Celsius)
print (list(Fahrenheit))

# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
[x**2 for x in range(1,11)]

lista = [item**2 for item in range(1,11)]
print (lista)


# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]


palavras = ["maça", "coiote", "banana", "terreno", "Python"]
palavras_com_a = [palavra for palavra in palavras if 'a' in palavra]
print(palavras_com_a)


# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10

num_menores = [numero for numero in range (1,10) if numero < 5]
print(num_menores)



