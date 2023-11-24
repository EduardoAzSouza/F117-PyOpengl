# Eduardo Azeni de Souza
# RA: 106270

# CONTROLES DE MOVIMENTO DA CAMERA:
    # Setas (Direita, Esquerda, Cima, Baixo)
    # PageUp e PageDown
    # Home
    # End

# CONTROLE DE MOVIMENTO DO AVIAO:
    # W flaps para baixo
    # S flaps para cima
    # A vira para Esquerda e mexe os flaps
    # D vira para Direita e mexe os flaps
    # Q vira os lemes para Esquerda
    # E vira os lemes para Direita
    # G Acelera
    # B Desacelera

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

px = 10
py = -30
pz = 0
ty = 0
fe = 0
fd = 0
speed = 30
direcao = 0
faixaZ1 = 40
faixaZ2 = 20
faixaZ3 = 0
faixaZ4 = -20
faixaZ5 = -40

def drawC():
    
    glRotatef(px, 1, 0, 0) # Rotaciona em relação ao eixo X (Setas cima e baixo)
    glRotatef(py, 0, 1, 0) # Rotaciona em relação ao eixo Y (Setas direita e esquerda)
    glRotatef(pz, 0, 0, 1) # Rotaciona em relação ao eixo Z (teclas PgUp e PgDn)
    glTranslatef(0, 0, 15)
#----------------------------------------------------------------------------------------------
    glRotatef(ty, 0, 0, 1)

    #Base =========================================
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, 0.0)
    glVertex3f(-5.15, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 12.5)
    glEnd()
    glColor3f(0.25, 0.25, 0.25)
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, 0.0)
    glVertex3f(-5.15, 0.0, 0.0)
    glVertex3f(-5.15, 0.0, -17.25)
    glVertex3f(5.15, 0.0, -17.25) 
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, -17.25)
    glVertex3f(5.15, 0.0, -17.25)
    glVertex3f(0.0, 0.0, -22.5)
    glEnd()
    #Base =========================================
    #Bordas e traseira ============================
    glColor3f(1, 0.5, 0)
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, -17.25)
    glVertex3f(0.0, 0.0, -22.5)
    glVertex3f(0.0, 0.2, -22.5)
    glVertex3f(-5.15, 0.2, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, -17.25)
    glVertex3f(0.0, 0.0, -22.5)
    glVertex3f(0.0, 0.2, -22.5)
    glVertex3f(5.15, 0.2, -17.25)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, -17.25)
    glVertex3f(-5.15, 0.2, -17.25)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-5.15, 0.0, -10.45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, -17.25)
    glVertex3f(5.15, 0.2, -17.25)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(5.15, 0.0, -10.45)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 4.5, 3.25)
    glVertex3f(0.0, 0.2, -22.5)
    glVertex3f(5.15, 0.2, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 4.5, 3.25)
    glVertex3f(0.0, 0.2, -22.5)
    glVertex3f(-5.15, 0.2, -17.25)
    glEnd()
    #Bordas e traseira ============================
    #Cabine =======================================
        #Bico
       #ponta superior do bico sme encaixe de vertice
       #bordas sem ponto fixo
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(1.24, 0.0, 9.5)
    glVertex3f(0.0, 0.0, 12.5)
    glVertex3f(0.0, 1.5, 7.4)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1.24, 0.0, 9.5)
    glVertex3f(0.0, 0.0, 12.5)
    glVertex3f(0.0, 1.5, 7.4)
    glEnd()
        #Frente
    glColor3f(0.25, 0.25, 0.25)
    glBegin(GL_POLYGON)
    glVertex3f(1.24, 0.0, 9.5)
    glVertex3f(0, 4.5, 3.25)
    glVertex3f(-1.24, 0.0, 9.5)
    glEnd()
        #janela
    glColor3f(0.45, 0.45, 1)
    glBegin(GL_POLYGON)
    glVertex3f(0.4, 2.6, 6)
    glVertex3f(0.0, 4, 4)
    glVertex3f(-0.4, 2.6, 6)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.65, 2.6, 5.8)
    glVertex3f(-0.22, 4, 3.9)
    glVertex3f(-0.9, 2.6, 5.3)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.65, 2.6, 5.8)
    glVertex3f(0.22, 4, 3.9)
    glVertex3f(0.9, 2.6, 5.3)
    glEnd()

    #Cabine =======================================
    #Lado Direito =================================
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-1.24, 0.0, 9.5)
    glVertex3f(0, 4.5, 3.25)
    glVertex3f(-2.06, 0.0, 7.5)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-2.06, 0.0, 7.5)
    glVertex3f(-0, 4.5, 3.25)
    glVertex3f(-2.2, 2.6, 2.8)
    glEnd()
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(-2.06, 0.0, 7.5)
    glVertex3f(-2.2, 2.6, 2.8)
    glVertex3f(-3.2, 0.25, 3.31)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-2.06, 0.0, 7.5)
    glVertex3f(-3.2, 0.25, 3.31)
    glVertex3f(-5.15, 0.0, 0.0)
    glEnd()
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-3.8, 1.5, 0.35)
    glVertex3f(-5.15, 0.0, 0.0)
    glVertex3f(-3.2, 0.25, 3.31)
    glVertex3f(-2.2, 2.6, 2.8)
    glEnd()
        #Sem encaixe certo no terceiro vertice
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-5.15, 0.2, -17.25)
    glVertex3f(-2.6, 2.32, -7.2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.6, 2.32, -7.2)
    glVertex3f(0, 4.5, 3.25)
    glVertex3f(-2.2, 2.6, 2.8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-5.15, 0.0, 0.0)
    glVertex3f(-3.8, 1.5, 0.35)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-3.8, 1.5, 0.35)
    glVertex3f(-2.2, 2.6, 2.8)
    glVertex3f(-2.6, 2.32, -7.2)
    glEnd()
    #Lado Direito =================================
    #Lado Esquerdo ================================
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(1.24, 0.0, 9.5)
    glVertex3f(0, 4.5, 3.25)
    glVertex3f(2.06, 0.0, 7.5)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(2.06, 0.0, 7.5)
    glVertex3f(0, 4.5, 3.25)
    glVertex3f(2.2, 2.6, 2.8)
    glEnd()
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(2.06, 0.0, 7.5)
    glVertex3f(2.2, 2.6, 2.8)
    glVertex3f(3.2, 0.25, 3.31)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(2.06, 0.0, 7.5)
    glVertex3f(3.2, 0.25, 3.31)
    glVertex3f(5.15, 0.0, 0.0)
    glEnd()
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(3.8, 1.5, 0.35)
    glVertex3f(5.15, 0.0, 0.0)
    glVertex3f(3.2, 0.25, 3.31)
    glVertex3f(2.2, 2.6, 2.8)
    glEnd()
    #Sem encaixe certo no terceiro vertice
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(5.15, 0.2, -17.25)
    glVertex3f(2.6, 2.32, -7.2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.6, 2.32, -7.2)
    glVertex3f(0, 4.5, 3.25)
    glVertex3f(2.2, 2.6, 2.8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(5.15, 0.0, 0.0)
    glVertex3f(3.8, 1.5, 0.35)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(3.8, 1.5, 0.35)
    glVertex3f(2.2, 2.6, 2.8)
    glVertex3f(2.6, 2.32, -7.2)
    glEnd()
    #Lado Esquerdo ================================
    #Asa Direita ==================================
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, 0.0)
    glVertex3f(-5.15, 0.0, -10.45)
    glVertex3f(-13.5, 0.0, -20.8)
    glVertex3f(-13.5, 0.0, -20.0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, 0.0)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-13.5, 0.2, -20.8)
    glVertex3f(-13.5, 0.0, -20.0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-13.5, 0.0, -20.0)
    glVertex3f(-13.5, 0.0, -20.8)
    glVertex3f(-13.5, 0.2, -20.8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-5.15, 0.0, -10.45)
    glVertex3f(-13.5, 0.0, -20.8)
    glVertex3f(-13.5, 0.2, -20.8)
    glEnd()
    #Asa Direita ==================================
    #Flap Direito =================================
    glTranslatef(-5.15, 0.35, -10.45)
    glRotatef(-51, 0, 1, 0)
    glRotatef(1, 0, 0, 1)
    glRotatef(fd, 1, 0, 0)
    glRotatef(-1, 0, 0, 1)
    glRotatef(51, 0, 1, 0)
    glTranslatef(5.15, -0.35, 10.45)
    
    glColor3f(0.25, 0.25, 0.25)
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, -10.45)
    glVertex3f(-13.5, 0.0, -20.8)
    glVertex3f(-13.5, 0.0, -22.5)
    glVertex3f(-5.15, 0.0, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-13.5, 0.2, -20.8)
    glVertex3f(-13.5, 0.2, -22.5)
    glVertex3f(-5.15, 0.2, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-13.5, 0.0, -22.5)
    glVertex3f(-13.5, 0.0, -20.8)
    glVertex3f(-13.5, 0.2, -20.8)
    glVertex3f(-13.5, 0.2, -22.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-13.5, 0.2, -22.5)
    glVertex3f(-13.5, 0.0, -22.5)
    glVertex3f(-5.15, 0.0, -17.25)
    glVertex3f(-5.15, 0.2, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-5.15, 0.0, -10.45)
    glVertex3f(-13.5, 0.0, -20.8)
    glVertex3f(-13.5, 0.2, -20.8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-5.15, 0.0, -17.25)
    glVertex3f(-5.15, 0.2, -17.25)
    glVertex3f(-5.15, 0.75, -10.45)
    glVertex3f(-5.15, 0.0, -10.45)
    glEnd()

    glTranslatef(-5.15, 0.35, -10.45)
    glRotatef(-51, 0, 1, 0)
    glRotatef(1, 0, 0, 1)
    glRotatef(-fd, 1, 0, 0)
    glRotatef(-1, 0, 0, 1)
    glRotatef(51, 0, 1, 0)
    glTranslatef(5.15, -0.35, 10.45)
    #Flap Direito =================================
    #Asa Esquerda =================================
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, 0.0)
    glVertex3f(5.15, 0.0, -10.45)
    glVertex3f(13.5, 0.0, -20.8)
    glVertex3f(13.5, 0.0, -20.0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, 0.0)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(13.5, 0.2, -20.8)
    glVertex3f(13.5, 0.0, -20.0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(13.5, 0.0, -20.0)
    glVertex3f(13.5, 0.0, -20.8)
    glVertex3f(13.5, 0.2, -20.8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(5.15, 0.0, -10.45)
    glVertex3f(13.5, 0.0, -20.8)
    glVertex3f(13.5, 0.2, -20.8)
    glEnd()
    #Asa Esquerda =================================
    #Flap esquerdo ================================
    glTranslatef(5.15, 0.35, -10.45)
    glRotatef(51.5, 0, 1, 0)
    glRotatef(-1, 0, 0, 1)
    glRotatef(fe, 1, 0, 0)
    glRotatef(1, 0, 0, 1)
    glRotatef(-51.5, 0, 1, 0)
    glTranslatef(-5.15, -0.35, 10.45)
    
    glColor3f(0.25, 0.25, 0.25)
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(13.5, 0.2, -20.8)
    glVertex3f(13.5, 0.2, -22.5)
    glVertex3f(5.15, 0.2, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, -10.45)
    glVertex3f(13.5, 0.0, -20.8)
    glVertex3f(13.5, 0.0, -22.5)
    glVertex3f(5.15, 0.0, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(13.5, 0.0, -22.5)
    glVertex3f(13.5, 0.0, -20.8)
    glVertex3f(13.5, 0.2, -20.8)
    glVertex3f(13.5, 0.2, -22.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(13.5, 0.2, -22.5)
    glVertex3f(13.5, 0.0, -22.5)
    glVertex3f(5.15, 0.0, -17.25)
    glVertex3f(5.15, 0.2, -17.25)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(5.15, 0.0, -10.45)
    glVertex3f(13.5, 0.0, -20.8)
    glVertex3f(13.5, 0.2, -20.8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(5.15, 0.0, -17.25)
    glVertex3f(5.15, 0.2, -17.25)
    glVertex3f(5.15, 0.75, -10.45)
    glVertex3f(5.15, 0.0, -10.45)
    glEnd()

    glTranslatef(5.15, 0.35, -10.45)
    glRotatef(51.5, 0, 1, 0)
    glRotatef(-1, 0, 0, 1)
    glRotatef(-fe, 1, 0, 0)
    glRotatef(1, 0, 0, 1)
    glRotatef(-51.5, 0, 1, 0)
    glTranslatef(-5.15, -0.35, 10.45)
    #Flap esquerdo ================================

    lfy = 1.6
    lfz = -18.355
    lfx = 2.225
    glTranslatef(1, 1, 0)
    glRotatef(25, 0, 0, 1)
    #Leme Direito =================================
    #Fixa
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-2.3, 1.6, -21.23)
    glVertex3f(-2.3, 1.6, -15.55)
    glVertex3f(-2.3, 0.2, -13.0)
    glVertex3f(-2.3, 0.2, -19.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.15, 1.6, -21.23)
    glVertex3f(-2.15, 1.6, -15.55)
    glVertex3f(-2.15, 0.2, -13.0)
    glVertex3f(-2.15, 0.2, -19.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.3, 0.2, -13.0)
    glVertex3f(-2.15, 0.2, -13.0)
    glVertex3f(-2.15, 1.6, -15.55)
    glVertex3f(-2.3, 1.6, -15.55)
    glEnd()  
    glBegin(GL_POLYGON)
    glVertex3f(-2.3, 0.2, -19.5)
    glVertex3f(-2.15, 0.2, -19.5)
    glVertex3f(-2.15, 1.6, -21.23)
    glVertex3f(-2.3, 1.6, -21.23)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.3, 1.6, -21.23)
    glVertex3f(-2.3, 1.6, -15.55)
    glVertex3f(-2.15, 1.6, -15.55)
    glVertex3f(-2.15, 1.6, -21.23)   
    glEnd()
    #Leme Direito =================================
    #Leme Direito ============================movel
    glTranslatef(-lfx, lfy, lfz)
    glRotatef(direcao, 0, 1, 0)

    glColor3f(0.18, 0.18, 0.18)
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 3.9, -7.61)
    glVertex3f(0.075, 3.9, -4.26)
    glVertex3f(0.075, 0, 2.84)
    glVertex3f(0.075, 0, -2.84)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.075, 3.9, -7.61)
    glVertex3f(-0.075, 3.9, -4.26)
    glVertex3f(-0.075, 0, 2.84)
    glVertex3f(-0.075, 0, -2.84)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 0, 2.84)
    glVertex3f(-0.075, 0, 2.84)
    glVertex3f(-0.075, 3.9, -4.26)
    glVertex3f(0.075, 3.9, -4.26)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 0, -2.84)
    glVertex3f(0.075, 3.9, -7.61)
    glVertex3f(-0.075, 3.9, -7.61)
    glVertex3f(-0.075, 0, -2.84)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 3.9, -7.61)
    glVertex3f(0.075, 3.9, -4.26)
    glVertex3f(-0.075, 3.9, -4.26)
    glVertex3f(-0.075, 3.9, -7.61)   
    glEnd()

    glRotatef(-direcao, 0, 1, 0)
    glTranslatef(lfx, -lfy, -lfz)
    #Leme Direito ============================movel
    glRotatef(-25, 0, 0, 1)
    glTranslatef(-1, -1, 0)

    glTranslatef(-1, 1, 0)
    glRotatef(-25, 0, 0, 1)
    #Leme Esquerdo ================================
    #Fixa
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(2.3, 1.6, -21.23)
    glVertex3f(2.3, 1.6, -15.55)
    glVertex3f(2.3, 0.2, -13.0)
    glVertex3f(2.3, 0.2, -19.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.15, 1.6, -21.23)
    glVertex3f(2.15, 1.6, -15.55)
    glVertex3f(2.15, 0.2, -13.0)
    glVertex3f(2.15, 0.2, -19.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.3, 0.2, -13.0)
    glVertex3f(2.15, 0.2, -13.0)
    glVertex3f(2.15, 1.6, -15.55)
    glVertex3f(2.3, 1.6, -15.55)
    glEnd()  
    glBegin(GL_POLYGON)
    glVertex3f(2.3, 0.2, -19.5)
    glVertex3f(2.15, 0.2, -19.5)
    glVertex3f(2.15, 1.6, -21.23)
    glVertex3f(2.3, 1.6, -21.23)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.3, 1.6, -21.23)
    glVertex3f(2.3, 1.6, -15.55)
    glVertex3f(2.15, 1.6, -15.55)
    glVertex3f(2.15, 1.6, -21.23)   
    glEnd()
    #Leme Esquerdo ================================
    #Leme Esquerdo ===========================movel
    glTranslatef(lfx, lfy, lfz)
    glRotatef(direcao, 0, 1, 0)

    glColor3f(0.18, 0.18, 0.18)
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 3.9, -7.61)
    glVertex3f(0.075, 3.9, -4.26)
    glVertex3f(0.075, 0, 2.84)
    glVertex3f(0.075, 0, -2.84)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.075, 3.9, -7.61)
    glVertex3f(-0.075, 3.9, -4.26)
    glVertex3f(-0.075, 0, 2.84)
    glVertex3f(-0.075, 0, -2.84)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 0, 2.84)
    glVertex3f(-0.075, 0, 2.84)
    glVertex3f(-0.075, 3.9, -4.26)
    glVertex3f(0.075, 3.9, -4.26)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 0, -2.84)
    glVertex3f(0.075, 3.9, -7.61)
    glVertex3f(-0.075, 3.9, -7.61)
    glVertex3f(-0.075, 0, -2.84)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.075, 3.9, -7.61)
    glVertex3f(0.075, 3.9, -4.26)
    glVertex3f(-0.075, 3.9, -4.26)
    glVertex3f(-0.075, 3.9, -7.61)   
    glEnd()
    glRotatef(-direcao, 0, 1, 0)
    glTranslatef(-lfx, -lfy, -lfz)
    #Leme Esquerdo ===========================movel
    glRotatef(25, 0, 0, 1)
    glTranslatef(1, -1, 0)
    

    glRotatef(-ty, 0, 0, 1)
    #---------------------------------------------------------------------------------------------- 

    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-8, -4.5, (faixaZ1-7))
    glVertex3f(-8, -4.5, faixaZ1)
    glEnd()

    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex3f(8, 10, (faixaZ2-7))
    glVertex3f(8, 10, faixaZ2)
    glEnd()

    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex3f(10, -9, (faixaZ3-7))
    glVertex3f(10, -9, faixaZ3)
    glEnd()
    
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-6, 5, (faixaZ4-7))
    glVertex3f(-6, 5, faixaZ4)
    glEnd()

    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex3f(12, 3, (faixaZ5-7))
    glVertex3f(12, 3, faixaZ5)
    glEnd()

    # < Cenário
    
    #----------------------------------------------------------------------------------------------
    glTranslatef(22, 15, faixaZ5) 
    glColor4f(1, 1, 1, 0)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(1,1,1)
    glTranslatef(1,1,1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,-1)
    glTranslatef(1,-1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,1,1)
    glTranslatef(1,1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,1)
    glTranslatef(2,1,1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-2,1,1)
    glTranslatef(-22, -15, -faixaZ5) 

    glTranslatef(-22, 15, faixaZ1) 
    glRotate(150, 1, 1, 0)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(1,1,1)
    glTranslatef(1,1,1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,-1)
    glTranslatef(1,-1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,1,1)
    glTranslatef(1,1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,1)
    glTranslatef(2,1,1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-2,1,1)
    glRotate(-150, 1, 1, 0)
    glTranslatef(22, -15, -faixaZ1)

    glTranslatef(-18, -2, faixaZ3) 
    glRotate(37, 1, 1, 0)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(1,1,1)
    glTranslatef(1,1,1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,-1)
    glTranslatef(1,-1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,1,1)
    glTranslatef(1,1,-1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-1,-1,1)
    glTranslatef(2,1,1)
    gluSphere(gluNewQuadric(), 2, 8, 8)
    glTranslatef(-2,1,1)
    glRotate(-37, 1, 1, 0)
    glTranslatef(18, 2, -faixaZ3)
    
    glRotatef(-px, 1, 0, 0)
    glRotatef(-py, 0, 1, 0)
    glRotatef(-pz, 0, 0, 1)
    
    glFlush()

def buttons(key,x,y):
    global px, py, pz
    if key == GLUT_KEY_LEFT:
        py -= 3
        
    elif key == GLUT_KEY_RIGHT:
        py += 3
        
    elif key == GLUT_KEY_UP:
        px += 3
        
    elif key == GLUT_KEY_DOWN:
        px -= 3
    
    elif key == GLUT_KEY_PAGE_UP:
        pz -= 3
    
    elif key == GLUT_KEY_PAGE_DOWN:
        pz += 3
    
    elif key == GLUT_KEY_HOME: # # Voltar para a vista frental (tecla Home)
        px = 0
        py = 0
        pz = 0
        
    elif key == GLUT_KEY_END: # Vista em perspectiva (tecla End)
        px = 6
        py = -30
        pz = 0
        
    glutPostRedisplay()
    
def movimento(key,x,y):
    global direcao, ty, fe, fd, speed, faixaZ1, faixaZ2, faixaZ3, faixaZ4, faixaZ5
    
    if (key == b'w') or (key == b'W'):
        if (fd == 20 and fe == 20):
            fe = 0
            fd = 0
        else:
            fd = -20
            fe = -20

    elif (key == b's') or (key == b'S'):
        if (fd == -20 and fe == -20):
            fe = 0
            fd = 0
        else:
            fd = 20
            fe = 20

    elif (key == b'a') or (key == b'A'):
        if (fd == 20):
            fe = 0
            fd = 0
        else:
            ty -= 6
            fe = 20
            fd = -20
    
    elif (key == b'd') or (key == b'D'):
        if (fe == 20):
            fe = 0
            fd = 0
        else:
            ty += 6
            fe = -20
            fd = 20

    elif (key == b'q') or (key == b'Q'):
        if direcao < 10:
            direcao += 3
    
    elif (key == b'e') or (key == b'E'):
        if direcao > -10:
            direcao -= 3
    
    elif (key == b'g') or (key == b'G'):
        if speed > 5:
            speed -= 2

    elif (key == b'b') or (key == b'B'):
        if speed < 30:
            speed += 2
    
    glutPostRedisplay()

def update(value):
    global faixaZ1, faixaZ2, faixaZ3, faixaZ4, faixaZ5
    faixaZ1 -= 1
    faixaZ2 -= 1
    faixaZ3 -= 1
    faixaZ4 -= 1
    faixaZ5 -= 1
    
    if faixaZ1 < -50:
        faixaZ1 = 50
    if faixaZ2 < -50:
        faixaZ2 = 50
    if faixaZ3 < -50:
        faixaZ3 = 50
    if faixaZ4 < -50:
        faixaZ4 = 50
    if faixaZ5 < -50:
        faixaZ5 = 50

    glutPostRedisplay()
    glutTimerFunc(speed, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1920,1080)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("LockHead F117 Nighthawk")
    glutTimerFunc(speed, update, 0)
    glClearColor(0.35, 0.35, 1, 1) #backgroundcolor
    glShadeModel(GL_SMOOTH)
    glFrontFace(GL_CCW)
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutSpecialFunc(buttons)
    glutKeyboardFunc(movimento)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50,(1000/650),1,200)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(12.25,-12.25,40,
                0,0,0,-0.07,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(30,1,1,0)
    drawC()
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()