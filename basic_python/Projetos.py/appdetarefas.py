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
        tarefas_adicionadas.append(tarefa)
        # criando uma label no canvas interior
        label_tarefa = tk.Label(canvas_interior, text=tarefa, font=(
            'Garamond', 16), bg='red', fg='#333', width=40, height=40, anchor='w')
        label_tarefa.pack(side=tk.TOP, expand=True,
                          fill=tk.X, padx=10, pady=10)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning(
            'Entrada inválida', 'Por favor, insira sua tarefa!')
    edit_buttom = tk.Button(label_tarefa, image=icon_edit,
                            command=lambda idx=len(tarefas_adicionadas)-1, l=label_tarefa: editar_tarefa(idx, l), bg='white', relief=tk.FLAT)
    edit_buttom.pack(side=tk.RIGHT, padx=5, pady=5)
    delete_buttom = tk.Button(label_tarefa, image=icon_delete,
                              command=lambda: deletar_tarefa(), bg='white', relief=tk.FLAT)
    delete_buttom.pack(side=tk.RIGHT, padx=5)
    check_button = tk.Button(label_tarefa, image=icon_check,
                             command=lambda: check_tarefa(), bg='white', relief=tk.FLAT)
    check_button.pack(side=tk.RIGHT, padx=5)

    def editar_tarefa(indice, label):
        tarefa_antiga = tarefas_adicionadas[indice]

        # remove o label atual
        label_tarefa.pack_forget()

        # cria um entry pra editar a tarefa
        entry_edit = tk.Entry(canvas_interior, bg='white')
        entry_edit.insert(0, tarefa_antiga)
        entry_edit.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # troca o botão editar pelo de salvar
        salvar_button = tk.Button(
            canvas_interior, text="Salvar", command=lambda: salvar_edicao(entry_edit, indice))
        salvar_button.pack(side=tk.RIGHT)

        def salvar_edicao(entry_edit, indice):
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
            label_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def deletar_tarefa():
        print("michikola")

    def check_tarefa():
        print('check')


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

# criando um frame pra lista de tarefas com rolagem
frame_homework_list = tk.Frame(window, bg='purple')
frame_homework_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


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

# vendo se mainha janela está funcionando
window.mainloop()
