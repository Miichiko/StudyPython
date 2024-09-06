import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


#  criando a janela
window = tk.Tk()
window.title('Meu App de Tarefas')
window.configure(bg='#F0F0F0')
window.geometry('500x600')

# adicionando icons
icon_edit = tk.PhotoImage(
    file='C:/Users/MK10/Desktop/python/basic_python/Projetos.py/edit.png').subsample(2, 2)
icon_delete = PhotoImage(
    file='C:/Users/MK10/Desktop/python/basic_python/Projetos.py/delete.png').subsample(2, 2)
icon_check = PhotoImage(
    file='C:/Users/MK10/Desktop/python/basic_python/Projetos.py/check.png').subsample(2, 2)

tarefas_adicionadas = []
label_tarefa = None


def botao_adicionar_tarefa():

    global label_tarefa
    tarefa = entry.get()
    if tarefa != '':
        indice = len(tarefas_adicionadas)
        tarefas_adicionadas.append(tarefa)
        # criando uma label no canvas interior
        label_tarefa = tk.Label(canvas_interior, text=tarefa, font=(
            'Garamond', 16), bg='red', fg='#333', anchor='w')
        label_tarefa.pack(side=tk.TOP, expand=True,
                          fill=tk.X, pady=10, padx=10)
        entry.delete(0, tk.END)
        # meu botões
        edit_buttom = tk.Button(label_tarefa, image=icon_edit,
                                command=lambda idx=indice, l=label_tarefa: editar_tarefa(idx, l), bg='white', relief=tk.FLAT)
        edit_buttom.pack(side=tk.RIGHT, padx=5, pady=5)
        delete_buttom = tk.Button(label_tarefa, image=icon_delete,
                                  command=lambda idx=indice, l=label_tarefa: deletar_tarefa(idx, l), bg='white', relief=tk.FLAT)
        delete_buttom.pack(side=tk.RIGHT, padx=5)
        check_button = tk.Button(label_tarefa, image=icon_check,
                                 command=lambda l=label_tarefa: check_tarefa(l), bg='white', relief=tk.FLAT)
        check_button.pack(side=tk.RIGHT, padx=5)
    else:
        messagebox.showwarning(
            'Entrada inválida', 'Por favor, insira sua tarefa!')

    def editar_tarefa(indice, label_tarefa):
        tarefa_antiga = tarefas_adicionadas[indice]

        if 0 <= indice < len(tarefas_adicionadas):
            # remove o label atual
            label_tarefa.pack_forget()

        # cria um entry pra editar a tarefa
        entry_edit = tk.Entry(canvas_interior, bg='white')
        entry_edit.insert(0, tarefa_antiga)
        entry_edit.pack(side=tk.LEFT, fill=tk.X, padx=10)

        # troca o botão editar pelo de salvar
        salvar_button = tk.Button(
            canvas_interior, text="Salvar", command=lambda: salvar_edicao(entry_edit, indice, label_tarefa))
        salvar_button.pack(side=tk.LEFT)

        def salvar_edicao(entry_edit, indice, label_tarefa):
            global tarefas_adicionadas

            # Obtém o novo texto do Entry
            nova_tarefa = entry_edit.get()

            # Atualiza a lista de tarefas
            tarefas_adicionadas[indice] = nova_tarefa

            # Atualiza o Label com o novo texto
            label_tarefa.config(text=nova_tarefa)

            # Remove o Entry e exibe o Label novamente
            entry_edit.pack_forget()
            salvar_button.pack_forget()
            label_tarefa.pack(side=tk.TOP, expand=True,
                              fill=tk.X, pady=10, padx=10)

    def deletar_tarefa(indice, label_tarefa):
        global tarefas_adicionadas

        if 0 <= indice < len(tarefas_adicionadas):
            # Remove a tarefa da lista
            del tarefas_adicionadas[indice]

        # Remove o label da interface
        label_tarefa.forget()

        # Atualiza o layout do canvas_interior
        canvas_interior.update_idletasks()
        canvas.update_idletasks()

        # Reconfigura o scrollregion para ajustar o canvas ao conteúdo atualizado
        canvas.configure(scrollregion=canvas.bbox('all'))

    def check_tarefa(label_tarefa):
        # Obtém a fonte atual da label
        fonte_atual = font.Font(label_tarefa, label_tarefa.cget("font"))

        # Verifica se já está em negrito ou com overstrike
        if fonte_atual.actual("weight") == "bold" and fonte_atual.actual("overstrike") == 1:
            # Se já está em negrito e tachado, volta ao normal
            fonte_atual.config(weight="normal", overstrike=False)
        else:
            # Caso contrário, coloca em negrito e tachado
            fonte_atual.config(weight="bold", overstrike=True)

        # Aplica a nova fonte ao label
        label_tarefa.config(font=fonte_atual)


# criando o Título do app
font_header = font.Font(family='Garamond', size=24, weight='bold')
label_header = tk.Label(window, text='Meu App de Tarefas',
                        font=font_header, bg='#F0F0F0', fg='#333').pack(pady=20)

# criando a caixa de entrada
frame = tk.Frame(window, bg='#F0F0F0')
frame.pack(pady=10)
# entry é onde a pessoa escreve
entry = tk.Entry(frame, font=('Garamond', 14),
                 relief=tk.FLAT, bg='white', fg='grey', width=30)
entry.pack(side=tk.LEFT, padx=10)

# criando o botão de entrada
entry_button = tk.Button(frame, text='Adicionar Tarefa', command=botao_adicionar_tarefa,
                         bg='#4CAF50', fg='white', height=1, width=15, font=('Roboto', 11), relief=tk.FLAT)
entry_button.pack(side=tk.LEFT, padx=10)

# criando a borda do canvas
frame_homework_list = tk.Frame(window)
frame_homework_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# caixa onde será as tarefas inseridas
canvas = tk.Canvas(frame_homework_list, bg='green')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# fazendo o scroll agora
scroll = ttk.Scrollbar(frame_homework_list,
                       orient='vertical', command=canvas.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scroll.set)
canvas_interior = tk.Frame(canvas, bg='blue')
canvas.create_window((0, 0), window=canvas_interior, anchor='nw')
canvas_interior.bind('<Configure>', lambda e: canvas.configure(
    scrollregion=canvas.bbox('all')))

canvas_window = canvas.create_window(
    (0, 0), window=canvas_interior, anchor='nw')


def ajustar_largura(event):
    # Ajusta a largura do canvas_interior para a largura atual do canvas
    canvas.itemconfig(canvas_window, width=event.width)


# Bind para ajustar o tamanho dinamicamente
canvas.bind("<Configure>", ajustar_largura)

# vendo se minha janela está funcionando
window.mainloop()
