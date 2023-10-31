from pathlib import Path
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

from database import DataBase


class Application(tk.Frame):

    file_name = ""

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        self.create_main_data_form()
        self.create_submit()

    def create_main_data_form(self):
        self.master.title('Trabalho Python')
        self.master.resizable(False, False)

        title = tk.Label(self, text="Dados Principais", font = ("Arial", 12))
        title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
   
        nome = tk.Label(self, text="Nome: ")
        nome.grid(row=1, column = 0, padx=10)
        self.data_nome = tk.Entry(self, width=30)
        self.data_nome.grid(row=1, column = 1)

        idade = tk.Label(self, text="Idade: ")
        idade.grid(row=2, column = 0)
        self.idade = tk.Entry(self, width=30)
        self.idade.grid(row=2, column = 1)

        cidade = tk.Label(self, text="Cidade: ")
        cidade.grid(row=3, column = 0)
        self.cidade = tk.Entry(self, width=30)
        self.cidade.grid(row=3, column = 1)

        estado = tk.Label(self, text="Estado: ")
        estado.grid(row=4, column = 0)
        self.estado = tk.Entry(self, width=30)
        self.estado.grid(row=4, column = 1)

        telefone = tk.Label(self, text="Telefone: ")
        telefone.grid(row=5, column = 0)
        self.telefone = tk.Entry(self, width=30)
        self.telefone.grid(row=5, column = 1)

        email = tk.Label(self, text="E-mail: ")
        email.grid(row=6, column = 0)
        self.email = tk.Entry(self, width=30)
        self.email.grid(row=6, column = 1)

        title = tk.Label(self, text="Experiências", font = ("Arial", 12))
        title.grid(row=7, column = 0, columnspan=2, pady=10, padx=10)
   
        trabalhos = tk.Label(self, text="Trabalhos anteriores: ")
        trabalhos.grid(row=8, column = 0)
        self.trabalho = tk.Entry(self, width=30)
        self.trabalho.grid(row=8, column = 1)

        soft_skills = tk.Label(self, text="Soft Skills: ")
        soft_skills.grid(row=9, column = 0)
        self.soft_skills = tk.Entry(self, width=30)
        self.soft_skills.grid(row=9, column = 1)

        hard_skills = tk.Label(self, text="Hard Skills: ")
        hard_skills.grid(row=10, column = 0)
        self.hard_skills = tk.Entry(self, width=30)
        self.hard_skills.grid(row=10, column = 1)

        likedin = tk.Label(self, text="linkedin: ")
        likedin.grid(row=11, column = 0)
        self.likedin = tk.Entry(self, width=30)
        self.likedin.grid(row=11, column = 1)

        self.experiencias_form_title = tk.Label(self, text="Empregabilidade", font = ("Arial", 12))
        self.experiencias_form_title.grid(row=12, column = 0, columnspan=2, pady=10, padx=10)

        label = tk.Label(self, text="Status atual de emprego: ")
        label.grid(row=13, column = 0)
        self.status = tk.Entry(self, width=30)
        self.status.grid(row=13, column = 1)

        label = tk.Label(self, text="Expectativa salarial: ")
        label.grid(row=14, column = 0)
        vcmd = (self.register(self.expectativa_validate))
        self.expectativa = tk.Entry(self, width=30, validate='all', validatecommand=(vcmd, '%P'))
        self.expectativa.grid(row=14, column = 1)

        label = tk.Label(self, text="Outras informações: ")
        label.grid(row=15, column = 0)
        self.outras = tk.Entry(self, width=30)
        self.outras.grid(row=15, column = 1, columnspan=2)

        label = tk.Label(self, text="Curriculo: ")
        label.grid(row=16, column = 0)

        self.file_button = tk.Button(self, text='Selecionar arquivo', command=self.file_clicked)
        self.file_button.grid(row=16, column = 1)


        label = tk.Label(self, text="Área de Atuação: ")
        label.grid(row=17, column = 0)

        selected_area = tk.StringVar()
        self.area_cb = ttk.Combobox(self,
                                    textvariable=selected_area, values=["comercial", "atendimento", "outra"],
                                    state='readonly',
                                    )
        self.area_cb.grid(row=17, column = 1, pady=10)


    def expectativa_validate(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def file_clicked(self):
        filetypes = (
        ('PDF files', '*.pdf'),
        ('DOC files', '*.doc'),
        ('DOCX files', '*.docx'),
    )

        file_name = filedialog.askopenfilename(
            title='Abrir arquivo',
            initialdir='/',
            filetypes=filetypes)
        
        if file_name:
            self.file_name = file_name
            self.file_button.config(text= self.file_name)

    def submit_clicked(self):
        if self.file_name:
            p = Path(self.file_name)
            arquivo = p.name
            bin = p.read_bytes()
        else:
            arquivo = bin = ""
        self.data = {
            "nome": self.data_nome.get(),
            "idade": self.idade.get(),
            "cidade": self.cidade.get(),
            "estado": self.estado.get(),
            "telefone": self.telefone.get(),
            "email": self.email.get(),
            "trabalhos_anteriores": self.trabalho.get(),
            "soft_skills": self.soft_skills.get(),
            "hard_skills": self.hard_skills.get(),
            "likedin": self.likedin.get(),
            "status": self.status.get(),
            "expectativa": self.expectativa.get() or 0,
            "outras": self.outras.get(),
            "area": self.area_cb.get() or "outra",
            "arquivo": arquivo,
            "bin": bin,
            "recrutador": "em espera",
        }

        self.db.insert(**self.data)
        
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

        self.file_button.config(text="Selecionar arquivo")
        self.file_name = ""        

        messagebox.showinfo(title='Dados', message="Dados submetidos com sucesso!")

    def create_submit(self):
        self.button = tk.Button(self, text='Submeter', command=self.submit_clicked, font=("Arial", 12))
        self.button.grid(column=0, columnspan=2, pady=(30, 0), padx=10)
    
    def start(self):
        self.db = DataBase()
        self.mainloop()
        self.db.con.close()


if __name__ == "__main__":
    db = DataBase()
    db.select()
    app = Application()
    app.start()
    db.select()
