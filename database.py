from pathlib import Path
import sqlite3

p = Path(".")

DB_FILE = p / "data.db"


class DataBase():

    def __init__(self):
        self.con = sqlite3.connect(DB_FILE)
        self.create_tables()

    def execute(self, *args, **kwargs):
        cur = self.con.cursor()
        cur.execute(*args, **kwargs)
        cur.close()
        self.con.commit()

    def create_tables(self):
        ddl = """
        CREATE TABLE IF NOT EXISTS dados (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
   	    nome TEXT,
        idade TEXT,
        cidade TEXT,
        estado TEXT,
        telefone TEXT,
        email TEXT,
        trabalhos_anteriores TEXT,
        soft_skills TEXT,
        hard_skills TEXT,
        likedin TEXT,
        status TEXT,
        expectativa INTEGER,
        outras TEXT,
        area TEXT,
        arquivo TEXT,
        bin BLOB,
        recrutador TEXT
        );
        """
        cur = self.con.cursor()
        cur.execute(ddl)
        cur.close()
        self.con.commit()

    def insert(self,
               nome="",
               idade="",
               cidade="",
               estado="",
               telefone="",
               email="",
               trabalhos_anteriores="",
               soft_skills="",
               hard_skills="",
               likedin="",
               status="",
               expectativa=0,
               outras="",
               area="",
               arquivo="",
               bin=b"",
               recrutador="",
               ):
        
        sql_stm = f"""
                  INSERT INTO dados
                  (nome, idade, cidade, estado, 
                   telefone, email, trabalhos_anteriores,
                   soft_skills, hard_skills, likedin, status,
                   expectativa, outras, area, arquivo, bin, recrutador)
                  VALUES
                  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                  """
        data = (nome, idade, cidade, estado, 
                   telefone, email, trabalhos_anteriores,
                   soft_skills, hard_skills, likedin, status,
                   expectativa, outras, area, arquivo, bin, recrutador)
        self.execute(sql_stm, data)
        
    def select(self, col=""):

        col = col or "id, expectativa, area, arquivo, recrutador"
        cur = self.con.cursor()
        res = cur.execute(f"SELECT {col} FROM dados;")
        print(res.fetchall())
        cur.close()
    
    def query(self, stm):
        cur = self.con.cursor()
        res = cur.execute(stm)
        data = res.fetchall()
        cur.close()
        return data

