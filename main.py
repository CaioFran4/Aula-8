import json
import unicodedata

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos 

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

produtos = carregar_produtos()


def mostrar_estoque():
    print("----> ESTOQUE <----")
    limite_baixo = 20
    
    for p in produtos:
        status = "Baixo" if p['estoque'] <= limite_baixo else "Alto"
        print(p)

def cadastrar_produto():
    print("----> Cadastrando Produto <----")
    cadastro = input("Qual produto será cadastrado?: ").capitalize() .strip()
    c_categoria = input("Qual a categoria do produto?: ").capitalize() .strip()
    c_preco = float(input("Qual o preço do produto?: "))
    c_estoque = float(input("Qual a quantidade de estoque da leva desse produto?: "))
    novo_id = produtos[-1]['id'] + 1 if produtos else 1

    cadastrar = {
        "id": novo_id,
        "nome": cadastro,
        "categoria": c_categoria,
        "preco": c_preco,
        "estoque":c_estoque
    }   
    produtos.append(cadastrar)
    salvar_produtos(produtos)
    print(produtos)

def mostrar_categoria():
    print("----> MOSTRANDO ESTOQUE POR CATEGORIA <----")
    pergunta = input("Qual a categoria procurada?: ").lower() .strip()
    remover_acentos = str.maketrans("áéíóúâêîôûãõçàèìòùäëïöü", "aeiouaeiouaocaeiouaeiou")


    for produto in produtos:
        
        if produto['categoria'].lower().translate(remover_acentos) == pergunta.translate(remover_acentos):
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {produto['categoria']}  | Preço: {produto['preco']} | Estoque: {produto['estoque']}")

def mostrar_preco():
    print("----> MOSTRANDO ESTOQUE POR PREÇO <----")
    preco_minimo = float(input("Qual o preço MÍNIMO?: "))
    preco_maximo = float(input("Qual o preço MÁXIMO?: "))
    print("----> MOSTRANDO ESTOQUE PELO PREÇO ESCOLHIDO <----") 
    for produto in produtos:
        
        if preco_minimo <= produto['preco'] <= preco_maximo:
            print(f" ID: {produto['id']} | Nome: {produto['nome']} | Preço: {produto['preco']}")

def analisar_estoque():
    print("----> ANALISANDO ESTOQUE <----")
    p_estoque = input("Qual situação do estoque você deseja ver?: ") .capitalize()

    limite_baixo = 20

    for produto in produtos:
        status = "Baixo" if produto['estoque'] <= limite_baixo else "Alto"

        if p_estoque == "Baixo" and produto['estoque'] <= limite_baixo:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {produto['categoria']}  | Preço: {produto['preco']} | Estoque: {produto['estoque']}")
            salvar_produtos(produtos)

        elif p_estoque == "Alto" and produto['estoque'] >= limite_baixo:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {produto['categoria']}  | Preço: {produto['preco']} | Estoque: {produto['estoque']}")   
            salvar_produtos(produtos)      
               






    


while True:

    print("======> Menu <======")
    print("----- 1 - Mostrar Estoque/Produtos-----")
    print("----- 2 - Cadastrar Produto-----")
    print("----- 3 - Mostrar por Categoria-----")
    print("----- 4 - Mostrar por Preço-----")
    print("----- 5 - Procurar por Estoque(Alto ou Baixo Estoque)-----")
    print("----- 0 - Encerrar Sistema-----")

    opcao = input("Escolha uma das opções a seguir: ")

    if opcao == "1":
        mostrar_estoque()

    elif opcao == "2":
        cadastrar_produto()

    elif opcao == "3":
        mostrar_categoria()

    elif opcao == "4":
        mostrar_preco()

    elif opcao == "5":
        analisar_estoque()
    
    elif opcao == "0":
        print("----> Encerrando Sistema <----")
        break
        