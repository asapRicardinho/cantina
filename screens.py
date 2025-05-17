import tkinter as tk
import time
from tkinter import ttk

Produtos = [
    ["ID"],
    ["Nome"],
    ["Preço"]
]



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

    vendasBtn = tk.Button(menuRoot, width=20, height=4, text="Vendas", command="")
    vendasBtn.grid(row=2, column=0, padx=10, pady=5)

    configBtn = tk.Button(menuRoot, width=20, height=4, text="Configurações", command="")
    configBtn.grid(row=3, column=0, padx=10, pady=5)

    menuRoot.mainloop()

def produtosCreate():
    global id
    id = 1
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
    texto = nomeEntry.get()

    # ID and Preço (ID first, Preço fills remaining)
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

    def LimparInterface():
        nomeEntry.delete(0, tk.END)
        precoEntry.delete(0, tk.END)
        idEntry.config(state="normal")
        idEntry.delete(0, tk.END)
        idEntry.insert(0, id)
        idEntry.config(state="readonly")

    def getInformacoesProduto():
        if(nomeEntry.get() == "" or idEntry.get() == "" or precoEntry.get() == ""):
            LimparInterface()
            print("Erro", "Preencha todos os campos")
        else:
            global id
            id = id+1
            Produtos[0].append(idEntry.get())
            Produtos[1].append(nomeEntry.get())
            Produtos[2].append(precoEntry.get())
            tree.insert("", "end", values=(idEntry.get(), nomeEntry.get(), precoEntry.get()))
            idEntry.config(state="normal")
            idEntry.delete(0, tk.END)
            idEntry.insert(0, str(id))
            idEntry.config(state="readonly")
        

    def AlterarProduto():
        if(controleID != 1.1):
            if(nomeEntry.get() == "" or idEntry.get() == "" or precoEntry.get() == ""):
                print("Erro", "Preencha todos os campos")
            else:
                for i in range(len(Produtos[0])):
                    if(Produtos[0][i] == controleID):
                        Produtos[0][i] = idEntry.get()
                        Produtos[1][i] = nomeEntry.get()
                        Produtos[2][i] = precoEntry.get()
                        tree.item(tree.selection(), values=(idEntry.get(), nomeEntry.get(), precoEntry.get()))
                        break
        LimparInterface()


    def RemoverProduto():
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
    removerBtn = tk.Button(produtosDados, text="Remover", width=10,command=RemoverProduto)
    removerBtn.pack(side=tk.RIGHT, padx=5, pady=10)
    adicionarBtn = tk.Button(produtosDados, text="Adicionar", width=10, command=getInformacoesProduto)
    adicionarBtn.pack(side=tk.RIGHT, padx=5, pady=10)
    alterarBtn = tk.Button(produtosDados, text="Alterar", width=10, command=AlterarProduto)
    alterarBtn.pack(side=tk.RIGHT, padx=5, pady=10)

    tree_frame = tk.Frame(produtosRoot)
    tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

    columns = ("id", "nome", "preco")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("preco", text="Preço")
    tree.column("id", width=50)
    tree.column("nome", width=200)
    tree.column("preco", width=80)
    tree.pack(fill="both", expand=True)

    def on_tree_select(event):
        selected_item = tree.focus()
        valores = tree.item(selected_item, "values")
        idEntry.config(state="normal")
        idEntry.delete(0, tk.END)
        idEntry.insert(0, valores[0])
        idEntry.config(state="readonly")
        nomeEntry.delete(0, tk.END)
        nomeEntry.insert(0, valores[1])
        precoEntry.delete(0, tk.END)
        precoEntry.insert(0, valores[2])
        global controleID
        controleID = valores[0]


    tree.bind("<<TreeviewSelect>>", on_tree_select)