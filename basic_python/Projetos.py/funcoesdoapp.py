# fazer uma função para cada ação do to do (adicionar_tarefa, atualizar_tarefa, concluir_tarefa, deletar_tarefa)
import tkinter as tk
from appdetarefas import label_tarefa, canvas_interior, tarefas_adicionadas


def editar_tarefa(tarefas_adicionadas):
    print("entrei aqui")
    # global label_tarefa
    # # remove o label atual
    # label_tarefa.pack_forget()

    # # cria um entry pra editar a tarefa
    # entry_edit = tk.Entry(canvas_interior, bg='white')
    # entry_edit.insert(0)
    # entry_edit.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # # troca o botão editar pelo de salvar
    # salvar_button = tk.Button(
    #     canvas_interior, text="Salvar", command=lambda: salvar_edicao(entry_edit))
    # salvar_button.pack(side=tk.RIGHT)


def salvar_edicao(entry_edit):
    global tarefas_adicionadas
    # Obtém o novo texto do Entry
    nova_tarefa = entry_edit.get()

    # Atualiza a lista de tarefas
    tarefas_adicionadas = nova_tarefa

    # Atualiza o Label com o novo texto
    label_tarefa.config(text=nova_tarefa)

    # Remove o Entry e exibe o Label novamente
    entry_edit.pack_forget()
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True)


def concluir_tarefa():
    print("michikola")


def deletar_tarefa():
    print("michikola")
