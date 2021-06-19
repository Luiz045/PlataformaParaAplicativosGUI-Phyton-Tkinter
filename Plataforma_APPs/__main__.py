# IMPORTAÇÃO DE MODULOS.
import tkinter
import shelve
import threading
import Logica_jogo_da_velha
from time import sleep
from Fontes import *
from Cores import *


class login(object):

    #INICIA O OBJETO
    def __init__(self, mestre):

        #INSTANCIA DE TK.
        self.interface = mestre

        #ABRE A BASE DE DADOS.
        self.data = shelve.open('data_base')

        # DEFINE OS PARAMETROS DA INSTANCIA DE TK.
        self.interface.title('LOGIN')
        self.interface.geometry("250x260")
        self.interface.resizable(False, False)
        self.interface['bg'] = 'SystemButtonFace'

        # VARIAVEL PARA FUNÇAO LEMBRAR.
        self.setlembrar = tkinter.IntVar(0)

        # CRIA OS FRAMES DA INTERFACE.
        self.nada = tkinter.Label(self.interface, pady=6, text=' ')
        self.frame1 = tkinter.Frame(self.interface)
        self.frame2 = tkinter.Frame(self.interface, pady=4)
        self.frame3 = tkinter.Frame(self.interface)

        #EMPACOTA OS FRAMES DA INTERFACE
        self.nada.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        #CRIA OS ELEMENTOS DA INTERFACE DE LOGIN.
        self.usuariotxt = tkinter.Label(self.frame1, text='Usuário')
        self.usuarioentry = tkinter.Entry(self.frame1)
        self.senhatxt = tkinter.Label(self.frame1, text='Senha')
        self.senhaentry = tkinter.Entry(self.frame1, show='*')
        self.lembrar = tkinter.Checkbutton(self.frame1, text='Lembrar', variable=self.setlembrar, command=self.lembrar)
        self.mensagem = tkinter.Label(self.frame2)
        self.entrar = tkinter.Button(self.frame3, text='Entrar', command=self.fazer_login, fg='green', padx=15)
        self.novo = tkinter.Button(self.frame3, text='Novo', command=self.mostra_criar, fg='blue', padx=15)

        # CRIA OS ELEMENTOS DA INTERFACE DE CRIAR USUARIO.
        self.nometxt = tkinter.Label(self.frame1, text='Nome')
        self.nomeentry = tkinter.Entry(self.frame1)
        self.emailtxt = tkinter.Label(self.frame1, text='E-mail')
        self.emailentry = tkinter.Entry(self.frame1)
        self.voltar = tkinter.Button(self.frame3, text='Voltar', command=self.mostra_login, padx=15)
        self.criar = tkinter.Button(self.frame3, text='Criar', command=self.criar_usuario, fg='green', padx=15)

        # CRIA REGISTRO DO ULTIMO USUARIO CASO NAO EXISTA
        if 'ultimo<>:/?' not in self.data:
            self.data['ultimo<>:/?'] = ['', '']
        else:
            # VERIFICA SE A FUNÇAO LEMBRAR ESTA ATIVADA.
            if 'lembrar<>:/?' in self.data:
                if self.data['lembrar<>:/?'] == 1:
                    self.setlembrar.set(1)
                    self.usuarioentry.insert(0, self.data['ultimo<>:/?'][0])
                    self.senhaentry.insert(0, self.data['ultimo<>:/?'][1])

        # MOSTRA INTERFACE DE LOGIN.
        self.usuariotxt.pack()
        self.usuarioentry.pack()
        self.senhatxt.pack()
        self.senhaentry.pack()
        self.mensagem.pack()
        self.lembrar.pack()
        self.entrar.pack(side=tkinter.LEFT)
        self.novo.pack()

    def fazer_login(self):
        """
        METODO PARA FAZER LOGIN.
        """
        #VERIFICA EXISTENCIA DO USUARIO E SENHA.
        try:
            usuario_atual = self.usuarioentry.get()
            senha_atual = self.senhaentry.get()
            if self.data[usuario_atual]['senha'] == senha_atual:
                self.mensagem['text'] = f'Bem vindo {usuario_atual}!'
                self.mensagem['fg'] = 'blue'
                if self.setlembrar.get() == 1:
                    self.data['ultimo<>:/?'] = [usuario_atual, senha_atual]
                    self.data.close()
                    self.destroy_login()
                    self.inicia_aplicacao(usuario_atual)
            else:
                self.mensagem['text'] = 'Senha inválida'
                self.mensagem['fg'] = 'red'
        except:
            self.mensagem['text'] = 'Usuário inválido'
            self.mensagem['fg'] = 'red'

    def criar_usuario(self):
        """
        METODO PARA CRIAR NOVO USUARIO.
        """
        #VERIFICA CAMPOS DIGITADOS E CRIA NOVO USUARIO.
        email = self.emailentry.get()
        usuario = self.usuarioentry.get()
        senha = self.senhaentry.get()
        nome = self.nomeentry.get()
        for c in self.data:
            if c == 'lembrar<>:/?' or 'ultimo<>:/?':
                pass
            elif email == self.data[c]['email']:
                print('ok')
                self.mensagem['text'] = 'E-mail já cadastrado.'
                self.mensagem['fg'] = 'red'
                break

        if usuario == '' or senha == '' or email == '' or nome == '':
            self.mensagem['text'] = 'Todos os campos devem ser preenchidos.'
            self.mensagem['fg'] = 'red'

        elif usuario in self.data:
            self.mensagem['text'] = 'Nome de usuário em uso.'
            self.mensagem['fg'] = 'red'

        elif self.mensagem['text'] == 'E-mail já cadastrado.':
            pass

        else:
            self.data[usuario] = {'nome': nome, 'email': email, 'senha': senha}
            self.mensagem['text'] = 'Usuário criado com sucesso!'
            self.mensagem['fg'] = 'blue'

    def lembrar(self):
        """
        METODO PARA LEMBRAR USUÁRIO.
        """
        self.data['lembrar<>:/?'] = self.setlembrar.get()
        if self.setlembrar.get() == 0:
            self.data['ultimo<>:/?'] = ['', '']

    def mostra_login(self):
        """
        METODO PARA MOSTRAR ELEMENTOS DE LOGIN.
        """
        self.esconde_criar()

        # EMPACOTA OS ELEMENTOS DA INTERFACE DE LOGIN.
        self.usuariotxt.pack()
        self.usuarioentry.pack()
        self.senhatxt.pack()
        self.senhaentry.pack()
        self.mensagem.pack()
        self.lembrar.pack()
        self.entrar.pack(side=tkinter.LEFT)
        self.novo.pack()

    def mostra_criar(self):
        """
        METODO PARA MOSTRAR ELEMENTOS DE CRIAR.
        """
        self.esconde_login()

        #EMPACOTA OS ELEMENTOS DA INTERFACE DE CRIAR.
        self.nometxt.pack()
        self.nomeentry.pack()
        self.emailtxt.pack()
        self.emailentry.pack()
        self.usuariotxt.pack()
        self.usuarioentry.pack()
        self.senhatxt.pack()
        self.senhaentry.pack()
        self.voltar.pack(side=tkinter.LEFT)
        self.criar.pack()
        self.mensagem.pack()

    def esconde_login(self):
        """
        METODO PARA ESCONDER ELEMENTOS DE LOGIN.
        """
        #LIMPA DADOS VISUAIS
        self.usuarioentry.delete(0, tkinter.END)
        self.senhaentry.delete(0, tkinter.END)
        self.mensagem['text'] = ''

        #ESCONDE OS ELEMENTOS DA INTERFACE DE LOGIN.
        self.usuariotxt.forget()
        self.usuarioentry.forget()
        self.senhatxt.forget()
        self.senhaentry.forget()
        self.mensagem.forget()
        self.lembrar.forget()
        self.entrar.forget()
        self.novo.forget()

    def esconde_criar(self):
        """
        METODO PARA ESCONDER ELEMENTOS DE CRIAR.
        """
        #LIMPA DADOS VISUAIS
        self.nomeentry.delete(0, tkinter.END)
        self.emailentry.delete(0, tkinter.END)
        self.usuarioentry.delete(0, tkinter.END)
        self.senhaentry.delete(0, tkinter.END)
        self.mensagem['text'] = ''

        # ESCONDE OS ELEMENTOS DA INTERFACE DE CRIAR.
        self.nometxt.forget()
        self.nomeentry.forget()
        self.emailtxt.forget()
        self.emailentry.forget()
        self.usuariotxt.forget()
        self.usuarioentry.forget()
        self.senhatxt.forget()
        self.senhaentry.forget()
        self.criar.forget()
        self.mensagem.forget()
        self.voltar.forget()

    def destroy_login(self):
        self.nometxt.destroy()
        self.nomeentry.destroy()
        self.emailtxt.destroy()
        self.emailentry.destroy()
        self.usuariotxt.destroy()
        self.usuarioentry.destroy()
        self.senhatxt.destroy()
        self.senhaentry.destroy()
        self.voltar.destroy()
        self.criar.destroy()
        self.mensagem.destroy()
        self.lembrar.destroy()
        self.entrar.destroy()
        self.novo.destroy()
        self.nada.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()

    def inicia_aplicacao(self, usuario):
        Menu(self.interface, usuario)


class Menu(object):
    def __init__(self, mestre, usuario, anula=False):
        self.interface = mestre
        self.usuario = usuario
        self.interface.title('APLICATIVOS')
        self.interface.geometry('1000x600')

        #CRIA FRAMES DO MENU.
        self.frame1 = tkinter.Frame(self.interface)
        self.frame2 = tkinter.Frame(self.interface)
        self.frame1.pack()
        self.frame2.pack()

        #CRIA ELEMENTOS DO MENU.
        if anula:
            self.mensagem = tkinter.Label(self.interface, text=f'Usuario: {self.usuario}', pady=10)
        else:
            self.mensagem = tkinter.Label(self.interface, text=f'Bem vindo, {self.usuario}!', pady=10)
        self.menu = tkinter.Label(self.interface, text='* Aplicativos *', pady=8)
        self.nada = tkinter.Label(self.interface, text='', pady=10)
        self.app1_linhas = tkinter.Button(self.interface, text='Traço mágico', command=self.app_linhas,
                                          padx=250, pady=6)
        self.app2_velha = tkinter.Button(self.interface, text='Jogo da velha', command=self.app_velha,
                                          padx=250, pady=6)
        self.sair = tkinter.Button(self.interface, text='LOGOUT', command=self.logout, padx=1000, font=fonte_sair)

        #EDITA OS FUNDOS.
        self.interface['bg'] = cinza
        self.mensagem['bg'] = cinza
        self.menu['bg'] = cinza
        self.nada['bg'] = cinza
        self.app1_linhas['bg'] = roxo
        self.app2_velha['bg'] = verde_fosco

        #EDITA AS FONTES.
        self.mensagem['font'] = fonte_bemvindo
        self.menu['font'] = fonte_titulo
        self.app1_linhas['font'] = fonte_linhas
        self.app2_velha['font'] = fonte_linhas

        #EDITA A COR DE TEXTO.
        self.mensagem['fg'] = azul_claro
        self.menu['fg'] = 'white'
        self.app1_linhas['fg'] = '#FDF5E6'
        self.app2_velha['fg'] = '#FDF5E6'

        #MOSTRA MENU.
        self.mensagem.pack()
        self.menu.pack()
        self.nada.pack()
        self.app1_linhas.pack()
        self.app2_velha.pack()
        self.sair.pack(side=tkinter.BOTTOM)

    def esconde_menu(self):
        """
        METODO PARA ESCONDER O MENU.
        """
        self.mensagem.forget()
        self.menu.forget()
        self.nada.forget()
        self.app1_linhas.forget()
        self.app2_velha.forget()
        self.sair.forget()

    def app_linhas(self):
        self.esconde_menu()
        linhas(self.interface, self.usuario)

    def app_velha(self):
        self.esconde_menu()
        jogo_velha(self.interface, self.usuario)

    def logout(self):
        self.esconde_menu()
        login(self.interface)


class linhas(object):
    def __init__(self, instancia, usuario):
        self.interface = instancia
        self.usuario = usuario
        self.interface.title('TRAÇO MAGICO')

        #CONSTANTES
        self.x_inicio = 500
        self.y_inicio = 250
        self.x_final = self.x_inicio
        self.y_final = self.y_inicio

        #FRAMES
        self.frame0 = tkinter.Frame(self.interface)
        self.frame1 = tkinter.Frame(self.interface)

        #ELEMENTOS VISUAIS DO JOGO.
        self.nada = tkinter.Label(self.frame0, text=' ')
        self.nada0 = tkinter.Label(self.frame1, padx=30, text=' ')
        self.nada1 = tkinter.Label(self.frame1, padx=30, text=' ')
        self.nada2 = tkinter.Label(self.frame1, padx=30, text=' ')
        self.tela = tkinter.Canvas(self.interface, bg=cinza, width=1000, height=480)
        self.esquerda_b = tkinter.Button(self.frame1, text='Esquerda', command=self.esquerda, width=20, pady=10)
        self.sobe_b = tkinter.Button(self.frame1, text='Para cima', command=self.sobe, width=20, pady=10)
        self.desce_b = tkinter.Button(self.frame1, text='Para baixo', command=self.desce, width=20, pady=10)
        self.direita_b = tkinter.Button(self.frame1, text='Direita', command=self.direita, width=20, pady=10)
        self.voltar = tkinter.Button(self.interface, text='SAIR', command=self.sair, padx=1000, font=fonte_sair)

        #DEFINE AS CORES.
        self.frame0['bg'] = cinza
        self.frame1['bg'] = cinza
        self.nada['bg'] = cinza
        self.nada0['bg'] = cinza
        self.nada1['bg'] = cinza
        self.nada2['bg'] = cinza
        self.voltar['bg'] = cinza

        self.esquerda_b['fg'] = 'white'
        self.direita_b['fg'] = 'white'
        self.sobe_b['fg'] = 'white'
        self.desce_b['fg'] = 'white'
        self.voltar['fg'] = 'white'

        self.esquerda_b['bg'] = vermelho_fosco
        self.direita_b['bg'] = azul_fosco
        self.sobe_b['bg'] = verde_fosco
        self.desce_b['bg'] = amarelo_fosco

        #DEFINE AS FONTES
        self.esquerda_b['font'] = fonte_botoes
        self.direita_b['font'] = fonte_botoes
        self.sobe_b['font'] = fonte_botoes
        self.desce_b['font'] = fonte_botoes

        #MOSTRA ELEMENTOS.
        self.voltar.pack()
        self.tela.pack()
        self.frame0.pack()
        self.frame1.pack()
        self.nada.pack()
        self.esquerda_b.pack(side=tkinter.LEFT)
        self.nada0.pack(side=tkinter.LEFT)
        self.sobe_b.pack(side=tkinter.LEFT)
        self.nada1.pack(side=tkinter.LEFT)
        self.desce_b.pack(side=tkinter.LEFT)
        self.nada2.pack(side=tkinter.LEFT)
        self.direita_b.pack(side=tkinter.LEFT)
        self.iteravel = 1

    def esquerda(self):
        self.x_final -= 10
        self.tela.create_line(self.x_inicio, self.y_inicio, self.x_final, self.y_inicio, fill='red')
        self.x_inicio = self.x_final

    def direita(self):
        self.x_final += 10
        self.tela.create_line(self.x_inicio, self.y_inicio, self.x_final, self.y_inicio, fill='blue')
        self.x_inicio = self.x_final

    def sobe(self):
        self.y_final -= 10
        self.tela.create_line(self.x_inicio, self.y_inicio, self.x_final, self.y_final, fill='green')
        self.y_inicio = self.y_final

    def desce(self):
        self.y_final += 10
        self.tela.create_line(self.x_inicio, self.y_inicio, self.x_final, self.y_final, fill='yellow')
        self.y_inicio = self.y_final

    def destroy(self):
        self.tela.destroy()
        self.frame0.destroy()
        self.frame1.destroy()
        self.nada.destroy()
        self.esquerda_b.destroy()
        self.nada0.destroy()
        self.sobe_b.destroy()
        self.nada1.destroy()
        self.desce_b.destroy()
        self.nada2.destroy()
        self.direita_b.destroy()
        self.voltar.destroy()

    def sair(self):
        self.destroy()
        Menu(self.interface, self.usuario, True)

    def animacao(self):
        for c in range(self.iteravel):
            self.direita()
        for c in range(self.iteravel):
            self.desce()
        self.iteravel += 1
        for c in range(self.iteravel):
            self.esquerda()
        for c in range(self.iteravel):
            self.sobe()
        self.iteravel += 1


class jogo_velha(object):
    def __init__(self, mestre, usuario):
        self.interface = mestre
        self.usuario = usuario
        self.minhavez = False
        self.tabuleiro = []
        for linha in range(3):
            self.tabuleiro.append([])
            for coluna in range(3):
                self.tabuleiro[linha].append(0)

        self.interface['bg'] = cinza
        self.interface.title('JOGO DA VELHA')
        self.interface.geometry('1000x600')

        #FRAMES DA INTERFACE.
        self.frame0 = tkinter.Frame(self.interface, bg=cinza)
        self.frame1 = tkinter.Frame(self.interface, bg=cinza)
        self.frame2 = tkinter.Frame(self.interface, bg=cinza)
        self.framel0 = tkinter.Frame(self.frame2, bg=cinza)
        self.framel1 = tkinter.Frame(self.frame2, bg=cinza)
        self.framel2 = tkinter.Frame(self.frame2, bg=cinza)

        #elementos para ajuste da interface.
        self.mensagem = tkinter.Label(self.frame0, bg=cinza, pady=20, font=fonte_mensagem_v)
        self.nada = tkinter.Label(self.frame1, text='', padx=205, bg=cinza)
        self.title = tkinter.Label(self.frame1, text='Jogo da velha', pady=10, bg=cinza, font=fonte_title_v, fg=azul_claro)
        self.t0x0 = tkinter.Button(self.framel0, text='', command=self.c0x0, padx=25, pady=20)
        self.t0x1 = tkinter.Button(self.framel0, text='', command=self.c0x1, padx=25, pady=20)
        self.t0x2 = tkinter.Button(self.framel0, text='', command=self.c0x2, padx=25, pady=20)
        self.t1x0 = tkinter.Button(self.framel1, text='', command=self.c1x0, padx=25, pady=20)
        self.t1x1 = tkinter.Button(self.framel1, text='', command=self.c1x1, padx=25, pady=20)
        self.t1x2 = tkinter.Button(self.framel1, text='', command=self.c1x2, padx=25, pady=20)
        self.t2x0 = tkinter.Button(self.framel2, text='', command=self.c2x0, padx=25, pady=20)
        self.t2x1 = tkinter.Button(self.framel2, text='', command=self.c2x1, padx=25, pady=20)
        self.t2x2 = tkinter.Button(self.framel2, text='', command=self.c2x2, padx=25, pady=20)
        self.voltar = tkinter.Button(self.interface, text='SAIR', command=self.sair, padx=1000, font=fonte_sair, fg=vermelho_fosco)
        self.denovo = tkinter.Button(self.interface, text='NOVO JOGO', command=self.novo_jogo, padx=1000, font=fonte_sair, fg=verde_fosco)

        self.mensagem['text'] = 'Faça uma jogada:'
        self.mensagem['fg'] = 'green'

        self.mostra_jogo()

    def mostra_jogo(self):
        self.voltar.pack()
        self.denovo.pack()
        self.frame0.pack()
        self.mensagem.pack()
        self.frame1.pack(side=tkinter.LEFT)
        self.frame2.pack(side=tkinter.LEFT)
        self.framel0.pack()
        self.framel1.pack()
        self.framel2.pack()

        # elementos para ajuste da interface.
        self.title.pack()
        self.nada.pack()
        self.t0x0.pack(side=tkinter.LEFT)
        self.t0x1.pack(side=tkinter.LEFT)
        self.t0x2.pack(side=tkinter.LEFT)
        self.t1x0.pack(side=tkinter.LEFT)
        self.t1x1.pack(side=tkinter.LEFT)
        self.t1x2.pack(side=tkinter.LEFT)
        self.t2x0.pack(side=tkinter.LEFT)
        self.t2x1.pack(side=tkinter.LEFT)
        self.t2x2.pack(side=tkinter.LEFT)

    def fazer_jogada(self):
        results = Logica_jogo_da_velha.resultado(self.tabuleiro)
        if not results:
            self.mensagem['text'] = 'Calculando'
            self.mensagem['fg'] = amarelo_fosco
            sleep(0.1)
            self.mensagem['text'] = 'Calculando.'
            sleep(0.1)
            self.mensagem['text'] = 'Calculando..'
            sleep(0.1)
            self.mensagem['text'] = 'Calculando...'
            sleep(0.2)
            self.mensagem['text'] = 'Sua vez:'
            self.mensagem['fg'] = 'green'
            jogada = Logica_jogo_da_velha.jogar(self.tabuleiro)
            self.tabuleiro[jogada[0]][jogada[1]] = -1
            if jogada == [0, 0]:
                self.t0x0['bg'] = vermelho_fosco
            elif jogada == [0, 1]:
                self.t0x1['bg'] = vermelho_fosco
            elif jogada == [0, 2]:
                self.t0x2['bg'] = vermelho_fosco
            elif jogada == [1, 0]:
                self.t1x0['bg'] = vermelho_fosco
            elif jogada == [1, 1]:
                self.t1x1['bg'] = vermelho_fosco
            elif jogada == [1, 2]:
                self.t1x2['bg'] = vermelho_fosco
            elif jogada == [2, 0]:
                self.t2x0['bg'] = vermelho_fosco
            elif jogada == [2, 1]:
                self.t2x1['bg'] = vermelho_fosco
            elif jogada == [2, 2]:
                self.t2x2['bg'] = vermelho_fosco
            self.minhavez = False
        results = Logica_jogo_da_velha.resultado(self.tabuleiro)
        if results != False:
            self.minhavez = True
            if results == 'perdi':
                self.mensagem['text'] = 'Parabens, voce venceu!!'
                self.mensagem['fg'] = 'green'
            elif results == 'ganhei':
                self.mensagem['text'] = 'você perdeu!'
                self.mensagem['fg'] = 'red'
            elif results == 'cheio':
                self.mensagem['text'] = 'Empatou.'
                self.mensagem['fg'] = 'white'

    def c0x0(self):
        if not self.minhavez:
            if self.t0x0['bg'] == 'SystemButtonFace':
                self.t0x0['bg'] = verde_fosco
                self.tabuleiro[0][0] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c0x1(self):
        if not self.minhavez:
            if self.t0x1['bg'] == 'SystemButtonFace':
                self.t0x1['bg'] = verde_fosco
                self.tabuleiro[0][1] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c0x2(self):
        if not self.minhavez:
            if self.t0x2['bg'] == 'SystemButtonFace':
                self.t0x2['bg'] = verde_fosco
                self.tabuleiro[0][2] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c1x0(self):
        if not self.minhavez:
            if self.t1x0['bg'] == 'SystemButtonFace':
                self.t1x0['bg'] = verde_fosco
                self.tabuleiro[1][0] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c1x1(self):
        if not self.minhavez:
            if self.t1x1['bg'] == 'SystemButtonFace':
                self.t1x1['bg'] = verde_fosco
                self.tabuleiro[1][1] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c1x2(self):
        if not self.minhavez:
            if self.t1x2['bg'] == 'SystemButtonFace':
                self.t1x2['bg'] = verde_fosco
                self.tabuleiro[1][2] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c2x0(self):
        if not self.minhavez:
            if self.t2x0['bg'] == 'SystemButtonFace':
                self.t2x0['bg'] = verde_fosco
                self.tabuleiro[2][0] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c2x1(self):
        if not self.minhavez:
            if self.t2x1['bg'] == 'SystemButtonFace':
                self.t2x1['bg'] = verde_fosco
                self.tabuleiro[2][1] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def c2x2(self):
        if not self.minhavez:
            if self.t2x2['bg'] == 'SystemButtonFace':
                self.t2x2['bg'] = verde_fosco
                self.tabuleiro[2][2] = 1
                self.minhavez = True
                threading.Thread(target=self.fazer_jogada, daemon=True).start()

    def destroy(self):
        self.frame0.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.framel0.destroy()
        self.framel1.destroy()
        self.framel2.destroy()

        # elementos para ajuste da interface.
        self.nada.destroy()
        self.t0x0.destroy()
        self.t0x1.destroy()
        self.t0x2.destroy()
        self.t1x0.destroy()
        self.t1x1.destroy()
        self.t1x2.destroy()
        self.t2x0.destroy()
        self.t2x1.destroy()
        self.t2x2.destroy()
        self.mensagem.destroy()
        self.voltar.destroy()
        self.denovo.destroy()
        self.title.destroy()

    def sair(self):
        self.destroy()
        Menu(self.interface, self.usuario, True)

    def novo_jogo(self):
        self.destroy()
        self.__init__(self.interface, self.usuario)


if __name__ == '__main__':
    #Cria a tela
    tela = tkinter.Tk()
    #Configura a tela
    login(tela)
    #inicia a tela
    tela.mainloop()
