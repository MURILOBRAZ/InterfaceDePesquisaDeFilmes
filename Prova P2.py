##Murilo Lima dos Santos Braz - 202873
import sqlite3
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label

conexao = sqlite3.connect('D:/Usuários/Pichau/Desktop/P2/bdP2.db')
class Tela(ScreenManager):
    pass

class P2_2022(App):
    def build(self):
        return Tela()
    def Verifica(self, senha, usuario, scman, label):
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM login WHERE usuario = ?',(usuario.text,))
        lista = cursor.fetchall()
        if lista[0][0] == usuario.text:
            if lista[0][1] == senha.text:
                scman.current = 'telaPesquisa'
            else:
                label.text = 'Senha Errada'
        else:
            label.text = 'Usuario Errada'
        
    def inserir(self, senha, usuario, label):
        conexao.execute('INSERT INTO login VALUES(?,?)',(usuario.text, senha.text,))
        conexao.commit()
        label.text = 'USUARIO CADASTRADO COM SUCESSO'
        
    def pesquisa(self,ano,ano2,label):
        label.text = ''
        ano = str(ano.value)
        ano2 = str(ano2.value)
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM filmes WHERE ano < ? AND ano > ?',(ano2, ano,))
        lista = cursor.fetchall()
        for x in lista:
            label.text += str(x[0]) + '-' + str(x[1]) + '-' + str(x[2]) + '\n'
        
P2_2022().run()
