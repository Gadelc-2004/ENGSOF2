import tkinter as tk
from tkinter import messagebox

# ------------------------------------------------------
# VARIÁVEIS GLOBAIS
# ------------------------------------------------------
jogador1_nome = "Jogador 1"
jogador2_nome = "Jogador 2"
placar = {"X": 0, "O": 0}

jogador_atual = "X"
botoes = []
label_placar = None
entry_j1 = None
entry_j2 = None


# ------------------------------------------------------
# LIMPAR JANELA
# ------------------------------------------------------
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()


# ------------------------------------------------------
# SALVAR NOMES E INICIAR JOGO
# ------------------------------------------------------
def salvar_nomes_e_iniciar():
    global jogador1_nome, jogador2_nome

    jogador1_nome = entry_j1.get().strip() or "Jogador 1"
    jogador2_nome = entry_j2.get().strip() or "Jogador 2"

    iniciar_jogo()


# ------------------------------------------------------
# MENU INICIAL (COM 2 CAIXAS PARA NOME)
# ------------------------------------------------------
def mostrar_menu():
    global entry_j1, entry_j2

    limpar_tela()

    frame_menu = tk.Frame(janela, bg="#f0f0f0")
    frame_menu.pack(expand=True, fill="both")

    titulo = tk.Label(
        frame_menu,
        text="Jogo da Velha",
        font=("Arial", 28, "bold"),
        bg="#f0f0f0"
    )
    titulo.pack(pady=20)

    # Área de preenchimento de nomes
    frame_nomes = tk.Frame(frame_menu, bg="#f0f0f0")
    frame_nomes.pack(pady=10)

    # Jogador 1
    lbl_j1 = tk.Label(frame_nomes, text="Jogador 1 (X):", font=("Arial", 14), bg="#f0f0f0")
    lbl_j1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    entry_j1 = tk.Entry(frame_nomes, font=("Arial", 14))
    entry_j1.grid(row=0, column=1, padx=5, pady=5)
    entry_j1.insert(0, jogador1_nome)

    # Jogador 2
    lbl_j2 = tk.Label(frame_nomes, text="Jogador 2 (O):", font=("Arial", 14), bg="#f0f0f0")
    lbl_j2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    entry_j2 = tk.Entry(frame_nomes, font=("Arial", 14))
    entry_j2.grid(row=1, column=1, padx=5, pady=5)
    entry_j2.insert(0, jogador2_nome)

    # Botão Jogar
    btn_jogar = tk.Button(
        frame_menu,
        text="Jogar",
        font=("Arial", 16),
        command=salvar_nomes_e_iniciar
    )
    btn_jogar.pack(fill="x", padx=80, pady=15)

    # Botão Sair
    btn_sair = tk.Button(
        frame_menu,
        text="Sair",
        font=("Arial", 16),
        command=janela.quit
    )
    btn_sair.pack(fill="x", padx=80, pady=10)


# ------------------------------------------------------
# AJUSTE DE FONTES RESPONSIVAS
# ------------------------------------------------------
def ajustar_fontes(event):
    if not botoes:
        return

    largura = janela.winfo_width()

    novo_tamanho = max(14, largura // 25)

    for b in botoes:
        b.config(font=("Arial", novo_tamanho, "bold"))

    label_placar.config(font=("Arial", max(14, largura // 30), "bold"))


# ------------------------------------------------------
# VERIFICAR VITÓRIA
# ------------------------------------------------------
def verificar_vitoria():
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinacoes:
        if botoes[a]["text"] != "" and botoes[a]["text"] == botoes[b]["text"] == botoes[c]["text"]:
            return botoes[a]["text"]

    return None


# ------------------------------------------------------
# AÇÃO DE CLIQUE
# ------------------------------------------------------
def clique(i):
    global jogador_atual

    if botoes[i]["text"] == "":
        botoes[i]["text"] = jogador_atual

        vencedor = verificar_vitoria()
        if vencedor:
            placar[vencedor] += 1
            messagebox.showinfo("Vitória!", f"{nome_do_jogador(vencedor)} venceu!")
            reiniciar_tabuleiro()
            atualizar_placar()
            return

        if all(btn["text"] != "" for btn in botoes):
            messagebox.showinfo("Empate", "O jogo terminou empatado!")
            reiniciar_tabuleiro()
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"


# ------------------------------------------------------
# NOME DO JOGADOR PELO SÍMBOLO
# ------------------------------------------------------
def nome_do_jogador(simbolo):
    return jogador1_nome if simbolo == "X" else jogador2_nome


# ------------------------------------------------------
# REINICIAR TABULEIRO
# ------------------------------------------------------
def reiniciar_tabuleiro():
    global jogador_atual
    jogador_atual = "X"
    for b in botoes:
        b.config(text="")


# ------------------------------------------------------
# ATUALIZAR PLACAR
# ------------------------------------------------------
def atualizar_placar():
    label_placar.config(
        text=f"{jogador1_nome} (X): {placar['X']}    |    {jogador2_nome} (O): {placar['O']}"
    )


# ------------------------------------------------------
# INICIAR JOGO
# ------------------------------------------------------
def iniciar_jogo():
    global botoes, label_placar, jogador_atual

    limpar_tela()
    botoes = []
    jogador_atual = "X"

    # Placar
    label_placar = tk.Label(
        janela,
        text=f"{jogador1_nome} (X): {placar['X']}    |    {jogador2_nome} (O): {placar['O']}",
        font=("Arial", 16, "bold")
    )
    label_placar.pack(pady=20)

    # Tabuleiro
    frame_jogo = tk.Frame(janela)
    frame_jogo.pack(expand=True, fill="both", padx=20, pady=20)

    for i in range(3):
        frame_jogo.grid_rowconfigure(i, weight=1)
        frame_jogo.grid_columnconfigure(i, weight=1)

    for i in range(9):
        btn = tk.Button(
            frame_jogo,
            text="",
            font=("Arial", 24, "bold"),
            command=lambda i=i: clique(i)
        )
        btn.grid(row=i//3, column=i%3, padx=5, pady=5, sticky="nsew")
        botoes.append(btn)

    # Botões inferiores
    frame_btns = tk.Frame(janela)
    frame_btns.pack(pady=10)

    tk.Button(frame_btns, text="Reiniciar", font=("Arial", 14), command=reiniciar_tabuleiro)\
        .pack(side="left", padx=20)

    tk.Button(frame_btns, text="Menu", font=("Arial", 14), command=mostrar_menu)\
        .pack(side="left", padx=20)

    janela.bind("<Configure>", ajustar_fontes)


# ------------------------------------------------------
# JANELA PRINCIPAL
# ------------------------------------------------------
janela = tk.Tk()
janela.title("Jogo da Velha Responsivo")
janela.geometry("420x550")

mostrar_menu()
janela.mainloop()

