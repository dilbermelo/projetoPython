from pathlib import Path
import sys
import os
import tkinter as tk
from tkinter import ttk

p = Path(__file__).parent
sys.path.insert(0, str(p))

from database import DataBase

class DataForm(tk.Frame):
    
    def __init__(self, master=None, data=None):
        self.data = data
        self.db = DataBase()
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=1, padx=20, pady=20)
        self.create_widgets()
    
    def create_widgets(self):
        data = self.data

        title = tk.Label(self, text="Dados Principais", font = ("Arial", 12))
        title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

   
        nome = tk.Label(self, text="Nome: ")
        nome.grid(row=1, column = 0, padx=10)
        self.data_nome = tk.Label(self, text=data["nome"], width=30)
        self.data_nome.grid(row=1, column = 1)

        idade = tk.Label(self, text="Idade: ")
        idade.grid(row=2, column = 0)
        self.idade = tk.Label(self, text=data["idade"], width=30)
        self.idade.grid(row=2, column = 1)

        cidade = tk.Label(self, text="Cidade: ")
        cidade.grid(row=3, column = 0)
        self.cidade = tk.Label(self, text=data["cidade"], width=30)
        self.cidade.grid(row=3, column = 1)

        estado = tk.Label(self, text="Estado: ")
        estado.grid(row=4, column = 0)
        self.estado = tk.Label(self, text=data["estado"], width=30)
        self.estado.grid(row=4, column = 1)

        telefone = tk.Label(self, text="Telefone: ")
        telefone.grid(row=5, column = 0)
        self.telefone = tk.Label(self, text=data["telefone"], width=30)
        self.telefone.grid(row=5, column = 1)

        email = tk.Label(self, text="E-mail: ")
        email.grid(row=6, column = 0)
        self.email = tk.Label(self, text=data["email"], width=30)
        self.email.grid(row=6, column = 1)

        title = tk.Label(self, text="Experiências", font = ("Arial", 12))
        title.grid(row=7, column = 0, columnspan=2, pady=10, padx=10)
   
        trabalhos = tk.Label(self, text="Trabalhos anteriores: ")
        trabalhos.grid(row=8, column = 0)
        self.trabalho = tk.Label(self, text=data["trabalhos_anteriores"], width=30)
        self.trabalho.grid(row=8, column = 1)

        soft_skills = tk.Label(self, text="Soft Skills: ")
        soft_skills.grid(row=9, column = 0)
        self.soft_skills = tk.Label(self, text=data["soft_skills"], width=30)
        self.soft_skills.grid(row=9, column = 1)

        hard_skills = tk.Label(self, text="Hard Skills: ")
        hard_skills.grid(row=10, column = 0)
        self.hard_skills = tk.Label(self, text=data["hard_skills"], width=30)
        self.hard_skills.grid(row=10, column = 1)

        likedin = tk.Label(self, text="linkedin: ")
        likedin.grid(row=11, column = 0)
        self.likedin = tk.Label(self, text=data["likedin"], width=30)
        self.likedin.grid(row=11, column = 1)

        self.experiencias_form_title = tk.Label(self, text="Empregabilidade", font = ("Arial", 12))
        self.experiencias_form_title.grid(row=12, column = 0, columnspan=2, pady=10, padx=10)

        label = tk.Label(self, text="Status atual de emprego: ")
        label.grid(row=13, column = 0)
        self.status = tk.Label(self, text=data["status"], width=30)
        self.status.grid(row=13, column = 1)

        label = tk.Label(self, text="Expectativa salarial: ")
        label.grid(row=14, column = 0)
        self.expectativa = tk.Label(self, text=data["expectativa"], width=30)
        self.expectativa.grid(row=14, column = 1)

        label = tk.Label(self, text="Outras informações: ")
        label.grid(row=15, column = 0)
        self.outras = tk.Label(self, text=data["outras"], width=30)
        self.outras.grid(row=15, column = 1, columnspan=2)

        label = tk.Label(self, text="Curriculo: ")
        label.grid(row=16, column = 0)

        self.file_button = tk.Button(self, text='Abrir arquivo', command=self.abrir_arquivo)
        self.file_button.grid(row=16, column = 1)


        label = tk.Label(self, text="Área de Atuação: ")
        label.grid(row=17, column = 0)

        self.area_cb = tk.Label(self, text=data["area"], width=30)
        self.area_cb.grid(row=17, column = 1, pady=10)


        label = tk.Label(self, text="Status do recutamento: ")
        label.grid(row=18, column = 0)
        values = ["em espera", "aprovado", "reprovado"]
        self.recrutador = ttk.Combobox(self,
                                    values=values,
                                    state='readonly',
                                    )
        self.recrutador.grid(row=18, column=1)
        self.recrutador.current(values.index(data["recrutador"]))
        self.recrutador.bind("<<ComboboxSelected>>", self.recrutador_update)
    
    def recrutador_update(self, event):
        recrutador = self.recrutador.get()
        idx = self.data["id"]
        db.execute(f"UPDATE dados SET recrutador=? WHERE id=?", (recrutador, idx))


    
    def abrir_arquivo(self):
        nome = self.data["arquivo"]
        bin = self.data["bin"]
        if not nome:
            return
        
        p = Path(__file__).parent / f"temp{Path(nome).suffix}"
        p.write_bytes(bin)

        os.startfile(str(p))




class Application(tk.Frame):


    def __init__(self, master=None, db=None):
        self.db = DataBase()
        tk.Frame.__init__(self, master)
        self.grid(padx=20, pady=20)
        self.create_widgets()


    def create_widgets(self):
        self.master.title('Trabalho Python')
        self.master.resizable(False, False)

        title = tk.Label(self, text="Recrutador", font = ("Arial", 12))
        title.grid(column=0, pady=10, padx=10)


        cidades_data = ["todas"] + self.get_cidades()
        nome = tk.Label(self, text="Filtro Cidades")
        nome.grid(column = 0, padx=10)
        self.cidade = ttk.Combobox(self,
                                    values=cidades_data,
                                    state='readonly',
                                    )
        self.cidade.current(0)
        self.cidade.grid(pady=10)
        self.cidade.bind("<<ComboboxSelected>>", self.cidade_selected)


        estados_data = ["todos"] + self.get_estados()
        nome = tk.Label(self, text="Filtro Estados")
        nome.grid(column = 0, padx=10)
        self.estado = ttk.Combobox(self,
                                    values=estados_data,
                                    state='readonly',
                                    )
        self.estado.current(0)
        self.estado.grid(pady=10)
        self.estado.bind("<<ComboboxSelected>>", self.estado_selected)


        expectativas_data = ["todas"] + self.get_expectativas()
        nome = tk.Label(self, text="Filtro Expectativa Salarial")
        nome.grid(column = 0, padx=10)
        self.expectativa = ttk.Combobox(self,
                                    values=expectativas_data,
                                    state='readonly',
                                    )
        self.expectativa.current(0)
        self.expectativa.grid(pady=10)
        self.expectativa.bind("<<ComboboxSelected>>", self.expectativa_selected)
   
        areas_data = ["todas"] + self.get_areas()
        nome = tk.Label(self, text="Filtro Areas de Trabalho")
        nome.grid(column = 0, padx=10)
        self.area = ttk.Combobox(self,
                                    values=areas_data,
                                    state='readonly',
                                    )
        self.area.current(0)
        self.area.grid(pady=10)
        self.area.bind("<<ComboboxSelected>>", self.area_selected)


        nome = tk.Label(self, text="Candidatos")
        nome.grid(column = 0, padx=10)

        self.listbox = tk.Listbox(self)
        data = self.get_list_candidatos()
        self.listbox.insert(0, *data) 
        self.listbox.grid(column = 0)
        self.listbox.bind("<<ListboxSelect>>", self.open_frame)


    def get_data(self):
        return self.db.query("SELECT * FROM dados;")
    
    def get_list_candidatos(self):
        data = self.db.query("SELECT id, nome FROM dados")
        return [f"{id} {nome}" for id, nome in data]

    def get_cidades(self):
        data = self.db.query("SELECT cidade FROM dados;")
        data = list(set(var[0] for var in data))
        return data

    def get_estados(self):
        data = self.db.query("SELECT estado FROM dados;")
        data = list(set(var[0] for var in data))
        return data

    def get_areas(self):
        data = self.db.query("SELECT area FROM dados;")
        data = list(set(var[0] for var in data))
        return data

    def get_expectativas(self):
        data = self.db.query("SELECT expectativa FROM dados;")
        data = list(set(var[0] for var in data))
        return data

    def cidade_selected(self, x):
        self.estado.current(0)
        self.area.current(0)
        self.expectativa.current(0)
        cidade = self.cidade.get()
        if cidade == "todas":
            self.manage_cbox()
            return
        data = self.db.query(f"SELECT id, nome FROM dados WHERE cidade = '{cidade}';")
        data = [f"{id} {nome}" for id, nome in data]
        self.listbox.delete(0, tk.END)
        self.listbox.insert(0, *data)

    def estado_selected(self, x):
        self.cidade.current(0)
        self.expectativa.current(0)
        self.area.current(0)
        estado = self.estado.get()
        if estado == "todos":
            self.manage_cbox()
            return
        data = self.db.query(f"SELECT id, nome FROM dados WHERE estado = '{estado}';")
        data = [f"{id} {nome}" for id, nome in data]
        self.listbox.delete(0, tk.END)
        self.listbox.insert(0, *data)

    def area_selected(self, x):
        self.cidade.current(0)
        self.expectativa.current(0)
        self.estado.current(0)
        area = self.area.get()
        if area == "todas":
            self.manage_cbox()
            return
        data = self.db.query(f"SELECT id, nome FROM dados WHERE area = '{area}';")
        data = [f"{id} {nome}" for id, nome in data]
        self.listbox.delete(0, tk.END)
        self.listbox.insert(0, *data)

    def expectativa_selected(self, x):
        self.cidade.current(0)
        self.area.current(0)
        self.estado.current(0)
        expectativa = self.expectativa.get()
        if expectativa == "todas":
            self.manage_cbox()
            return
        data = self.db.query(f"SELECT id, nome FROM dados WHERE expectativa = '{expectativa}';")
        data = [f"{id} {nome}" for id, nome in data]
        self.listbox.delete(0, tk.END)
        self.listbox.insert(0, *data)

    def manage_cbox(self):
        self.listbox.delete(0, tk.END)
        data = self.get_list_candidatos()
        self.listbox.insert(0, *data)

    def start(self):
        self.mainloop()
        self.db.con.close()

    def open_frame(self, event):
        selection = event.widget.curselection()
        if not selection:
            return
        selection = event.widget.get(selection[0]).split()[0]
        
        res = self.db.query(f"SELECT * FROM dados WHERE id = {selection};")[0]
        cols = ["id", "nome", "idade", "cidade", "estado", "telefone", "email",
                "trabalhos_anteriores", "soft_skills", "hard_skills", "likedin",
                "status", "expectativa", "outras", "area", "arquivo", "bin", "recrutador" ]
        data = {k:v for k, v in zip(cols, res)}
        DataForm(data=data)

if __name__ == "__main__":
    db = DataBase()
    db.select()
    app = Application()
    app.start()
    db.select()
