import tkinter as tk
import tkinter.messagebox as messagebox
import time
from tkinter import ttk

Produtos = [
    [""],
    [""],
    [""],
    [""]
]
Carrinho = [
    [""],
    [""],
    [""],
    [""],
    [""]
]
id = 1
ValorTotal = 0

# Interface para o sistema de cantina
def menuCreate():
    menuRoot = tk.Tk()
    menuRoot.geometry("400x300")
    menuRoot.resizable(False, False)
    menuRoot.grid_columnconfigure(0, weight=1)

    titleLabel = tk.Label(menuRoot, text="Sistema de Cantina", font=("Arial", 20))
    titleLabel.grid(row=0, column=0)

    produtosBtn = tk.Button(
        menuRoot, width=20, height=4, text="Produtos",
        command=lambda: [menuRoot.destroy(), produtosCreate()]
    )
    produtosBtn.grid(row=1, column=0, padx=10, pady=5)

    vendasBtn = tk.Button(
        menuRoot, width=20, height=4, text="Vendas",
        command=lambda: [menuRoot.destroy(), vendasCreate()]
    )
    vendasBtn.grid(row=2, column=0, padx=10, pady=5)

    configBtn = tk.Button(menuRoot, width=20, height=4, text="Configurações", command="")
    configBtn.grid(row=3, column=0, padx=10, pady=5)

    menuRoot.mainloop()

def produtosCreate():
   

    global id
    
    produtosRoot = tk.Tk()
    produtosRoot.title("Produtos")
    produtosRoot.geometry("600x400")
    produtosRoot.resizable(False, False)

    back_frame = tk.Frame(produtosRoot)
    back_frame.pack(fill="x", pady=(10, 0))
    backBtn = tk.Button(back_frame, text="Voltar", width=15, command=lambda: [produtosRoot.destroy(), menuCreate()])
    backBtn.pack(side=tk.LEFT, padx=10)

    produtosDados = tk.LabelFrame(produtosRoot, text="Dados do Produto")
    produtosDados.pack(padx=10, pady=10, fill="x")

    # Nome
    nomeLabel = tk.Label(produtosDados, text="Nome")
    nomeLabel.pack(anchor="w", padx=5, pady=(10, 0))

    nomeEntry = tk.Entry(produtosDados)
    nomeEntry.pack(anchor="w", padx=5, pady=2, fill="x", expand=True)

    # ID, Preço e Categoria
    id_preco_frame = tk.Frame(produtosDados)
    id_preco_frame.pack(anchor="w", padx=5, pady=(10, 0), fill="x")

    idLabel = tk.Label(id_preco_frame, text="ID")
    idLabel.pack(side=tk.LEFT)
    idEntry = tk.Entry(id_preco_frame, width=8)
    idEntry.pack(side=tk.LEFT, padx=(5, 20))
    idEntry.insert(0, str(id))
    idEntry.config(state="readonly")

    precoLabel = tk.Label(id_preco_frame, text="Preço")
    precoLabel.pack(side=tk.LEFT)
    precoEntry = tk.Entry(id_preco_frame)
    precoEntry.pack(side=tk.LEFT, padx=5, fill="x", expand=True)

    # Categoria
    categoriaLabel = tk.Label(id_preco_frame, text="Categoria")
    categoriaLabel.pack(side=tk.LEFT, padx=(10,0))
    categoriaEntry = tk.Entry(id_preco_frame, width=15)
    categoriaEntry.pack(side=tk.LEFT, padx=5)

    def LimparInterface():
        nomeEntry.delete(0, tk.END)
        precoEntry.delete(0, tk.END)
        categoriaEntry.delete(0, tk.END)
        idEntry.config(state="normal")
        idEntry.delete(0, tk.END)
        idEntry.insert(0, id)
        idEntry.config(state="readonly")

    def getInformacoesProduto():
        if(nomeEntry.get() == "" or idEntry.get() == "" or precoEntry.get() == "" or categoriaEntry.get() == ""):
            LimparInterface()
            print("Erro", "Preencha todos os campos")
        else:
            global id
            id = id+1
            Produtos[0].append(idEntry.get())
            Produtos[1].append(nomeEntry.get())
            Produtos[2].append(precoEntry.get())
            Produtos[3].append(categoriaEntry.get())
            # Adicione categoria ao seu armazenamento se desejar
            tree.insert("", "end", values=(idEntry.get(), nomeEntry.get(), precoEntry.get(), categoriaEntry.get()))
            idEntry.config(state="normal")
            idEntry.delete(0, tk.END)
            idEntry.insert(0, str(id))
            idEntry.config(state="readonly")
            LimparInterface()

    def AlterarProduto():
        if(controleID != 1.1):
            if(nomeEntry.get() == "" or idEntry.get() == "" or precoEntry.get() == "" or categoriaEntry.get() == ""):
                print("Erro", "Preencha todos os campos")
            else:
                for i in range(len(Produtos[0])):
                    if(Produtos[0][i] == controleID):
                        Produtos[0][i] = idEntry.get()
                        Produtos[1][i] = nomeEntry.get()
                        Produtos[2][i] = precoEntry.get()
                        Produtos[3][i] = categoriaEntry.get()
                        # Atualize categoria se desejar
                        tree.item(tree.selection(), values=(idEntry.get(), nomeEntry.get(), precoEntry.get(), categoriaEntry.get()))
                        break
        LimparInterface()

    def RemoverProduto():
        selected_item = tree.selection()
        if(controleID != 1.1):
            for i in range(len(Produtos[0])):
                if(Produtos[0][i] == controleID):
                    Produtos[0].remove(Produtos[0][i])
                    Produtos[1].remove(Produtos[1][i])
                    Produtos[2].remove(Produtos[2][i])
                    tree.delete(tree.selection())
                    break
        LimparInterface()

    # Buttons
    removerBtn = tk.Button(produtosDados, text="Remover", width=10, command=RemoverProduto)
    removerBtn.pack(side=tk.RIGHT, padx=5, pady=10)
    adicionarBtn = tk.Button(produtosDados, text="Adicionar", width=10, command=getInformacoesProduto)
    adicionarBtn.pack(side=tk.RIGHT, padx=5, pady=10)
    alterarBtn = tk.Button(produtosDados, text="Alterar", width=10, command=AlterarProduto)
    alterarBtn.pack(side=tk.RIGHT, padx=5, pady=10)

    tree_frame = tk.Frame(produtosRoot)
    tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Treeview Produtos (tela de produtos)
    columns = ("id", "nome", "preco", "categoria")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("preco", text="Preço")
    tree.heading("categoria", text="Categoria")
    tree.column("id", width=50)
    tree.column("nome", width=200)
    tree.column("preco", width=80)
    tree.column("categoria", width=120)
    tree.pack(fill="both", expand=True)

    def on_tree_select(event):
        selected_item = tree.focus()
        valores = tree.item(selected_item, "values")
        if valores:
            idEntry.config(state="normal")
            idEntry.delete(0, tk.END)
            idEntry.insert(0, valores[0])
            idEntry.config(state="readonly")
            nomeEntry.delete(0, tk.END)
            nomeEntry.insert(0, valores[1])
            precoEntry.delete(0, tk.END)
            precoEntry.insert(0, valores[2])
            categoriaEntry.delete(0, tk.END)
            categoriaEntry.insert(0, valores[3])
            global controleID
            controleID = valores[0]

    for i in range(len(Produtos[0])):
        tree.insert("", "end", values=(Produtos[0][i], Produtos[1][i], Produtos[2][i], Produtos[3][i]))

def vendasCreate():
    global ValorTotal
    IDControle = 1.1
    vendasRoot = tk.Tk()
    vendasRoot.title("Vendas")
    # Centraliza horizontalmente e posiciona mais para o topo (y=50)
    largura = 1200
    altura = 650
    x = int((vendasRoot.winfo_screenwidth() - largura) / 2)
    y = 50  # Mais próximo do topo
    vendasRoot.geometry(f"{largura}x{altura}+{x}+{y}")
    vendasRoot.resizable(False, False)

    # Botão para voltar ao menu no canto superior esquerdo
    voltarBtn = tk.Button(
        vendasRoot, text="Voltar ao Menu", width=18, height=2,
        command=lambda: [vendasRoot.destroy(), menuCreate()]
    )
    voltarBtn.place(x=10, y=10)

    topFrame = tk.LabelFrame(vendasRoot, text="Busca de Produtos")
    topFrame.pack(padx=10, pady=(60,10), fill="x")

    procurarProduto = tk.Entry(topFrame, width=50)
    procurarProduto.pack(side=tk.LEFT, padx=5, pady=10, fill="x", expand=True)

    def RemoverCarrinho():
        global ValorTotal
        global IDControle
        print("Remover")
        selected_item = carrinhoTree.selection()
        for i in range(len(Carrinho[0])):
            print(IDControle)
            if(Carrinho[0][i] == IDControle):
                ValorTotal -= float(Carrinho[2][i]) * int(Carrinho[4][i])
                valorTotalLabel.config(text=str(ValorTotal))
                print("Remover", Carrinho[0][i])
                Carrinho[0].remove(Carrinho[0][i])
                Carrinho[1].remove(Carrinho[1][i])
                Carrinho[2].remove(Carrinho[2][i])
                Carrinho[3].remove(Carrinho[3][i])
                Carrinho[4].remove(Carrinho[4][i])
                carrinhoTree.delete(carrinhoTree.selection())
                
                break

    def BuscarProduto():
        ControleProduto = procurarProduto.get()
        if ControleProduto == "":
            for i in range(len(Produtos[0])):
                for item in tree.get_children():
                    tree.delete(item)
                tree.insert("", "end", values=(Produtos[0][i], Produtos[1][i], Produtos[2][i], Produtos[3][i]))
        else:
            for item in tree.get_children():
                tree.delete(item)
            for i in range(len(Produtos[0])):
                if Produtos[1][i] == ControleProduto:
                    tree.insert("", "end", values=(Produtos[0][i], Produtos[1][i], Produtos[2][i], Produtos[3][i]))
                else:
                    print("Erro", "Produto não encontrado")

    def AdicinarCarrinho():
        global ValorTotal
        selected_item = tree.selection()
        if selected_item:
            valores = tree.item(selected_item, "values")
            if valores:
                for i in range(len(Produtos[0])):
                    if Produtos[0][i] == valores[0]:
                        Carrinho[0].append(Produtos[0][i])
                        Carrinho[1].append(Produtos[1][i])
                        Carrinho[2].append(Produtos[2][i])
                        Carrinho[3].append(Produtos[3][i])
                        Carrinho[4].append(quantidadeEntry.get())
                        carrinhoTree.insert("", "end", values=(Produtos[0][i], Produtos[1][i], Produtos[2][i], Produtos[3][i], quantidadeEntry.get()))
                        ValorTotal += float(Produtos[2][i]) * int(quantidadeEntry.get())
                        valorTotalLabel.config(text=str(ValorTotal))
                        break
        else:
            print("Erro", "Selecione um produto para adicionar ao carrinho")

    procurarBtn = tk.Button(topFrame, text="Procurar", width=14, height=2, command=BuscarProduto)
    procurarBtn.pack(side=tk.LEFT, padx=5, pady=10)
    adicionarBtn = tk.Button(topFrame, text="Adicionar", width=14, height=2, command=AdicinarCarrinho)
    adicionarBtn.pack(side=tk.LEFT, padx=5, pady=10)
    removerBtn = tk.Button(topFrame, text="Remover", width=14, height=2, command=RemoverCarrinho)
    removerBtn.pack(side=tk.LEFT, padx=5, pady=10)

    # Frame principal para Treeview e Carrinho lado a lado
    mainFrame = tk.Frame(vendasRoot)
    mainFrame.pack(fill="both", expand=True, padx=10, pady=10)

    # Treeview de produtos (tela de vendas)
    produtosFrame = tk.Frame(mainFrame)
    produtosFrame.pack(side=tk.LEFT, fill="both", expand=True)

    columns = ("id", "nome", "preco", "categoria")
    tree = ttk.Treeview(produtosFrame, columns=columns, show="headings", height=18)
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("preco", text="Preço")
    tree.heading("categoria", text="Categoria")
    tree.column("id", width=50)
    tree.column("nome", width=200)
    tree.column("preco", width=80)
    tree.column("categoria", width=120)
    tree.pack(fill="both", expand=True)

    Carrinho_ID = 0
    Carrinho_Nome = 0
    Carrinho_Preco = 0
    Carrinho_Categoria = 0
    def on_tree_select(event):
        global Carrinho_ID, Carrinho_Nome, Carrinho_Preco, Carrinho_Categoria
        selected_item = tree.focus()
        valores = tree.item(selected_item, "values")
        if valores:
            for i in range(len(Produtos[0])):
                if Produtos[0][i] == valores[0]:
                    Carrinho_ID = Produtos[0][i]
                    Carrinho_Nome = Produtos[1][i]
                    Carrinho_Preco = Produtos[2][i]
                    Carrinho_Categoria = Produtos[3][i]
    tree.bind("<ButtonRelease-1>", on_tree_select)

    

    # Carrinho de compras ao lado direito
    carrinhoFrame = tk.LabelFrame(mainFrame, text="Carrinho de compras")
    carrinhoFrame.pack(side=tk.LEFT, fill="both", expand=True, padx=(30,10))

    # Treeview do carrinho (tela de vendas)
    carrinhoColumns = ("id", "nome", "preco", "categoria", "qtd")
    carrinhoTree = ttk.Treeview(carrinhoFrame, columns=carrinhoColumns, show="headings", height=14)
    carrinhoTree.heading("id", text="ID")
    carrinhoTree.heading("nome", text="Nome")
    carrinhoTree.heading("preco", text="Preço")
    carrinhoTree.heading("categoria", text="Categoria")
    carrinhoTree.heading("qtd", text="Qtd")
    carrinhoTree.column("id", width=50)
    carrinhoTree.column("nome", width=120)
    carrinhoTree.column("preco", width=60)
    carrinhoTree.column("categoria", width=120)
    carrinhoTree.column("qtd", width=40)
    carrinhoTree.pack(fill="both", expand=True, pady=(10, 10), padx=10)

    def on_carrinho_select(event):
        global IDControle
        selected_item = carrinhoTree.focus()
        valores = carrinhoTree.item(selected_item, "values")
        if valores:
            IDControle = valores[0]
    carrinhoTree.bind("<ButtonRelease-1>", on_carrinho_select)

    # Frame para alinhar Total e Finalizar Compra na parte inferior direita
    bottomCarrinhoFrame = tk.Frame(carrinhoFrame)
    bottomCarrinhoFrame.pack(fill="x", side=tk.BOTTOM, anchor="se", padx=10, pady=10)

    totalLabel = tk.Label(bottomCarrinhoFrame, text="Total:", font=("Arial", 12, "bold"))
    totalLabel.pack(side=tk.LEFT)
    valorTotalLabel = tk.Label(bottomCarrinhoFrame, text="0,00", font=("Arial", 12))
    valorTotalLabel.pack(side=tk.LEFT, padx=(5, 10))

    quantidadeLabel = tk.Label(bottomCarrinhoFrame, text="Quantidade:", font=("Arial", 12, "bold"))
    quantidadeLabel.pack(side=tk.LEFT)
    quantidadeEntry = tk.Entry(bottomCarrinhoFrame, width=50)
    quantidadeEntry.pack(side=tk.LEFT, padx=5, pady=10, fill="x", expand=True)

    def FinalizarCompra():
        global ValorTotal
        if ValorTotal == 0:
            print("Erro", "Carrinho vazio")
        else:
            print("Compra finalizada com sucesso!")
            print("Valor total:", ValorTotal)
            messagebox.showinfo("Compra finalizada!", f"Valor total: {ValorTotal}")
            # Aqui você pode adicionar lógica para salvar a venda em um banco de dados ou arquivo
            # Limpar o carrinho após finalizar a compra
            Carrinho[0].clear()
            Carrinho[1].clear()
            Carrinho[2].clear()
            Carrinho[3].clear()
            Carrinho[4].clear()
            for item in carrinhoTree.get_children():
                carrinhoTree.delete(item)
            ValorTotal = 0
            valorTotalLabel.config(text="0,00")

    finalizarBtn = tk.Button(bottomCarrinhoFrame, text="Finalizar Compra", width=16, height=2, command=FinalizarCompra)
    finalizarBtn.pack(side=tk.RIGHT)

    for i in range(len(Carrinho[0])):
        carrinhoTree.insert("", "end", values=(Carrinho[0][i], Carrinho[1][i], Carrinho[2][i], Carrinho[3][i], Carrinho[4][i]))
    for i in range(len(Produtos[0])):
        tree.insert("", "end", values=(Produtos[0][i], Produtos[1][i], Produtos[2][i], Produtos[3][i]))