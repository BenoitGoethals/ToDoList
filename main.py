# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter.messagebox import showinfo

import ToDo as ToDo
from tkinter import *

toDos = []


def add(todo: ToDo):
    toDos.append(todo)


def delete(todo):
    toDos.remove(todo)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    root.geometry('600x600')

    listbox_widget = Listbox(root)
    listbox_widget.config(height=300, width=300)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # create a list box

    listbox = Listbox(
        root,

        height=6,
        selectmode='extended')

    listbox.grid(
        column=0,
        row=0,
        sticky='nwes',
        columnspan=2
    )

    # link a scrollbar to a list
    scrollbar = Scrollbar(
        root,
        orient='vertical',
        command=listbox.yview
    )

    listbox['yscrollcommand'] = scrollbar.set

    scrollbar.grid(
        column=1,
        row=0,
        sticky='ns')

    but_add = Button(text="Add")
    but_add.grid(
        column=0, columnspan=2,
        row=1
    )
    but_delete = Button(text="Delete")
    but_delete.grid(
        column=1,
        row=1, columnspan=2
    )



    # handle event

    def items_selected(event):
        """ handle item selected event
        """
        # get selected indices
        selected_indices = listbox.curselection()
        # get selected items
        selected_langs = ",".join([listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'

        showinfo(
            title='Information',
            message=msg)


    listbox.bind('<<ListboxSelect>>', items_selected)

    to = ToDo.ToDoItem(id_todo=1, description="dfdsf", start="sdf", end="dfdfssf", done=False)

    toDos.append(to)
    listbox.insert(END,to)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
