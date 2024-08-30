import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

#  criando a janela
window = tk.Tk()
window.title('Meu App de Tarefas')
window.configure(bg='#F0F0F0')
window.geometry('500x600')

# criando o Título do app
font_header = font.Font(family='Garamond', size=24, weight='bold')
label_header = tk.Label(window, text='Meu App de Tarefas',
                        font=font_header, bg='#F0F0F0', fg='#333').pack(pady=20)

# criando a caixa de entrada
frame = tk.Frame(window, bg='#F0F0F0').pack(pady=10)
entry = tk.Entry(frame, font=('Garamond', 14),
                 relief=tk.FLAT, bg='white', fg='grey', width=30)
entry.pack(side=tk.LEFT, padx=10)

# criando o botão de entrada
entry_button = tk.Button(frame, text='Adicionar Tarefa',
                         bg='#4CAF50', fg='white', height=1, width=15, font=('Roboto', 11), relief=tk.FLAT)
entry_button.pack(side=tk.LEFT, padx=10)

# criando um frame pra lista de tarefas com rolagem
frame_homework_list = tk.Frame(window, bg='white')
frame_homework_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_homework_list, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# vendo se mainha janela está funcionando
window.mainloop()
