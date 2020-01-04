from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from BANCO import *
import sqlite3

#LINK INTERESSANTE : https://www.pycursos.com/tkinter-sqlite3/

class Loginwindow:
    def __init__(self, master = None):
        self.master = master
        self.login_window = Toplevel()
        self.login_window.title('TELA DE LOGIN')
        self.login_window.geometry('350x120')
        self.login_window.resizable(False,False)
        self.login_window.iconbitmap('logo.ico')

        self.label1 = Label(self.login_window, text = 'Login', font = 'Times').grid(row = 0, column = 1, sticky = N)
        self.label2 = Label(self.login_window, text = 'Usuário :', font = 'Times, 12').grid(row = 1, column = 0)
        self.label3 = Label(self.login_window, text = 'Senha :', font = 'Times, 12').grid(row = 2, column = 0)
        self.label4 = Label(self.login_window, text = '(Padrão: admin)', font = 'Times, 12').grid(row = 1, column = 2, sticky = E)
        self.label5 = Label(self.login_window, text = '(Padrão: root)', font = 'Times, 12').grid(row = 2, column = 2, sticky = E)
        

        self.username = Entry(self.login_window, font = 'Times, 10')
        self.username.grid(row=1, column = 1)
        self.username.focus_force()

        self.password = Entry(self.login_window, font = 'Times, 10', show = '*')
        self.password.grid(row=2, column = 1)

        self.but = Button(self.login_window, text = 'ENTRAR', font = "Times, 10", command = self.Verification_password)
        self.but.grid(row=3, column=1, rowspan=2, sticky = S)


        self.incorrect_password = Label(self.login_window, text = '', font = 'Times, 8')
        self.incorrect_password.grid(row = 4, column = 2, sticky = W)

        self.login_window.mainloop()
    
    
    def Verification_password(self):
        username = self.username.get()
        password = self.password.get()


        if (username == 'admin' and password == 'root'):
            self.master.destroy()
            
            try:
                Mainwindow()
            
            except:
                raise Exception ('Deu erro no Mainwindow')

        
        else:
            self.incorrect_password["text"] = 'Login/Senha incorreto(a)' 
            self.incorrect_password["fg"] = 'red'

class Initialwindow:

    def Create_login(self):
        try:
            Loginwindow(self.root)

        
        except:
            raise Exception ('Deu erro no Loginwindow')


    def __init__(self, master = None):
        
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('700x600+220+80')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root['bg'] = 'white'


        self.root.iconbitmap('logo.ico')
        self.root.title('PROJETO DE INTRODUÇÃO À PROGRAMAÇÃO')
        self.img = ImageTk.PhotoImage(Image.open('UFRPE.jpeg'))
        self.panel = Label(self.root, image = self.img)
        self.panel.grid(row=0, column = 0)
        

        self.label1 = Label(self.root, text = 'Projeto - Sistema de Controle Acadêmico Simplificado', font = 'Times, 20', bg = 'white').grid(row = 1, column = 0, sticky = W+E, padx = 30)
        self.label2 = Label(self.root, text = 'UFRPE', font = 'Times, 20', bg = 'white').grid(row = 2, column = 0, sticky = W+E, padx = 30)
        self.label3 = Label(self.root, text = 'Clique abaixo para efetuar o login e continuar', font = 'Times, 14', bg = 'white').grid(row = 3, column = 0, sticky = W+E, padx = 30)
        
        self.but = Button(self.root, text = 'LOGIN', bg = 'white', command = self.Create_login)
        self.but.configure(width = 10, height = 1)
        self.but.grid(row=4, column=0, columnspan=2, sticky='N', pady=30)

        self.label4 = Label(self.root, text = 'Developed by Alexandre Marques', font = 'Arial, 10', fg = 'red4', bg = 'white').place(x = 280, y = 560)



        self.root.mainloop()

class Mainwindow:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('525x525+220+80')
        self.root.protocol('WM_DELETE_WINDOW')

        self.root.title('Sistema de Controle Acadêmico Simplificado')
        self.label1 = Label(self.root, text = 'Bem-vindo!! ', font = 'bold')
        self.label1.place(x = 225, y = 5)

        self.label2 = Label(self.root, text = '=> Funções do sistema listadas acima.', font = 'bold').place(x = 0, y = 45)
        
        self.label3 = Label(self.root, text = '=> Para gerar ATA, clique no botão abaixo: ', font = 'bold').place(x = 0, y = 90)

        self.but = Button(self.root, text = 'Gerador de ATA', font = 'bold', width = 20, command = self.Gerador_ata).place(x = 180, y = 200)

        self.text_help = '''Qualquer dúvida entre em contato por:\n\nE-mail: alexandre-ft2@hotmail.com\n\nWhatsapp: (81) 98407-3151'''
        
        self.label4 = Label(self.root, text = self.text_help, font = 'bold').place(x = 130, y = 400)


        #----------------------AQUI-ENCONTRA-SE-OS-LABELS-DO-MENU-----------------------------
        self.menu_bar = Menu(self.root)
        self.menu_bar.add_separator()


        self.teacher_menu = Menu(self.menu_bar, tearoff=0)
        self.teacher_menu.add_command(label = 'Adicionar professor', command = self.Create_teacher)
        self.teacher_menu.add_separator()
        self.teacher_menu.add_command(label = 'Procurar professor', command =  self.Read_teacher)
        self.teacher_menu.add_separator()
        self.teacher_menu.add_command(label = 'Atualizar professor', command = self.Update_teacher)
        self.teacher_menu.add_separator()
        self.teacher_menu.add_command(label = 'Deletar professor', command = self.Delete_teacher)
        self.menu_bar.add_cascade(label = 'Professor', menu = self.teacher_menu)


        self.menu_bar.add_separator()


        self.student_menu = Menu(self.menu_bar, tearoff = 0)
        self.student_menu.add_command(label = 'Adicionar aluno', command = self.Create_student)
        self.student_menu.add_separator()
        self.student_menu.add_command(label = 'Procurar aluno', command = self.Read_student)
        self.student_menu.add_separator()
        self.student_menu.add_command(label = 'Atualizar aluno', command = self.Update_student)
        self.student_menu.add_separator()
        self.student_menu.add_command(label = 'Deletar aluno', command = self.Delete_student)
        self.menu_bar.add_cascade(label = 'Aluno', menu = self.student_menu)

        self.menu_bar.add_separator()


        self.discipline_menu = Menu(self.menu_bar, tearoff = 0)
        self.discipline_menu.add_command(label = 'Adicionar disciplina', command = self.Create_discipline)
        self.discipline_menu.add_separator()
        self.discipline_menu.add_command(label = 'Procurar disciplina', command = self.Read_discipline)
        self.discipline_menu.add_separator()
        self.discipline_menu.add_command(label = 'Atualizar disciplina', command = self.Update_discipline)
        self.discipline_menu.add_separator()
        self.discipline_menu.add_command(label = 'Deletar disciplina', command = self.Delete_discipline)
        self.menu_bar.add_cascade(label = 'Disciplina', menu = self.discipline_menu)

        self.menu_bar.add_separator()

        self.class_menu = Menu(self.menu_bar, tearoff = 0)
        self.class_menu.add_command(label = 'Adicionar turma', command = self.Create_class)
        self.class_menu.add_separator()
        self.class_menu.add_command(label = 'Procurar turma', command = self.Read_class)
        self.class_menu.add_separator()
        self.class_menu.add_command(label = 'Atualizar turma', command = self.Update_class)
        self.class_menu.add_separator()
        self.class_menu.add_command(label = 'Deletar turma')
        self.menu_bar.add_cascade(label = 'Turma', menu = self.class_menu)

        self.menu_bar.add_separator()

        self.exit_program = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_command(label = 'Sair', command = self.Quit_window)

        self.root.configure(menu = self.menu_bar)


        self.root.mainloop()
        #------------------------------------------------------------------------------------
        
        
        self.root.mainloop()
    




    #--------------------------MESAGEBOX-DE-SAIDA----------------------------------------------
    def Quit_window(self):
        if messagebox.askokcancel('Fechar programa', 'Deseja realmente sair?'):
            self.root.destroy()
    #-------------------------------------------------------------------------------------------
    



    #---------------------------------FUNÇÕES-DO-MENU-DE-PROFESSORES-----------------------------

    def Create_teacher(self):
        try:
            Teacherinsert(Mainwindow)
        
        except:
            raise Exception('Deu erro no Teacherinsert')

    
    def Read_teacher(self):
        try:
            Teachersearch(Mainwindow)
        
        except:
            raise Exception ('Deu erro no Teachersearch')

    
    def Update_teacher(self):
        try:
            Teacherupdate(Mainwindow)
        
        except:
            raise Exception('Deu erro no Teacherupdate')

    
    def Delete_teacher(self):
        try:
            Teacherdelete(Mainwindow)
        
        except:
            raise Exception('Deu erro no Teacherdelete')
    
    
    #---------------------------------------------------------------------------------------








    #----------------------------------FUNÇÕES-DO-MENU-DE-ALUNOS-----------------------------

    def Create_student(self):
        try:
            Studentinsert(Mainwindow)
        
        except:
            raise Exception('Deu erro em Studentinsert')

    
    def Read_student(self):
        try:
            Studentsearch(Mainwindow)
        
        except:
            raise Exception('Deu erro no Studentsearch')

    
    def Update_student(self):
        try:
            Studentupdate(Mainwindow)

        except:
            raise Exception('Deu erro no Studentupdate')
    
    def Delete_student(self):
        try:
            Studentdelete(Mainwindow)
        
        except:
            raise Exception('Deu erro no Studentdelete')
    #-----------------------------------------------------------------------------------------







    #----------------------------FUNÇÕES-DO-MENU-DISCIPLINA-----------------------------------

    def Create_discipline(self):
        try:
            Disciplineinsert(Mainwindow)
        
        except:
            raise Exception('Deu erro em Disciplineinsert')

    
    def Read_discipline(self):
        try:
            Disciplinesearch(Mainwindow)
        
        except:
            raise Exception('Deu erro no Disciplinesearch')
    
    def Update_discipline(self):
        try:
            Disciplineupdate(Mainwindow)
        
        except:
            raise Exception('Deu erro no Disciplineupdate')
    
    def Delete_discipline(self):
        try:
            Disciplinedelete(Mainwindow)
        
        except:
            raise Exception('Deu erro no Disciplinedelete')
    #-----------------------------------------------------------------------------------------



    #--------------------------------FUNÇÕES-DO-MENU-TURMA------------------------------------

    def Create_class(self):
        try:
            Classinsert(Mainwindow)
        
        except:
            raise Exception('Deu erro no Classinsert')
    
    def Read_class(self):
        try:
            Classsearch(Mainwindow)
        
        except:
            raise Exception('Deu erro no Classsearch')
    
    def Update_class(self):
        try:
            Classupdate(Mainwindow)
        
        except:
            raise Exception('Deu erro no Classupdate')
    
    def Delete_class(self):
        try:
            Classdelete(Mainwindow)
        
        except:
            raise Exception('Deu erro no Classdelete')


    #-----------------------------------------------------------------------------------------


    def Gerador_ata(self):
        try:
            Gerador(Mainwindow)
        
        except:
            raise Exception('Deu erro no Gerador')


#-------------------------------------TODAS-AS-FUNÇÕES-DA-ABA-DE-PROFESSORES------------------------------

class Teacherinsert:
    

    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('430x250+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Cadastramento de professor')

        self.label_nome = Label(self.root, text = 'Nome (completo): ').place(x = 10, y = 20)
        self.name = Entry(self.root)
        self.name.focus_force()
        self.name.place(x = 170, y = 20)

        self.label_cpf = Label(self.root, text = 'CPF: ').place(x = 10, y = 60)
        self.cpf = Entry(self.root)
        self.cpf.place(x = 170, y= 60)

        self.label_depart = Label(self.root, text = 'Departamento: ').place(x = 10, y = 100)
        self.depart = Entry(self.root)
        self.depart.place(x = 170, y= 100)

        self.but = Button(self.root, text = 'CADASTRAR', command = self.Insert_teacher)
        self.but.place(x = 175, y = 170)

        self.status = Label(self.root, text = '')
        self.status.place(x = 155, y = 210)

        self.notname = Label(self.root, text = '', fg = 'red')
        self.notname.place(x = 300, y = 20)

        self.notcpf = Label(self.root, text = '', fg = 'red')
        self.notcpf.place(x = 300, y = 60)

        self.notdepar = Label(self.root, text = '', fg = 'red')
        self.notdepar.place(x = 300, y = 100)

        self.root.mainloop()
    
    def Insert_teacher(self):
        self.name2 = self.name.get()
        self.cpf2 = self.cpf.get()
        self.depart2 = self.depart.get()


        if (self.name2 != '' and self.cpf2 != '' and self.depart2 != ''):
            self.insert = Professor()
            self.insert.Create_professor(self.name2, self.cpf2, self.depart2)
            self.notname["text"] = ''
            self.notcpf["text"] = ''
            self.notdepar["text"] = ''

            if (self.insert.condition_add == True):
                self.status["fg"] = 'green'
                self.status["text"] = 'Cadastro feito !!'
                self.but["text"] = 'Sair'
                self.but['width'] = '10'
                self.but['command'] = self.Exit
                
        
            else:
                self.status["fg"] = 'red'
                self.status["text"] = 'Cadastro já existente!!'

        else:
            if(self.name2 == ''):
                self.notname["text"] = 'Item em branco!'
            
            else:
                self.notname["text"] = ''

            if(self.cpf2 == ''):
                self.notcpf["text"] = 'Item em branco!'
            
            else:
                self.notcpf["text"] = ''
            
            if (self.depart2 == ''):
                self.notdepar["text"] = 'Item em branco!'
            
            else:
                self.notdepar["text"] = ''
    
    def Exit(self):
        self.root.destroy()




class Teachersearch:
    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('800x500+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Pesquisador de professor')

        self.label_nome = Label(self.root, text = 'Nome completo (Deixe em branco para ver todos): ').pack()
        self.name = Entry(self.root)
        self.name.focus_force()
        self.name.pack()


        self.but = Button(self.root, text = 'PESQUISAR', command = self.Search_teacher)
        self.but.pack()


        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(fill = Y, side = RIGHT)

        self.listbox = Listbox(self.root, width = 140, height = 20)
        self.listbox.pack(pady = 5)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command = self.listbox.yview)


        self.status = Label(self.root, text = '')
        self.status.pack()

        self.root.mainloop()
    
    def Search_teacher(self):
        self.listbox.delete(0, END)
        self.name2 = self.name.get().upper()
        self.sql = 'SELECT * FROM professor'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()

        for self.row in self.cursor.execute(self.sql):
            
            if (self.name2 in self.row[1]):
                self.condition_existence = True
                self.status["text"] = ''
                self.show = '-> NOME: {}    CPF: {}    DEPARTAMENTO: {}'.format(self.row[1], self.row[2], self.row[3])
                self.listbox.insert(END,self.show, ' ')
                
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado !!'
            self.status["fg"] = 'red' 
        
        self.connection.close() 
          



class Teacherupdate:
    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x150+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Atualização de professor')

        self.label_cpf = Label(self.root, text = 'Digite o CPF ').pack()
        self.cpf2 = Entry(self.root)
        self.cpf2.focus_force()
        self.cpf2.pack()


        self.but = Button(self.root, text = 'PROCURAR', command = self.Update_teacher)
        self.but.pack()


        self.status = Label(self.root, text = '', fg = 'red')
        self.status.pack()

        self.root.mainloop()
    
    def Update_teacher(self):
        self.cpf = self.cpf2.get()
        self.sql = 'SELECT * FROM professor'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[2] == self.cpf):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!'
        

        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.geometry('430x300+300+150')
            self.root2.resizable(False,False)
            self.root2.protocol('WM_DELETE_WINDOW')
            self.root2.title('Dados do Professor')



            self.label1 = Label(self.root2, text = 'Dados do professor').place(x = 170, y = 10)

            self.content_name = StringVar(self.root2, self.row[1])
            self.content_cpf = StringVar(self.root2, self.row[2])
            self.content_depart = StringVar(self.root2, self.row[3])

            self.label_name = Label(self.root2, text = 'NOME: ').place(x = 0, y = 50)
            self.name = Entry(self.root2, width = 32, textvariable = self.content_name)
            self.name.place(x = 120, y = 50)


            self.label_cpf = Label(self.root2, text = 'CPF: ').place(x = 0, y = 100)
            self.cpf = Entry(self.root2, width = 32, textvariable = self.content_cpf, state = DISABLED)
            self.cpf.place(x = 120, y = 100)

            
            self.label_depart = Label(self.root2, text = 'DEPARTAMENTO: ').place(x = 0, y = 150)
            self.depart = Entry(self.root2, width = 32, textvariable = self.content_depart)
            self.depart.place(x = 120, y = 150)

            self.notname = Label(self.root2, text = '', fg = 'red')
            self.notname.place(x = 350, y = 50)

            self.notdepart = Label(self.root2, text = '', fg = 'red')
            self.notdepart.place(x = 350, y = 150)

            self.status2 = Label(self.root2, text = '', fg = 'green')
            self.status2.place(x = 165, y = 250)
            

            self.but2 = Button(self.root2, text = 'ATUALIZAR', command = self.Final_upteacher)
            self.but2.place(x = 190, y = 200)
            self.root2.mainloop()



    
    def Final_upteacher(self):
        self.new_name = self.name.get().upper()
        self.new_depart = self.depart.get().upper()

        if (self.new_name != '' and self.new_depart != ''):
            self.cursor.execute('''UPDATE professor set name = ?, cpf = ?, departament = ? WHERE cpf = ?''', 
                                (self.new_name, self.row[2], self.new_depart, self.row[2]))
            self.connection.commit()
            self.connection.close()
            self.notname["text"] = ''
            self.notdepart["text"] = ''
            self.status2["text"] = 'Cadastro Atualizado!'
            self.but2['text'] = 'Sair'
            self.but2['width'] = '10'
            self.but2['command'] = self.Exit
        
        else:
            if(self.new_name == ''):
                self.notname["text"] = 'Inválido'
            else:
                self.notname['text'] = ''

            if(self.new_depart == ''):
                self.notdepart["text"] = 'Inválido'
            else:
                self.notdepart["text"] = ''

    def Exit(self):
        self.root2.destroy()



class Teacherdelete:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x130+500+180')
        self.root.title('Deletar professor')

        self.labe_cpf = Label(self.root, text = 'Digite o CPF').place(x = 120, y = 0)
        self.cpf = Entry(self.root, width = 27)
        self.cpf.place(x = 60, y = 30)
        self.cpf.focus_force()

        self.status = Label(self.root, text = '', fg = 'red')
        self.status.place(x = 70, y = 60)

        self.but = Button(self.root, text = 'PROCURAR', command = self.Delete_teacher).place(x = 114, y = 80)

        self.root.mainloop()
    
    def Delete_teacher(self):
        self.cpf2 = self.cpf.get()
        self.sql = 'SELECT * FROM professor'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[2] == self.cpf2):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!!'
        
        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.resizable(False,False)
            self.root2.geometry('360x280+500+180')
            self.root2.title('Deletar?')


            self.content_name = StringVar(self.root2, self.row[1])
            self.content_cpf = StringVar(self.root2, self.row[2])
            self.content_depart = StringVar(self.root2, self.row[3])


            self.title = Label(self.root2, text = 'Dados').place(x = 140, y = 0)

            self.label_name = Label(self.root2, text = 'NOME: ').place(x = 0, y = 50)
            self.entry_name = Entry(self.root2, width = 27, textvariable = self.content_name, state = DISABLED)
            self.entry_name.place(x = 120, y = 50)

            self.label_cpf = Label(self.root2, text = 'CPF: ').place(x = 0, y = 100)
            self.entry_cpf = Entry(self.root2, width = 27, textvariable = self.content_cpf, state = DISABLED)
            self.entry_cpf.place(x = 120, y = 100)

            self.label_depart = Label(self.root2, text = 'DEPARTAMENTO: ').place(x = 0, y = 150)
            self.entry_depart = Entry(self.root2, width = 27, textvariable = self.content_depart, state = DISABLED)
            self.entry_depart.place(x = 120, y = 150)

            self.but_ok = Button(self.root2, text = 'DELETAR', command = self.Ok_delete).place(x = 80, y = 200)
            self.but_cancel = Button(self.root2, text = 'CANCELAR', command = self.Cancel_delete)
            self.but_cancel.place(x = 220, y = 200)
            self.but_cancel.focus_force()
            

            self.root2.mainloop()

    def Cancel_delete(self):
        self.root2.destroy()

    def Ok_delete(self):
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.geometry('340x150+510+270')
        self.root3.title('Autenticação')


        self.label_title2 = Label(self.root3, text = 'Digite a senha de acesso para autenticação').place(x = 40, y = 0)

        self.entry_password = Entry(self.root3, width = 25, show = '*')
        self.entry_password.place(x = 90, y = 30)
        self.entry_password.focus_force()
        self.status = Label(self.root3, text = '', fg = 'red')
        self.status.place(x = 130, y = 60)

        self.butok_aut = Button(self.root3, text = 'AUTENTICAR', command = self.Ok_aut).place(x = 40, y = 100)
        self.butcancel_aut = Button(self.root3, text = 'CANCELAR', command = self.Cancel_aut).place(x = 230, y = 100)



        self.root3.mainloop()


    def Cancel_aut(self):
        self.root3.destroy()
        self.root2.destroy()
    
    def Ok_aut(self):
        self.password = self.entry_password.get()

        if (self.password != 'root'):
            self.status["text"] = 'Senha inválida!'

        else:
            self.id = str(self.row[0])
            self.cursor.execute('''DELETE FROM professor WHERE id = ?''', (self.id,))
            self.connection.commit()
            self.connection.close()

            self.root4 = Toplevel()
            self.root4.resizable(False,False)
            self.root4.geometry('240x100+550+290')
            self.root4.title('SUCESSO')

            self.completed = Label(self.root4, text = 'Cadastro deletado! (Aperte OK para sair)').place(x = 0, y = 0)
            self.but_exit = Button(self.root4, text = 'OK', width = 20, command = self.Exit).place(x = 50, y = 50)
            self.root4.mainloop()

    def Exit(self):
        self.root4.destroy()
        self.root3.destroy()
        self.root2.destroy()



#------------------------------------------------------------------------------------------------------------





#--------------------------------TODAS-AS-FUNÇÕES-DA-ABA-DE-ALUNOS-------------------------------------------

class Studentinsert:
    
    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('430x200+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Cadastramento de Aluno')

        self.label_nome = Label(self.root, text = 'Nome (completo): ').place(x = 10, y = 20)
        self.name = Entry(self.root)
        self.name.focus_force()
        self.name.place(x = 170, y = 20)

        self.label_cpf = Label(self.root, text = 'CPF: ').place(x = 10, y = 60)
        self.cpf = Entry(self.root)
        self.cpf.place(x = 170, y = 60)

        self.but = Button(self.root, text = 'CADASTRAR', command = self.Insert_student)
        self.but.place(x = 175, y = 120)

        self.status = Label(self.root, text = '')
        self.status.place(x = 155, y = 170)

        self.notname = Label(self.root, text = '', fg = 'red')
        self.notname.place(x = 300, y = 20)

        self.notcpf = Label(self.root, text = '', fg = 'red')
        self.notcpf.place(x = 300, y = 60)


        self.root.mainloop()
    
    def Insert_student(self):
        self.name2 = self.name.get()
        self.cpf2 = self.cpf.get()


        if (self.name2 != '' and self.cpf2 != ''):
            self.insert = Aluno()
            self.insert.Create_aluno(self.name2, self.cpf2)

            if (self.insert.condition_add == True):
                self.notname["text"] = ''
                self.notcpf["text"] = ''
                self.status["fg"] = 'green'
                self.status["text"] = 'Cadastro feito !!'
                self.but['text'] = 'Sair'
                self.but['width'] = '10'
                self.but['command'] = self.Exit
                
        
            else:
                self.status["fg"] = 'red'
                self.status["text"] = 'Cadastro já existente!!'

        else:
            if(self.name2 == ''):
                self.notname["text"] = 'Item em branco!'
            
            else:
                self.notname["text"] = ''

            if(self.cpf2 == ''):
                self.notcpf["text"] = 'Item em branco!'
            
            else:
                self.notcpf["text"] = ''
    
    def Exit(self):
        self.root.destroy()
            



class Studentsearch:

    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('800x500+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Pesquisador de professor')

        self.label_nome = Label(self.root, text = 'Nome completo (Deixe em branco para ver todos): ').pack()
        self.name = Entry(self.root)
        self.name.focus_force()
        self.name.pack()


        self.but = Button(self.root, text = 'PESQUISAR', command = self.Search_student)
        self.but.pack()

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(fill = Y, side = RIGHT)

        self.listbox = Listbox(self.root, width = 140, height = 20)
        self.listbox.pack(pady = 5)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command = self.listbox.yview)


        self.status = Label(self.root, text = '')
        self.status.pack()

        self.root.mainloop()
    
    def Search_student(self):
        self.listbox.delete(0, END)
        self.name2 = self.name.get().upper()
        self.sql = 'SELECT * FROM aluno'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()

        for self.row in self.cursor.execute(self.sql):
            
            if (self.name2 in self.row[1]):
                self.condition_existence = True
                self.status["text"] = ''
                self.show = '-> NOME:  {}    CPF:  {}  '.format(self.row[1], self.row[2])
                self.listbox.insert(END,self.show, ' ')
                
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado !!'
            self.status["fg"] = 'red' 
        
        self.connection.close() 
    



class Studentupdate:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x150+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Atualização de aluno')

        self.label_cpf = Label(self.root, text = 'Digite o CPF ').pack()
        self.cpf2 = Entry(self.root)
        self.cpf2.focus_force()
        self.cpf2.pack()


        self.but = Button(self.root, text = 'PROCURAR', command = self.Update_teacher)
        self.but.pack()


        self.status = Label(self.root, text = '', fg = 'red')
        self.status.pack()

        self.root.mainloop()
    
    def Update_teacher(self):
        self.cpf = self.cpf2.get()
        self.sql = 'SELECT * FROM aluno'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[2] == self.cpf):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!'
        

        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.geometry('430x270+300+150')
            self.root2.resizable(False,False)
            self.root2.protocol('WM_DELETE_WINDOW')
            self.root2.title('Dados do aluno')



            self.label1 = Label(self.root2, text = 'Dados do aluno').place(x = 170, y = 10)

            self.content_name = StringVar(self.root2, self.row[1])
            self.content_cpf = StringVar(self.root2, self.row[2])

            self.label_name = Label(self.root2, text = 'NOME: ').place(x = 0, y = 50)
            self.name = Entry(self.root2, width = 32, textvariable = self.content_name)
            self.name.place(x = 120, y = 50)


            self.label_cpf = Label(self.root2, text = 'CPF: ').place(x = 0, y = 100)
            self.cpf = Entry(self.root2, width = 32, textvariable = self.content_cpf, state = DISABLED)
            self.cpf.place(x = 120, y = 100)

            

            self.notname = Label(self.root2, text = '', fg = 'red')
            self.notname.place(x = 340, y = 50)


            self.status2 = Label(self.root2, text = '', fg = 'green')
            self.status2.place(x = 165, y = 230)
            

            self.but2 = Button(self.root2, text = 'ATUALIZAR', command = self.Final_upteacher)
            self.but2.place(x = 190, y = 180)
            self.root2.mainloop()



    
    def Final_upteacher(self):
        self.new_name = self.name.get().upper()

        if (self.new_name != ''):
            self.cursor.execute('''UPDATE aluno set name = ?, cpf = ? WHERE cpf = ?''', 
                                (self.new_name, self.row[2], self.row[2]))
            self.connection.commit()
            self.connection.close()
            self.notname["text"] = ''
            self.status2["text"] = 'Cadastro Atualizado!'
            self.but2['text'] = 'Sair'
            self.but2['width'] = '10'
            self.but2['command'] = self.Exit
        
        else:
            self.notname["text"] = 'Inválido'
    
    def Exit(self):
        self.root2.destroy()




class Studentdelete:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x130+500+180')
        self.root.title('Deletar aluno')

        self.labe_cpf = Label(self.root, text = 'Digite o CPF').place(x = 120, y = 0)
        self.cpf = Entry(self.root, width = 27)
        self.cpf.place(x = 60, y = 30)
        self.cpf.focus_force()

        self.status = Label(self.root, text = '', fg = 'red')
        self.status.place(x = 70, y = 60)

        self.but = Button(self.root, text = 'PROCURAR', command = self.Delete_student).place(x = 114, y = 80)

        self.root.mainloop()
    
    def Delete_student(self):
        self.cpf2 = self.cpf.get()
        self.sql = 'SELECT * FROM aluno'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[2] == self.cpf2):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!!'
        
        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.resizable(False,False)
            self.root2.geometry('360x280+500+180')
            self.root2.title('Deletar?')


            self.content_name = StringVar(self.root2, self.row[1])
            self.content_cpf = StringVar(self.root2, self.row[2])


            self.title = Label(self.root2, text = 'Dados').place(x = 140, y = 0)

            self.label_name = Label(self.root2, text = 'NOME: ').place(x = 0, y = 50)
            self.entry_name = Entry(self.root2, width = 27, textvariable = self.content_name, state = DISABLED)
            self.entry_name.place(x = 120, y = 50)

            self.label_cpf = Label(self.root2, text = 'CPF: ').place(x = 0, y = 100)
            self.entry_cpf = Entry(self.root2, width = 27, textvariable = self.content_cpf, state = DISABLED)
            self.entry_cpf.place(x = 120, y = 100)


            self.but_ok = Button(self.root2, text = 'DELETAR', command = self.Ok_delete).place(x = 80, y = 200)
            self.but_cancel = Button(self.root2, text = 'CANCELAR', command = self.Cancel_delete)
            self.but_cancel.place(x = 220, y = 200)
            self.but_cancel.focus_force()
            

            self.root2.mainloop()

    def Cancel_delete(self):
        self.root2.destroy()

    def Ok_delete(self):
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.geometry('340x150+510+270')
        self.root3.title('Autenticação')


        self.label_title2 = Label(self.root3, text = 'Digite a senha de acesso para autenticação').place(x = 40, y = 0)

        self.entry_password = Entry(self.root3, width = 25, show = '*')
        self.entry_password.place(x = 90, y = 30)
        self.entry_password.focus_force()
        self.status = Label(self.root3, text = '', fg = 'red')
        self.status.place(x = 130, y = 60)

        self.butok_aut = Button(self.root3, text = 'AUTENTICAR', command = self.Ok_aut).place(x = 40, y = 100)
        self.butcancel_aut = Button(self.root3, text = 'CANCELAR', command = self.Cancel_aut).place(x = 230, y = 100)



        self.root3.mainloop()


    def Cancel_aut(self):
        self.root3.destroy()
        self.root2.destroy()
    
    def Ok_aut(self):
        self.password = self.entry_password.get()

        if (self.password != 'root'):
            self.status["text"] = 'Senha inválida!'

        else:
            self.id = str(self.row[0])
            self.cursor.execute('''DELETE FROM aluno WHERE id = ?''', (self.id,))
            self.connection.commit()
            self.connection.close()

            self.root4 = Toplevel()
            self.root4.resizable(False,False)
            self.root4.geometry('240x100+550+290')
            self.root4.title('SUCESSO')

            self.completed = Label(self.root4, text = 'Cadastro deletado! (Aperte OK para sair)').place(x = 0, y = 0)
            self.but_exit = Button(self.root4, text = 'OK', width = 20, command = self.Exit).place(x = 50, y = 50)
            self.root4.mainloop()

    def Exit(self):
        self.root4.destroy()
        self.root3.destroy()
        self.root2.destroy()


#------------------------------------------------------------------------------------------------------------




#--------------------------------TODAS-AS-FUNÇÕES-DA-ABA-DE-DISCIPLINAS--------------------------------------

class Disciplineinsert:


    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('430x200+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Cadastramento de disciplina')

        self.label_cod = Label(self.root, text = 'Código: ').place(x = 10, y = 20)
        self.cod = Entry(self.root)
        self.cod.focus_force()
        self.cod.place(x = 170, y = 20)

        self.label_name = Label(self.root, text = 'Nome: ').place(x = 10, y = 60)
        self.name = Entry(self.root)
        self.name.place(x = 170, y = 60)

        self.but = Button(self.root, text = 'CADASTRAR', command = self.Insert_student)
        self.but.place(x = 175, y = 120)

        self.status = Label(self.root, text = '')
        self.status.place(x = 155, y = 170)

        self.notcod = Label(self.root, text = '', fg = 'red')
        self.notcod.place(x = 300, y = 20)

        self.notname = Label(self.root, text = '', fg = 'red')
        self.notname.place(x = 300, y = 60)


        self.root.mainloop()
    
    def Insert_student(self):
        self.cod2 = self.cod.get()
        self.name2 = self.name.get()


        if (self.cod2 != '' and self.name2 != ''):
            self.insert = Disciplina()
            self.insert.Create_disciplina(self.name2, self.cod2)

            if (self.insert.condition_add == True):
                self.notcod["text"] = ''
                self.notname["text"] = ''
                self.status["fg"] = 'green'
                self.status["text"] = 'Cadastro feito !!'
                self.but['text'] = 'Sair'
                self.but['width'] = '10'
                self.but['command'] = self.Exit
                
        
            else:
                self.status["fg"] = 'red'
                self.status["text"] = 'Cadastro já existente!!'

        else:
            if(self.name2 == ''):
                self.notname["text"] = 'Item em branco!'
            
            else:
                self.notname["text"] = ''

            if(self.cod2 == ''):
                self.notcod["text"] = 'Item em branco!'
            
            else:
                self.notcod["text"] = ''
    
    def Exit(self):
        self.root.destroy()




class Disciplinesearch:

    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('800x500+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Pesquisador de disciplina')

        self.label_nome = Label(self.root, text = 'Nome da disciplina (Deixe em branco para ver todos): ').pack()
        self.name = Entry(self.root)
        self.name.focus_force()
        self.name.pack()


        self.but = Button(self.root, text = 'PESQUISAR', command = self.Search_discipline)
        self.but.pack()

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(fill = Y, side = RIGHT)

        self.listbox = Listbox(self.root, width = 140, height = 20)
        self.listbox.pack(pady = 5)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command = self.listbox.yview)


        self.status = Label(self.root, text = '')
        self.status.pack()

        self.root.mainloop()
    
    def Search_discipline(self):
        self.listbox.delete(0, END)
        self.name2 = self.name.get().upper()
        self.sql = 'SELECT * FROM disciplina'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()

        for self.row in self.cursor.execute(self.sql):
            
            if (self.name2 in self.row[1]):
                self.condition_existence = True
                self.status["text"] = ''
                self.show = '-> NOME DA DISCIPLINA:  {}    CÓDIGO:  {}  '.format(self.row[1], self.row[2])
                self.listbox.insert(END,self.show, ' ')
                
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado !!'
            self.status["fg"] = 'red' 
        
        self.connection.close() 



class Disciplineupdate:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x150+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Atualização de disciplina')

        self.label_cod = Label(self.root, text = 'Digite o Código ').pack()
        self.cod2 = Entry(self.root)
        self.cod2.focus_force()
        self.cod2.pack()


        self.but = Button(self.root, text = 'PROCURAR', command = self.Update_discipline)
        self.but.pack()


        self.status = Label(self.root, text = '', fg = 'red')
        self.status.pack()

        self.root.mainloop()
    
    def Update_discipline(self):
        self.cod = self.cod2.get()
        self.sql = 'SELECT * FROM disciplina'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[2] == self.cod):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!'
        

        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.geometry('430x270+300+150')
            self.root2.resizable(False,False)
            self.root2.protocol('WM_DELETE_WINDOW')
            self.root2.title('Dados da disciplina')



            self.label1 = Label(self.root2, text = 'Dados da disciplina').place(x = 170, y = 10)

            self.content_name = StringVar(self.root2, self.row[1])
            self.content_cod = StringVar(self.root2, self.row[2])

            self.label_name = Label(self.root2, text = 'NOME: ').place(x = 0, y = 50)
            self.name = Entry(self.root2, width = 32, textvariable = self.content_name)
            self.name.place(x = 120, y = 50)


            self.label_cod = Label(self.root2, text = 'CÓDIGO: ').place(x = 0, y = 100)
            self.cod = Entry(self.root2, width = 32, textvariable = self.content_cod, state = DISABLED)
            self.cod.place(x = 120, y = 100)

            

            self.notname = Label(self.root2, text = '', fg = 'red')
            self.notname.place(x = 340, y = 50)


            self.status2 = Label(self.root2, text = '', fg = 'green')
            self.status2.place(x = 165, y = 230)
            

            self.but2 = Button(self.root2, text = 'ATUALIZAR', command = self.Final_upteacher)
            self.but2.place(x = 190, y = 180)
            self.root2.mainloop()



    
    def Final_upteacher(self):
        self.new_name = self.name.get().upper()

        if (self.new_name != ''):
            self.cursor.execute('''UPDATE disciplina set name = ?, cod_disciplina = ? WHERE cod_disciplina = ?''', 
                                (self.new_name, self.row[2], self.row[2]))
            self.connection.commit()
            self.connection.close()
            self.notname["text"] = ''
            self.status2["text"] = 'Cadastro Atualizado!'
            self.but2['text'] = 'Sair'
            self.but2['width'] = '10'
            self.but2['command'] = self.Exit
        
        else:
            self.notname["text"] = 'Inválido'
    
    def Exit(self):
        self.root2.destroy()



class Disciplinedelete:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x130+500+180')
        self.root.title('Deletar disciplina')

        self.labe_cod = Label(self.root, text = 'Digite o Código').place(x = 100, y = 0)
        self.cod = Entry(self.root, width = 27)
        self.cod.place(x = 60, y = 30)
        self.cod.focus_force()

        self.status = Label(self.root, text = '', fg = 'red')
        self.status.place(x = 70, y = 60)

        self.but = Button(self.root, text = 'PROCURAR', command = self.Delete_discipline).place(x = 114, y = 80)

        self.root.mainloop()
    
    def Delete_discipline(self):
        self.cod2 = self.cod.get()
        self.sql = 'SELECT * FROM disciplina'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[2] == self.cod2):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!!'
        
        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.resizable(False,False)
            self.root2.geometry('360x280+500+180')
            self.root2.title('Deletar?')


            self.content_name = StringVar(self.root2, self.row[1])
            self.content_cod = StringVar(self.root2, self.row[2])


            self.title = Label(self.root2, text = 'Dados').place(x = 140, y = 0)

            self.label_nama = Label(self.root2, text = 'NOME: ').place(x = 0, y = 50)
            self.entry_name = Entry(self.root2, width = 27, textvariable = self.content_name, state = DISABLED)
            self.entry_name.place(x = 120, y = 50)

            self.label_cod = Label(self.root2, text = 'CÓDIGO: ').place(x = 0, y = 100)
            self.entry_cod = Entry(self.root2, width = 27, textvariable = self.content_cod, state = DISABLED)
            self.entry_cod.place(x = 120, y = 100)


            self.but_ok = Button(self.root2, text = 'DELETAR', command = self.Ok_delete).place(x = 80, y = 200)
            self.but_cancel = Button(self.root2, text = 'CANCELAR', command = self.Cancel_delete)
            self.but_cancel.place(x = 220, y = 200)
            self.but_cancel.focus_force()
            

            self.root2.mainloop()

    def Cancel_delete(self):
        self.root2.destroy()

    def Ok_delete(self):
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.geometry('340x150+510+270')
        self.root3.title('Autenticação')


        self.label_title2 = Label(self.root3, text = 'Digite a senha de acesso para autenticação').place(x = 40, y = 0)

        self.entry_password = Entry(self.root3, width = 25, show = '*')
        self.entry_password.place(x = 90, y = 30)
        self.entry_password.focus_force()
        self.status = Label(self.root3, text = '', fg = 'red')
        self.status.place(x = 130, y = 60)

        self.butok_aut = Button(self.root3, text = 'AUTENTICAR', command = self.Ok_aut).place(x = 40, y = 100)
        self.butcancel_aut = Button(self.root3, text = 'CANCELAR', command = self.Cancel_aut).place(x = 230, y = 100)



        self.root3.mainloop()


    def Cancel_aut(self):
        self.root3.destroy()
        self.root2.destroy()
    
    def Ok_aut(self):
        self.password = self.entry_password.get()

        if (self.password != 'root'):
            self.status["text"] = 'Senha inválida!'

        else:
            self.id = str(self.row[0])
            self.cursor.execute('''DELETE FROM disciplina WHERE id = ?''', (self.id,))
            self.connection.commit()
            self.connection.close()

            self.root4 = Toplevel()
            self.root4.resizable(False,False)
            self.root4.geometry('240x100+550+290')
            self.root4.title('SUCESSO')

            self.completed = Label(self.root4, text = 'Cadastro deletado! (Aperte OK para sair)').place(x = 0, y = 0)
            self.but_exit = Button(self.root4, text = 'OK', width = 20, command = self.Exit).place(x = 50, y = 50)
            self.root4.mainloop()

    def Exit(self):
        self.root4.destroy()
        self.root3.destroy()
        self.root2.destroy()


#------------------------------------------------------------------------------------------------------------



#---------------------------------------TODOAS-AS-FUNÇÕES-DA-ABA-DE-TURMAs-----------------------------------

class Classinsert:
    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('430x250+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Cadastramento de turma')

        self.label_codt = Label(self.root, text = 'Código da turma: ').place(x = 10, y = 20)
        self.codt = Entry(self.root)
        self.codt.focus_force()
        self.codt.place(x = 170, y = 20)

        self.label_per = Label(self.root, text = 'Período: ').place(x = 10, y = 60)
        self.per = Entry(self.root)
        self.per.place(x = 170, y= 60)

        self.label_codd = Label(self.root, text = 'Código da disciplina: ').place(x = 10, y = 100)
        self.codd = Entry(self.root)
        self.codd.place(x = 170, y= 100)

        self.but = Button(self.root, text = 'Continuar', command = self.Next_insert)
        self.but.place(x = 175, y = 170)

        self.status = Label(self.root, text = '')
        self.status.place(x = 155, y = 210)

        self.notcodt = Label(self.root, text = '', fg = 'red')
        self.notcodt.place(x = 300, y = 20)

        self.notper = Label(self.root, text = '', fg = 'red')
        self.notper.place(x = 300, y = 60)

        self.notcodd = Label(self.root, text = '', fg = 'red')
        self.notcodd.place(x = 300, y = 100)

        self.root.mainloop()
    
    def Next_insert(self):

        self.codt2 = self.codt.get().upper()
        self.per2 = self.per.get()
        self.codd2 = self.codd.get()


        if (self.codt2 != '' and self.per2 != '' and self.codd2 != ''):
            self.sql = 'SELECT * FROM turma'
            self.condition_add = True
            self.connection = sqlite3.connect('CRUD.db')
            self.cursor = self.connection.cursor()
            self.notcodt['text'] = ''
            self.notper["text"] = ''
            self.notcodd["text"] = ''


            for self.row in self.cursor.execute(self.sql):
    
                if (self.row[1] == self.codt2):
                    self.condition_add = False
                    break


            if (self.condition_add == False):
                self.status['fg'] = 'red'
                self.status["text"] = 'Cadastro já existente!!'

            else:
                self.cursor.execute('''INSERT INTO turma (cod_turma, periodo, cod_disciplina) VALUES (?, ?, ?)''',
                                    (self.codt2, self.per2, self.codd2))
                self.connection.commit()
                self.root.destroy()

                self.root2 = Tk()

                self.root2.resizable(False,False)
                self.root2.geometry('350x150+300+150')
                self.root2.protocol('WM_DELETE_WINDOW')
                self.root2.title('Adicionar professor a turma')


                self.cpf_add = ''



                self.label1 = Label(self.root2, text = 'Digite o CPF do professor, e clique no + para adicionar.').place(x = 30, y = 0)
                
                self.cpf_prof = Entry(self.root2, width = 30)
                self.cpf_prof.place(x = 90, y = 40)
                
                self.but_add = Button(self.root2, text = '+', command = self.cpfprof).place(x = 290, y = 35)
                
                self.status = Label(self.root2, text = '', fg = 'red')
                self.status.place(x = 140, y = 60)

                self.but_next = Button(self.root2, text = 'Continuar', command = self.Next2_insert).place(x = 140, y = 80)

                self.root2.mainloop()


        else:
            if(self.codt2 == ''):
                self.notcodt["text"] = 'Item em branco!'
            
            else:
                self.notcodt["text"] = ''

            if(self.per2 == ''):
                self.notper["text"] = 'Item em branco!'
            
            else:
                self.notper["text"] = ''
            
            if (self.codd2 == ''):
                self.notcodd["text"] = 'Item em branco!'
            
            else:
                self.notcodd["text"] = ''


    def cpfprof(self):
        if(self.cpf_prof.get() != ''):
            if (self.cpf_prof.get() in self.cpf_add):
                self.status['text'] = 'Professor já adicionado!'
            
            else:
                self.status['text'] = ''
                self.cpf_add += self.cpf_prof.get() + '//'

        else:
            self.status['text'] = 'Inválido'
    
    def Next2_insert(self):
        self.cursor.execute('''UPDATE turma set cpf_professor = ? WHERE cod_turma = ?''',
                            (self.cpf_add, self.codt2))
        self.connection.commit()
        self.root2.destroy()

        self.root3 = Tk()

        self.root3.resizable(False,False)
        self.root3.geometry('350x150+300+150')
        self.root3.protocol('WM_DELETE_WINDOW')
        self.root3.title('Adicionar aluno a turma')


        self.cpf_add = ''


        self.label1 = Label(self.root3, text = 'Digite o CPF do aluno, e clique no + para adicionar.').place(x = 30, y = 0)
                
        self.cpf_aluno = Entry(self.root3, width = 30)
        self.cpf_aluno.place(x = 90, y = 40)
                
        self.but_add = Button(self.root3, text = '+', command = self.cpfaluno).place(x = 290, y = 35)
                
        self.status = Label(self.root3, text = '', fg = 'red')
        self.status.place(x = 140, y = 60)

        self.but_next = Button(self.root3, text = 'FINALIZAR', command = self.Finish_insert).place(x = 140, y = 80)

        self.root3.mainloop()
    


    def cpfaluno(self):
        if(self.cpf_aluno.get() != ''):
            if(self.cpf_aluno.get() in self.cpf_add):
                self.status['text'] = 'Aluno já adicionado!'

            else:    
                self.status['text'] = ''
                self.cpf_add += self.cpf_aluno.get() + '//'

        else:
            self.status['text'] = 'Inválido'




    def Finish_insert(self):

        self.cursor.execute('''UPDATE turma set cpf_aluno = ? WHERE cod_turma = ?''',
                            (self.cpf_add, self.codt2))
        
        self.connection.commit()
        self.connection.close()
        
        self.status.place(x = 100, y = 100)
        self.status['fg'] = 'green'
        self.status['text'] = 'Turma criada com sucesso!!'





class Classsearch:

    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('800x500+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Pesquisador de turma')

        self.label_nome = Label(self.root, text = 'Digite o código da turma: ').pack()
        self.cod = Entry(self.root)
        self.cod.focus_force()
        self.cod.pack()


        self.but = Button(self.root, text = 'PESQUISAR', command = self.Search_discipline)
        self.but.pack()

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(fill = Y, side = RIGHT)

        self.listbox = Listbox(self.root, width = 140, height = 20)
        self.listbox.pack(pady = 5)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command = self.listbox.yview)


        self.status = Label(self.root, text = '')
        self.status.pack()

        self.root.mainloop()
    
    def Search_discipline(self):
        self.listbox.delete(0, END)
        self.cod2 = self.cod.get().upper()
        self.sql = 'SELECT * FROM turma'
        self.sql2 = 'SELECT * FROM professor'
        self.sql3 = 'SELECT * FROM aluno'
        self.sql4 = 'SELECT * FROM disciplina'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()

        for self.row in self.cursor.execute(self.sql):
            
            if (self.cod2 == self.row[1]):
                self.condition_existence = True
                self.status["text"] = ''

                self.show = '-> Código da turma:  {}    Período:  {}    Código da disciplina: {}'.format(self.row[1], self.row[2], self.row[3])
                
                
                
                for self.row4 in self.cursor.execute(self.sql4):
                    if (self.row[3] == self.row4[2]):
                        self.show4 = '-> Nome da disciplina: {}'.format(self.row4[1])


                self.listbox.insert(END,self.show, ' ', self.show4, ' ', '-> PROFESSOR(ES):', '')


                self.rowprof = self.row[4].split('//')
                self.rowaluno = self.row[5].split('//')


                for i in range(len(self.rowprof) - 1):
                    if (self.rowprof[i] == ''):
                        del(self.rowprof[i])
                    
                    else:
                        for self.row2 in self.cursor.execute(self.sql2):
                            if (self.rowprof[i] == self.row2[2]):
                                self.show2 = '-> NOME: {}   CPF: {}'.format(self.row2[1], self.row2[2])
                                self.listbox.insert(END, self.show2)
                
                self.listbox.insert(END, '', '-> ALUNOS:', '')
                for j in range(len(self.rowaluno) - 1):
                    if(self.rowaluno[j] == ''):
                        del(self.rowaluno[i])
                    
                    else:
                        for self.row3 in self.cursor.execute(self.sql3):
                            if (self.rowaluno[j] == self.row3[2]):
                                self.show3 = '-> NOME: {}   CPF: {}'.format(self.row3[1], self.row3[2])
                                self.listbox.insert(END, self.show3)
                    
                

        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado !!'
            self.status["fg"] = 'red' 
        
        self.connection.close() 




class Classupdate:


    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x150+300+150')
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.title('Atualização de turma')

        self.label_cod = Label(self.root, text = 'Digite o Código ').pack()
        self.cod2 = Entry(self.root)
        self.cod2.focus_force()
        self.cod2.pack()


        self.but = Button(self.root, text = 'PROCURAR', command = self.Update_class)
        self.but.pack()


        self.status = Label(self.root, text = '', fg = 'red')
        self.status.pack()

        self.root.mainloop()
    
    def Update_class(self):
        self.cod = self.cod2.get().upper()
        self.sql = 'SELECT * FROM turma'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[1] == self.cod):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!'
        

        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.geometry('430x300+300+150')
            self.root2.resizable(False,False)
            self.root2.protocol('WM_DELETE_WINDOW')
            self.root2.title('Dados da turma')



            self.label1 = Label(self.root2, text = 'Dados da turma').place(x = 170, y = 10)

            self.content_codt = StringVar(self.root2, self.row[1])
            self.content_per = StringVar(self.root2, self.row[2])
            self.content_codd = StringVar(self.root2, self.row[3])

            self.label_codt = Label(self.root2, text = 'Código da turma: ').place(x = 0, y = 50)
            self.codt = Entry(self.root2, width = 32, textvariable = self.content_codt)
            self.codt.place(x = 120, y = 50)


            self.label_per = Label(self.root2, text = 'Período: ').place(x = 0, y = 100)
            self.per = Entry(self.root2, width = 32, textvariable = self.content_per)
            self.per.place(x = 120, y = 100)

            
            self.label_codd = Label(self.root2, text = 'Código da disciplina: ').place(x = 0, y = 150)
            self.codd = Entry(self.root2, width = 32, textvariable = self.content_codd)
            self.codd.place(x = 120, y = 150)

            self.notcodt = Label(self.root2, text = '', fg = 'red')
            self.notcodt.place(x = 350, y = 50)

            self.notper = Label(self.root2, text = '', fg = 'red')
            self.notper.place(x = 350, y = 100)

            self.notcodd = Label(self.root2, text = '', fg = 'red')
            self.notcodd.place(x = 350, y = 150)


            self.status2 = Label(self.root2, text = '', fg = 'green')
            self.status2.place(x = 165, y = 250)
            

            self.but2 = Button(self.root2, text = 'ATUALIZAR', command = self.Final_upclass)
            self.but2.place(x = 190, y = 200)


            self.delprof = Button(self.root2, text = 'DELETAR PROFESSOR', command = self.Deleteprof)
            self.delprof.place(x = 0, y = 230)

            self.addprof = Button(self.root2, text = 'ADICIONAR PROFESSOR', command = self.Addprof)
            self.addprof.place(x = 0, y = 260)

            self.delaluno = Button(self.root2, text = 'DELETAR ALUNO', command = self.Deletealuno)
            self.delaluno.place(x = 290, y = 230)

            self.addaluno = Button(self.root2 , text = 'ADICIONAR ALUNO', command = self.Addaluno)
            self.addaluno.place(x = 290, y = 260)


            self.root2.mainloop()



    
    def Final_upclass(self):
        self.new_codt = self.codt.get().upper()
        self.new_per = self.per.get().upper()
        self.new_codd = self.codd.get().upper()

        if (self.new_codt != '' and self.new_per != '' and self.new_codd != ''):
            self.cursor.execute('''UPDATE turma set cod_turma = ?, periodo = ?, cod_disciplina = ? WHERE cod_turma = ?''', 
                                (self.new_codt, self.new_per, self.new_codd, self.row[1]))
            self.connection.commit()
            self.connection.close()
            self.notcodt["text"] = ''
            self.notper["text"] = ''
            self.notcodd['text'] = ''
            self.status2["text"] = 'Cadastro Atualizado!'
            self.but2['text'] = 'Sair'
            self.but2['width'] = '10'
            self.but2['command'] = self.Exit
        
        else:
            if(self.new_codt == ''):
                self.notcodt["text"] = 'Inválido'
            else:
                self.notcodt['text'] = ''

            if(self.new_per == ''):
                self.notper["text"] = 'Inválido'
            
            else:
                self.notper["text"] = ''
            
            if(self.new_codd == ''):
                self.notcodd['text'] = 'Inválido'
            
            else:
                self.notcodd['text'] == ''
    
    def Deleteprof(self):
        self.rowprof = self.row[4].split('//')
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.protocol('WM_DELETE_WINDOW')
        self.root3.geometry('250x100') 
        self.root3.title('DELETAR PROFESSOR')

        self.label = Label(self.root3, text = 'Digite o CPF').pack()

        self.cpf = Entry(self.root3)
        self.cpf.focus_force()
        self.cpf.pack()

        self.but = Button(self.root3, text = 'DELETAR', command = self.Delprof).pack()
        self.status = Label(self.root3, text = '')
        self.status.pack()

        self.root3.mainloop()
    
    def Delprof(self):
        self.cpf_del = self.cpf.get()

        for i in range(len(self.rowprof)):
            if (self.cpf_del == self.rowprof[i]):
                del(self.rowprof[i])
        
        self.rowprof = '//'.join(self.rowprof)

        self.cursor.execute('''UPDATE turma set cpf_professor = ? WHERE cod_turma = ?''',
                            (self.rowprof, self.row[1]))
        self.connection.commit()
        self.status['text'] = 'Professor deletado!'
    
    def Addprof(self):

        self.rowprof = self.row[4].split('//')
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.protocol('WM_DELETE_WINDOW')
        self.root3.geometry('250x100')
        self.root3.title('ADICIONAR PROFESSOR')
        self.label = Label(self.root3, text = 'Digite o CPF').pack()

        self.cpf = Entry(self.root3)
        self.cpf.focus_force()
        self.cpf.pack()

        self.but = Button(self.root3, text = 'ADICIONAR', command = self.Profadd).pack()
        self.status = Label(self.root3, text = '')
        self.status.pack()

        self.root3.mainloop()
    
    def Profadd(self):
    
        self.cpf_add = self.cpf.get()

        for i in range(len(self.rowprof)):
            if (self.rowprof[i] == ''):
                del(self.rowprof[i])
        
        self.rowprof.append(self.cpf_add)
        self.rowprof = '//'.join(self.rowprof)

        self.cursor.execute('''UPDATE turma set cpf_professor = ? WHERE cod_turma = ?''',
                            (self.rowprof, self.row[1]))
        self.connection.commit()
        self.status['text'] = 'Professor adicionado!'
    




    def Deletealuno(self):
        self.rowaluno = self.row[5].split('//')
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.protocol('WM_DELETE_WINDOW')
        self.root3.geometry('250x100')
        self.root3.title('DELETAR ALUNO')


        self.label = Label(self.root3, text = 'Digite o CPF').pack()

        self.cpf = Entry(self.root3)
        self.cpf.focus_force()
        self.cpf.pack()

        self.but = Button(self.root3, text = 'DELETAR', command = self.Delaluno).pack()
        self.status = Label(self.root3, text = '')
        self.status.pack()

        self.root3.mainloop()
    
    def Delaluno(self):
        self.cpf_del = self.cpf.get()

        for i in range(len(self.rowaluno)):
            if (self.cpf_del == self.rowaluno[i]):
                del(self.rowaluno[i])
        
        self.rowaluno = '//'.join(self.rowaluno)

        self.cursor.execute('''UPDATE turma set cpf_aluno = ? WHERE cod_turma = ?''',
                            (self.rowaluno, self.row[1]))
        self.connection.commit()
        self.status['text'] = 'Aluno deletado!'
    
    def Addaluno(self):

        self.rowaluno = self.row[5].split('//')
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.protocol('WM_DELETE_WINDOW')
        self.root3.geometry('250x100')
        self.root3.title('ADICIONAR ALUNO')



        self.label = Label(self.root3, text = 'Digite o CPF').pack()

        self.cpf = Entry(self.root3)
        self.cpf.focus_force()
        self.cpf.pack()

        self.but = Button(self.root3, text = 'ADICIONAR', command = self.Alunoadd).pack()
        self.status = Label(self.root3, text = '')
        self.status.pack()

        self.root3.mainloop()
    
    def Alunoadd(self):
    
        self.cpf_add = self.cpf.get()

        for i in range(len(self.rowaluno)):
            if (self.rowaluno[i] == ''):
                del(self.rowaluno[i])
        
        self.rowaluno.append(self.cpf_add)
        self.rowaluno = '//'.join(self.rowaluno)

        self.cursor.execute('''UPDATE turma set cpf_aluno = ? WHERE cod_turma = ?''',
                            (self.rowaluno, self.row[1]))
        self.connection.commit()
        self.status['text'] = 'Professor adicionado!'


    def Exit(self):
        self.connection.close()
        self.root2.destroy()




class Classdelete:

    def __init__(self, master = None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.geometry('300x130+500+180')
        self.root.title('Deletar turma')

        self.labe_cod = Label(self.root, text = 'Digite o Código da turma').place(x = 100, y = 0)
        self.cod = Entry(self.root, width = 27)
        self.cod.place(x = 60, y = 30)
        self.cod.focus_force()

        self.status = Label(self.root, text = '', fg = 'red')
        self.status.place(x = 70, y = 60)

        self.but = Button(self.root, text = 'PROCURAR', command = self.Delete_class).place(x = 114, y = 80)

        self.root.mainloop()
    
    def Delete_class(self):
        self.cod2 = self.cod.get()
        self.sql = 'SELECT * FROM turma'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()


        for self.row in self.cursor.execute(self.sql):

            if (self.row[1] == self.cod2):
                self.condition_existence = True
                break
        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado!!'
        
        else:
            self.root.destroy()

            self.root2 = Tk()
            self.root2.resizable(False,False)
            self.root2.geometry('360x280+500+180')
            self.root2.title('Deletar?')


            self.content_codt = StringVar(self.root2, self.row[1])
            self.content_codd = StringVar(self.root2, self.row[3])



            self.title = Label(self.root2, text = 'Dados').place(x = 140, y = 0)

            self.label_codt = Label(self.root2, text = 'COD. Turma: ').place(x = 0, y = 50)
            self.entry_codt = Entry(self.root2, width = 27, textvariable = self.content_codt, state = DISABLED)
            self.entry_codt.place(x = 120, y = 50)

            self.label_codd = Label(self.root2, text = 'COD. Disciplina: ').place(x = 0, y = 100)
            self.entry_codd = Entry(self.root2, width = 27, textvariable = self.content_codd, state = DISABLED)
            self.entry_codd.place(x = 120, y = 100)


            self.but_ok = Button(self.root2, text = 'DELETAR', command = self.Ok_delete).place(x = 80, y = 200)
            self.but_cancel = Button(self.root2, text = 'CANCELAR', command = self.Cancel_delete)
            self.but_cancel.place(x = 220, y = 200)
            self.but_cancel.focus_force()
            

            self.root2.mainloop()

    def Cancel_delete(self):
        self.root2.destroy()

    def Ok_delete(self):
        self.root3 = Toplevel()
        self.root3.resizable(False,False)
        self.root3.geometry('340x150+510+270')
        self.root3.title('Autenticação')


        self.label_title2 = Label(self.root3, text = 'Digite a senha de acesso para autenticação').place(x = 40, y = 0)

        self.entry_password = Entry(self.root3, width = 25, show = '*')
        self.entry_password.place(x = 90, y = 30)
        self.entry_password.focus_force()
        self.status = Label(self.root3, text = '', fg = 'red')
        self.status.place(x = 130, y = 60)

        self.butok_aut = Button(self.root3, text = 'AUTENTICAR', command = self.Ok_aut).place(x = 40, y = 100)
        self.butcancel_aut = Button(self.root3, text = 'CANCELAR', command = self.Cancel_aut).place(x = 230, y = 100)



        self.root3.mainloop()


    def Cancel_aut(self):
        self.root3.destroy()
        self.root2.destroy()
    
    def Ok_aut(self):
        self.password = self.entry_password.get()

        if (self.password != 'root'):
            self.status["text"] = 'Senha inválida!'

        else:
            self.id = str(self.row[0])
            self.cursor.execute('''DELETE FROM turma WHERE id = ?''', (self.id,))
            self.connection.commit()
            self.connection.close()

            self.root4 = Toplevel()
            self.root4.resizable(False,False)
            self.root4.geometry('240x100+550+290')
            self.root4.title('SUCESSO')

            self.completed = Label(self.root4, text = 'Cadastro deletado! (Aperte OK para sair)').place(x = 0, y = 0)
            self.but_exit = Button(self.root4, text = 'OK', width = 20, command = self.Exit).place(x = 50, y = 50)
            self.root4.mainloop()

    def Exit(self):
        self.root4.destroy()
        self.root3.destroy()
        self.root2.destroy()
#------------------------------------------------------------------------------------------------------------


class Gerador:

    def __init__(self, master=None):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.geometry('250x100') 
        self.root.title('Gerar ata')

        self.label_nome = Label(self.root, text = 'Digite o código da turma: ').pack()
        self.cod = Entry(self.root)
        self.cod.focus_force()
        self.cod.pack()


        self.but = Button(self.root, text = 'PESQUISAR', command = self.Ata)
        self.but.pack()


        self.status = Label(self.root, text = '')
        self.status.pack()

        self.root.mainloop()
    
    def Ata(self):
        self.cod2 = self.cod.get().upper()
        self.sql = 'SELECT * FROM turma'
        self.sql2 = 'SELECT * FROM professor'
        self.sql3 = 'SELECT * FROM aluno'
        self.sql4 = 'SELECT * FROM disciplina'
        self.condition_existence = False
        self.connection = sqlite3.connect('CRUD.db')
        self.cursor = self.connection.cursor()
        self.arquivo = open('ATA.txt', 'w')

        for self.row in self.cursor.execute(self.sql):
            
            if (self.cod2 == self.row[1]):
                self.condition_existence = True
                self.status["text"] = ''

                self.show = '-> Código da turma:  {}    Período:  {}    Código da disciplina: {}\n'.format(self.row[1], self.row[2], self.row[3])
                self.arquivo.write(self.show)
                self.arquivo.flush()                
                
                for self.row4 in self.cursor.execute(self.sql4):
                    if (self.row[3] == self.row4[2]):
                        self.show2 = '-> Nome da disciplina: {}\n'.format(self.row4[1])
                        self.arquivo.write(self.show2)
                        self.arquivo.flush()


                self.arquivo.write('\n-> PROFESSOR(ES):\n')
                self.arquivo.flush()


                self.rowprof = self.row[4].split('//')
                self.rowaluno = self.row[5].split('//')


                for i in range(len(self.rowprof) - 1):
                    if (self.rowprof[i] == ''):
                        del(self.rowprof[i])
                    
                    else:
                        for self.row2 in self.cursor.execute(self.sql2):
                            if (self.rowprof[i] == self.row2[2]):
                                self.show3 = '-> NOME: {}   CPF: {} \n'.format(self.row2[1], self.row2[2])
                                self.arquivo.write(self.show3)
                                self.arquivo.flush()
                
                self.arquivo.write('\n-> ALUNOS:\n')
                self.arquivo.flush()

                for j in range(len(self.rowaluno) - 1):
                    if(self.rowaluno[j] == ''):
                        del(self.rowaluno[i])
                    
                    else:
                        for self.row3 in self.cursor.execute(self.sql3):
                            if (self.rowaluno[j] == self.row3[2]):
                                self.show4 = '-> NOME: {}   CPF: {} \n'.format(self.row3[1], self.row3[2])
                                self.arquivo.write(self.show4)
                                self.arquivo.flush()
                
                self.status['fg'] = 'green'
                self.status['text'] = 'ATA GERADA'

                    
                

        
        if (self.condition_existence == False):
            self.status["text"] = 'Cadastro não encontrado !!'
            self.status["fg"] = 'red' 
        
        self.connection.close() 

try:
    Initialwindow()


except:
    raise Exception('Deu erro no Initialwindow ')


#Gerador()
