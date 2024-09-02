import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

#  criando a janela
window = tk.Tk()
window.title('Meu App de Tarefas')
window.configure(bg='#F0F0F0')
window.geometry('500x600')

# Função pra adicionar tarefa
tarefas_adicionadas = []

def adicionar_tarefa():
    tarefa = entry.get()
    if tarefa in tarefa != '':
        tarefas_adicionadas.append(tarefa)
        # criando uma label no canvas interior
        label_tarefa = tk.Label(canvas_interior, text=tarefa, font=(
            'Garamond', 16), bg='red', fg='#333', width=25, height=2, anchor='w')
        label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning(
            'Entrada inválida', 'Por favor, insira sua tarefa!')
    
    # edit_buttom = tk.Button(frame_homework_list, image=icon_edit,
    #                         command=lambda f=frame_homework_list, l=label_tarefa: preparar_edicao(f, l), bg='white', relief=tk.FLAT)
    # edit_buttom.pack(side=tk.RIGHT, padx=5)
    # delete_buttom = tk.Button(frame_homework_list, image=icon_delete,
    #                           command=lambda f=frame_homework_list: deletar_tarefa(f), bg='white', relief=tk.FLAT)
    # delete_buttom.pack(side=tk.RIGHT, padx=5)
    # frame_homework_list.pack(fill=tk.X, padx=5, pady=5)


# icon_edit = PhotoImage('edit.png'.subsample(3, 3))
# icon_delete = PhotoImage('detele.png'.subsample(3, 3))


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
entry_button = tk.Button(frame, text='Adicionar Tarefa', command=adicionar_tarefa,
                         bg='#4CAF50', fg='white', height=1, width=15, font=('Roboto', 11), relief=tk.FLAT)
entry_button.pack(side=tk.LEFT, padx=10)

# criando um frame pra lista de tarefas com rolagem
frame_homework_list = tk.Frame(window, bg='white')
frame_homework_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_homework_list, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# fazendo o scroll agora
scroll = ttk.Scrollbar(frame_homework_list,
                       orient='vertical', command=canvas.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scroll.set)
canvas_interior = tk.Frame(canvas, bg='white')
canvas.create_window((0, 0), window=canvas_interior, anchor='nw')
canvas_interior.bind('<Configure>', lambda e: canvas.configure(
    scrollregion=canvas.bbox('all')))


# vendo se mainha janela está funcionando
window.mainloop()
