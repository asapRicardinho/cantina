import tkinter as tk
from tkinter import ttk

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

    # ID and Preço (ID first, Preço fills remaining)
    id_preco_frame = tk.Frame(produtosDados)
    id_preco_frame.pack(anchor="w", padx=5, pady=(10, 0), fill="x")

    idLabel = tk.Label(id_preco_frame, text="ID")
    idLabel.pack(side=tk.LEFT)
    idEntry = tk.Entry(id_preco_frame, width=8)
    idEntry.pack(side=tk.LEFT, padx=(5, 20))

    precoLabel = tk.Label(id_preco_frame, text="Preço")
    precoLabel.pack(side=tk.LEFT)
    precoEntry = tk.Entry(id_preco_frame)
    precoEntry.pack(side=tk.LEFT, padx=5, fill="x", expand=True)

    removerBtn = tk.Button(produtosDados, text="Remover", width=10)
    removerBtn.pack(side=tk.RIGHT, padx=5, pady=10)
    adicionarBtn = tk.Button(produtosDados, text="Adicionar", width=10)
    adicionarBtn.pack(side=tk.RIGHT, padx=5, pady=10)
    alterarBtn = tk.Button(produtosDados, text="Alterar", width=10)
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




