#CREATE = CRIAR TABELA
#INSERT = INSERIR
#UPDATE = ATUALIZAR
#DELETE = DELETAR
#SELECT = PROCURAR 

import sqlite3

#---------------AQUI ELE INICIA A CRIAÇÃO DO BANCO DE DADOS CASO ELE NÃO EXISTA !!---------------#
connection = sqlite3.connect('CRUD.db')
cursor = connection.cursor()
sql1 = '''
CREATE TABLE IF NOT EXISTS professor (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        cpf TEXT NOT NULL,
                        departament TEXT NOT NULL)'''
cursor.execute(sql1)
connection.commit()

sql2 = '''
CREATE TABLE IF NOT EXISTS aluno (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     cpf TEXT NOT NULL)'''
cursor.execute(sql2)
connection.commit()

sql3 = '''
CREATE TABLE IF NOT EXISTS disciplina (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         cod_disciplina TEXT NOT NULL)'''
cursor.execute(sql3)
connection.commit()

sql4 = '''
CREATE TABLE IF NOT EXISTS turma(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   cod_turma TEXT NOT NULL,
                   periodo TEXT NOT NULL,
                   cod_disciplina TEXT NOT NULL,
                   cpf_professor TEXT,
                   cpf_aluno TEXT)'''
cursor.execute(sql4)
connection.commit()

connection.close()

class Professor(): 

    def __init__(self):
        pass

    def Create_professor(self, name, cpf, department):
        self.name = name.upper()
        self.cpf = cpf
        self.department = department.upper()

        def Analyzer(self):
            self.connection = sqlite3.connect('CRUD.db')
            self.cursor = self.connection.cursor()
            self.sql = 'SELECT * FROM professor'
            self.condition_add = True

            for self.row in self.cursor.execute(self.sql):
                if (self.row [2] == self.cpf):
                    self.condition_add = False
                    break
            
            if (self.condition_add == True):
                self.cursor.execute('''INSERT INTO professor (name, cpf, departament) VALUES (?, ?, ?)''',
                                 (self.name, self.cpf, self.department))
                self.connection.commit()
                self.connection.close()
                            

        Analyzer(self)

          #ESTA FUNÇÃO IRÁ SER RETIRADA

        

class Aluno(object):
    def __init__(self):
        pass

    def Create_aluno(self, name, cpf):
        self.name = name.upper()
        self.cpf = cpf

        def Analyzer():
            self.connection = sqlite3.connect('CRUD.db')
            self.cursor = self.connection.cursor()
            self.sql = 'SELECT * FROM aluno'
            self.condition_add = True

            for self.row in self.cursor.execute(self.sql):
                if (self.cpf == self.row[2]):
                   self.condition_add = False
                   break
            
            if (self.condition_add == True):
                self.cursor.execute('''INSERT INTO aluno (name, cpf) VALUES (?, ?)''',
                                 (self.name, self.cpf))
                self.connection.commit()
                self.connection.close()
        
        Analyzer()



class Disciplina(object):
    def __init__(self):
        pass
    
    def Create_disciplina(self, name, cod):
        self.cod = cod
        self.name = name.upper()

        def Analyzer():
            self.connection = sqlite3.connect('CRUD.db')
            self.cursor = self.connection.cursor()
            self.sql = 'SELECT * FROM disciplina '
            self.condition_add = True

            for self.row in self.cursor.execute(self.sql):
                if (self.cod == self.row[2] or self.name == self.row[1]):
                   self.condition_add = False
                   break
            
            if (self.condition_add == True):
                self.cursor.execute('''INSERT INTO disciplina (name, cod_disciplina) VALUES (?, ?)''',
                                 (self.name, self.cod))
                self.connection.commit()
                self.connection.close()
        
        Analyzer()
    



class Turma(object):
    def __init__(self, cod_turma, periodo, cod_disciplina):
        self.cod_turma = cod_turma
        self.periodo = periodo
        self.cod_disciplina = cod_disciplina
        
    
    def Create(self):
        pass
    
    def Read(self):
        pass
    

    def Update(self):
        pass

    def Delete(self):
        pass

'''
Alexandre = Aluno()
Alexandre.Delete_aluno('123')'''