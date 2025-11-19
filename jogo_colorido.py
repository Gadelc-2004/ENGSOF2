# Jogo da Velha - Tema Espaço Infantil (Versão Atualizada)
# Layout com botões maiores, campos centralizados e estilo infantil

import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Janela Principal
# ------------------------------
root = tk.Tk()
root.title("Jogo da Velha - Espaço Infantil")
root.geometry("600x700")
root.configure(bg="#001f3f")

# Variáveis globais
player1 = "Jogador 1"
player2 = "Jogador 2"
current_player = "X"
board = [""] * 9
score_x = 0
score_o = 0

# Frames principais
menu_frame = tk.Frame(root, bg="#001f3f")
game_frame = tk.Frame(root, bg="#001f3f")

menu_frame.pack(fill="both", expand=True)

# ------------------------------
# Funções
# ------------------------------
def voltar_menu():
    game_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)

def iniciar_jogo():
    global player1, player2

    p1 = entry_p1.get().strip()
    p2 = entry_p2.get().strip()

    if p1 != "":
        player1 = p1
    if p2 != "":
        player2 = p2

    menu_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

    resetar_tabuleiro()
    atualizar_placar()

def resetar_tabuleiro():
    global board, current_player
    board = [""] * 9
    current_player = "X"

    for i in range(9):
        botoes[i]["text"] = ""
        botoes[i]["state"] = "normal"

def atualizar_placar():
    label_placar.config(
        text=f"{player1} (X): {score_x}    |    {player2} (O): {score_o}"
    )

def apertar_botao(i):
    global current_player, score_x, score_o

    if board[i] == "":
        board[i] = current_player
        botoes[i]["text"] = current_player

        if verificar_vitoria(current_player):
            if current_player == "X":
                score_x += 1
            else:
                score_o += 1
            atualizar_placar()
            messagebox.showinfo("Vitória!", f"{current_player} venceu!")
            resetar_tabuleiro()
            return

        if "" not in board:
            messagebox.showinfo("Empate", "Empate!")
            resetar_tabuleiro()
            return

        current_player = "O" if current_player == "X" else "X"

def verificar_vitoria(p):
    c = board
    return (
        (c[0] == p and c[1] == p and c[2] == p) or
        (c[3] == p and c[4] == p and c[5] == p) or
        (c[6] == p and c[7] == p and c[8] == p) or
        (c[0] == p and c[3] == p and c[6] == p) or
        (c[1] == p and c[4] == p and c[7] == p) or
        (c[2] == p and c[5] == p and c[8] == p) or
        (c[0] == p and c[4] == p and c[8] == p) or
        (c[2] == p and c[4] == p and c[6] == p)
    )

# ------------------------------
# MENU INICIAL
# ------------------------------
label_titulo = tk.Label(menu_frame, text="Jogo da Velha",
    font=("Comic Sans MS", 40, "bold"), bg="#001f3f", fg="#ffdc00")
label_titulo.pack(pady=40)

label_sub = tk.Label(menu_frame, text="Tema Espaço Infantil",
    font=("Comic Sans MS", 20), bg="#001f3f", fg="#7FDBFF")
label_sub.pack(pady=10)

# Centralização dos campos
entry_p1 = tk.Entry(menu_frame, font=("Comic Sans MS", 20), justify="center")
entry_p2 = tk.Entry(menu_frame, font=("Comic Sans MS", 20), justify="center")

entry_p1.place(relx=0.5, rely=0.45, anchor="center", width=300)
entry_p2.place(relx=0.5, rely=0.55, anchor="center", width=300)

label_p1 = tk.Label(menu_frame, text="Nome do Jogador 1 (X):",
    font=("Comic Sans MS", 18), bg="#001f3f", fg="#FF851B")
label_p1.place(relx=0.5, rely=0.40, anchor="center")

label_p2 = tk.Label(menu_frame, text="Nome do Jogador 2 (O):",
    font=("Comic Sans MS", 18), bg="#001f3f", fg="#FF851B")
label_p2.place(relx=0.5, rely=0.50, anchor="center")

btn_style = {
    "font": ("Comic Sans MS", 22, "bold"),
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

btn_jogar = tk.Button(menu_frame, text="JOGAR", bg="#FF851B", fg="white",
                      command=iniciar_jogo, **btn_style)
btn_sair = tk.Button(menu_frame, text="SAIR", bg="#0074D9", fg="white",
                     command=root.quit, **btn_style)

btn_jogar.place(relx=0.5, rely=0.70, anchor="center", width=300)
btn_sair.place(relx=0.5, rely=0.82, anchor="center", width=300)

# ------------------------------
# TELA DO JOGO
# ------------------------------

label_placar = tk.Label(game_frame, text="", font=("Comic Sans MS", 24, "bold"),
    bg="#001f3f", fg="#ffdc00")
label_placar.pack(pady=20)

tabuleiro = tk.Frame(game_frame, bg="#001f3f")
tabuleiro.pack()

botoes = []
for i in range(9):
    b = tk.Button(tabuleiro, text="", font=("Comic Sans MS", 40, "bold"),
                  width=4, height=2, bg="#0074D9", fg="white",
                  command=lambda i=i: apertar_botao(i))
    b.grid(row=i//3, column=i%3, padx=10, pady=10)
    botoes.append(b)

frame_btns = tk.Frame(game_frame, bg="#001f3f")
frame_btns.pack(pady=20)

btn_reset = tk.Button(frame_btns, text="Reiniciar",
                      bg="#FF851B", fg="white",
                      font=("Comic Sans MS", 20, "bold"),
                      command=resetar_tabuleiro)
btn_voltar = tk.Button(frame_btns, text="Voltar ao Menu",
                       bg="#0074D9", fg="white",
                       font=("Comic Sans MS", 20, "bold"),
                       command=voltar_menu)

btn_reset.grid(row=0, column=0, padx=20, ipadx=20, ipady=10)
btn_voltar.grid(row=0, column=1, padx=20, ipadx=20, ipady=10)

root.mainloop()
