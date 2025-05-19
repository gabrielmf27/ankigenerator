import genanki
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

df_carregado = None

def ler_arquivo_para_dataframe(caminho):
    ext = os.path.splitext(caminho)[1].lower()

    if ext == ".csv":
        return pd.read_csv(caminho, encoding="latin1")
    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(caminho)
    elif ext == ".ods":
        return pd.read_excel(caminho, engine="odf")
    else:
        raise ValueError("Formato de arquivo não suportado.")

def converter_para_apkg(df, nome_arquivo):
    try:
        if df.shape[1] < 2:
            raise ValueError("O arquivo precisa ter pelo menos duas colunas (Pergunta e Resposta).")

        model_id = 1607392319
        model = genanki.Model(
            model_id,
            'Modelo Simples',
            fields=[
                {'name': 'Pergunta'},
                {'name': 'Resposta'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Pergunta}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Resposta}}',
                },
            ])

        deck_id = 2059400110
        nome_deck = os.path.splitext(os.path.basename(nome_arquivo))[0]
        deck = genanki.Deck(deck_id, nome_deck)

        for _, row in df.iterrows():
            pergunta = str(row[0])
            resposta = str(row[1])
            note = genanki.Note(model=model, fields=[pergunta, resposta])
            deck.add_note(note)

        output_path = os.path.splitext(nome_arquivo)[0] + ".apkg"
        genanki.Package(deck).write_to_file(output_path)

        messagebox.showinfo("Sucesso", f"APKG salvo como:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter: {e}")

def exibir_dataframe(df):
    for widget in frame_tabela.winfo_children():
        widget.destroy()

    colunas = df.columns.tolist()
    tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=12)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor="w", width=200)

    for _, row in df.iterrows():
        valores = [str(cell) for cell in row]
        tree.insert("", "end", values=valores)

    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")

    frame_tabela.grid_rowconfigure(0, weight=1)
    frame_tabela.grid_columnconfigure(0, weight=1)

def selecionar_arquivo():
    global df_carregado, caminho_arquivo
    caminho = filedialog.askopenfilename(
        filetypes=[
            ("Arquivos suportados", "*.csv *.xls *.xlsx *.ods"),
            ("Todos os arquivos", "*.*")
        ]
    )
    if caminho:
        try:
            df = ler_arquivo_para_dataframe(caminho)
            df_carregado = df
            caminho_arquivo = caminho
            exibir_dataframe(df)
            botao_gerar_anki.config(state="normal")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o arquivo: {e}")

def gerar_anki():
    if df_carregado is not None:
        converter_para_apkg(df_carregado, caminho_arquivo)

janela = tk.Tk()
janela.title("Conversor de Arquivos para Anki (.apkg)")
janela.geometry("900x650")
janela.configure(bg="#1e1e1e")

estilo_fonte = ("Segoe UI", 12)
cor_fundo = "#1e1e1e"
cor_texto = "#d4d4d4"
cor_botao = "#2d4a7a"
cor_botao_hover = "#3a5a99"

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background=cor_fundo, foreground=cor_texto, fieldbackground=cor_fundo, font=estilo_fonte)
style.configure("Treeview.Heading", background="#2b2b2b", foreground="#ffffff", font=("Segoe UI", 11, "bold"))

def on_enter(e): e.widget.configure(bg=cor_botao_hover)
def on_leave(e): e.widget.configure(bg=cor_botao)

rotulo = tk.Label(
    janela,
    text="Clique no botão para selecionar um arquivo (.csv, .xls, .xlsx, .ods):",
    font=estilo_fonte,
    bg=cor_fundo,
    fg=cor_texto,
    wraplength=800,
    justify="center"
)
rotulo.pack(pady=20)

botao_selecionar = tk.Button(
    janela,
    text="Selecionar Arquivo",
    command=selecionar_arquivo,
    font=("Segoe UI", 12, "bold"),
    bg=cor_botao,
    fg="white",
    activebackground=cor_botao_hover,
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10
)
botao_selecionar.pack(pady=5)
botao_selecionar.bind("<Enter>", on_enter)
botao_selecionar.bind("<Leave>", on_leave)

frame_tabela = tk.Frame(janela, bg=cor_fundo)
frame_tabela.pack(fill="both", expand=True, padx=20, pady=20)

botao_gerar_anki = tk.Button(
    janela,
    text="Gerar Arquivo Anki (.apkg)",
    command=gerar_anki,
    font=("Segoe UI", 12, "bold"),
    bg=cor_botao,
    fg="white",
    activebackground=cor_botao_hover,
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    state="disabled"
)
botao_gerar_anki.pack(pady=10)
botao_gerar_anki.bind("<Enter>", on_enter)
botao_gerar_anki.bind("<Leave>", on_leave)

janela.mainloop()
