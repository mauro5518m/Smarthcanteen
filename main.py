# ficheiro principal do sistema
import tkinter as tk
from tkinter import Canvas, messagebox
from src.db import conectar
from src.auth import login
from src.estudantes import adicionar as add_estudante, listar as listar_estudantes
from src.refeicoes import adicionar as add_refeicao, listar as listar_refeicoes
from src.carregamentos import carregar_saldo
from src.compras import comprar
from src.relatorios import refeicoes_mais_vendidas

# -------------------------
# FUNÇÕES DA INTERFACE
# -------------------------

def login_funcionario():
    email = entry_email_login.get()
    usuario = login(email)
    if usuario:
        messagebox.showinfo("Login", f"Login bem-sucedido: {usuario[2]}")  # nome do funcionário
    else:
        messagebox.showerror("Login", "Falha no login")

def adicionar_estudante_interface():
    nome = entry_nome.get()
    numero = entry_num.get()
    curso = entry_curso.get()
    email = entry_email_est.get()
    add_estudante(nome, numero, curso, email)
    messagebox.showinfo("Estudante", f"Estudante {nome} adicionado!")

def listar_estudantes_interface():
    alunos = listar_estudantes()
    lista_alunos.delete(0, tk.END)
    for a in alunos:
        lista_alunos.insert(tk.END, f"{a[1]} - {a[2]} ({a[3]})")

def adicionar_refeicao_interface():
    nome = entry_nome_ref.get()
    categoria = entry_categoria.get()
    preco = float(entry_preco.get())
    qtd = int(entry_qtd.get())
    add_refeicao(nome, categoria, preco, qtd)
    messagebox.showinfo("Refeição", f"Refeição {nome} adicionada!")

def listar_refeicoes_interface():
    refeicoes = listar_refeicoes()
    lista_refeicoes.delete(0, tk.END)
    for r in refeicoes:
        lista_refeicoes.insert(tk.END, f"{r[1]} - {r[2]} ({r[3]} CVE)")

def carregar_saldo_interface():
    id_est = int(entry_id_est.get())
    valor = float(entry_valor.get())
    carregar_saldo(id_est, valor)
    messagebox.showinfo("Saldo", f"Saldo de {valor} carregado para estudante {id_est}")

def registrar_compra_interface():
    id_est = int(entry_id_est_compra.get())
    id_ref = int(entry_id_ref_compra.get())
    qtd = int(entry_qtd_compra.get())
    comprar(id_est, id_ref, qtd)
    messagebox.showinfo("Compra", f"Compra registrada: Estudante {id_est}, Refeição {id_ref}, Qtde {qtd}")

def relatorio_refeicoes_interface():
    relatorio = refeicoes_mais_vendidas()
    lista_relatorio.delete(0, tk.END)
    for r in relatorio:
        lista_relatorio.insert(tk.END, f"{r[0]} - {r[1]} vendas")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

# -------------------------
# INTERFACE GRÁFICA
# -------------------------

root = tk.Tk()
root.title("SmartCanteen")
root.geometry("600x600")  # define tamanho da janela

# CRIAR CANVAS
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# ADICIONAR SCROLLBAR
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# FRAME PRINCIPAL DENTRO DO CANVAS
frame_principal = tk.Frame(canvas)
canvas.create_window((0,0), window=frame_principal, anchor="nw")


# LOGIN FUNCIONÁRIO
frame_login = tk.LabelFrame(frame_principal, text="Login Funcionário")
frame_login.pack(padx=10, pady=5, fill="x")
tk.Label(frame_login, text="Email:").grid(row=0, column=0, padx=5, pady=5)
entry_email_login = tk.Entry(frame_login)
entry_email_login.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_login, text="Login", command=login_funcionario).grid(row=0, column=2, padx=5, pady=5)

# ADICIONAR ESTUDANTE
frame_estudante = tk.LabelFrame(root, text="Adicionar Estudante")
frame_estudante.pack(padx=10, pady=5, fill="x")
tk.Label(frame_estudante, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(frame_estudante)
entry_nome.grid(row=0, column=1)
tk.Label(frame_estudante, text="Número:").grid(row=1, column=0)
entry_num = tk.Entry(frame_estudante)
entry_num.grid(row=1, column=1)
tk.Label(frame_estudante, text="Curso:").grid(row=2, column=0)
entry_curso = tk.Entry(frame_estudante)
entry_curso.grid(row=2, column=1)
tk.Label(frame_estudante, text="Email:").grid(row=3, column=0)
entry_email_est = tk.Entry(frame_estudante)
entry_email_est.grid(row=3, column=1)
tk.Button(frame_estudante, text="Adicionar", command=adicionar_estudante_interface).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(frame_estudante, text="Listar Estudantes", command=listar_estudantes_interface).grid(row=5, column=0, columnspan=2, pady=5)

lista_alunos = tk.Listbox(frame_estudante, width=50)
lista_alunos.grid(row=6, column=0, columnspan=2, pady=5)

# ADICIONAR REFEIÇÃO
frame_refeicao = tk.LabelFrame(root, text="Adicionar Refeição")
frame_refeicao.pack(padx=10, pady=5, fill="x")
tk.Label(frame_refeicao, text="Nome:").grid(row=0, column=0)
entry_nome_ref = tk.Entry(frame_refeicao)
entry_nome_ref.grid(row=0, column=1)
tk.Label(frame_refeicao, text="Categoria:").grid(row=1, column=0)
entry_categoria = tk.Entry(frame_refeicao)
entry_categoria.grid(row=1, column=1)
tk.Label(frame_refeicao, text="Preço:").grid(row=2, column=0)
entry_preco = tk.Entry(frame_refeicao)
entry_preco.grid(row=2, column=1)
tk.Label(frame_refeicao, text="Qtd diária:").grid(row=3, column=0)
entry_qtd = tk.Entry(frame_refeicao)
entry_qtd.grid(row=3, column=1)
tk.Button(frame_refeicao, text="Adicionar Refeição", command=adicionar_refeicao_interface).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(frame_refeicao, text="Listar Refeições", command=listar_refeicoes_interface).grid(row=5, column=0, columnspan=2, pady=5)

lista_refeicoes = tk.Listbox(frame_refeicao, width=50)
lista_refeicoes.grid(row=6, column=0, columnspan=2, pady=5)

# CARREGAR SALDO
frame_saldo = tk.LabelFrame(root, text="Carregar Saldo")
frame_saldo.pack(padx=10, pady=5, fill="x")
tk.Label(frame_saldo, text="ID Estudante:").grid(row=0, column=0)
entry_id_est = tk.Entry(frame_saldo)
entry_id_est.grid(row=0, column=1)
tk.Label(frame_saldo, text="Valor:").grid(row=1, column=0)
entry_valor = tk.Entry(frame_saldo)
entry_valor.grid(row=1, column=1)
tk.Button(frame_saldo, text="Carregar Saldo", command=carregar_saldo_interface).grid(row=2, column=0, columnspan=2, pady=5)

# REGISTRAR COMPRA
frame_compra = tk.LabelFrame(root, text="Registrar Compra")
frame_compra.pack(padx=10, pady=5, fill="x")
tk.Label(frame_compra, text="ID Estudante:").grid(row=0, column=0)
entry_id_est_compra = tk.Entry(frame_compra)
entry_id_est_compra.grid(row=0, column=1)
tk.Label(frame_compra, text="ID Refeição:").grid(row=1, column=0)
entry_id_ref_compra = tk.Entry(frame_compra)
entry_id_ref_compra.grid(row=1, column=1)
tk.Label(frame_compra, text="Quantidade:").grid(row=2, column=0)
entry_qtd_compra = tk.Entry(frame_compra)
entry_qtd_compra.grid(row=2, column=1)
tk.Button(frame_compra, text="Registrar Compra", command=registrar_compra_interface).grid(row=3, column=0, columnspan=2, pady=5)

# RELATÓRIO DE VENDAS
frame_relatorio = tk.LabelFrame(root, text="Relatório de Refeições Mais Vendidas")
frame_relatorio.pack(padx=10, pady=5, fill="x")
tk.Button(frame_relatorio, text="Gerar Relatório", command=relatorio_refeicoes_interface).pack(pady=5)
lista_relatorio = tk.Listbox(frame_relatorio, width=50)
lista_relatorio.pack(pady=5)

# -------------------------
# RODA A INTERFACE
# -------------------------
root.mainloop()
