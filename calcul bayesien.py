from mpl_toolkits import mplot3d
import random
import itertools 
import time

import math as m
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.ttk import Progressbar
from tkinter.ttk import *

from fpdf import FPDF
from matplotlib.backends.backend_pdf import PdfPages

#DIM 1 POUR UNE SEULE VARIABLE
'''
echant=1000
pf=[5,15]

def F(p):
	occ1 = pf[0]
	occ2 = pf[1]
	N=occ1+occ2
	return (p**occ1)*((1-p)**occ2)*m.comb(N,occ1)

x=[i/echant for i in range(1001)]
y=[F(i) for i in x]

print (y)

plt.plot(x,y)
plt.show()

'''
#DIM 2 POUR 2 VARIABLE (NAPPE)
def F(p1,p2):
	occ1 = pf[0]
	occ2 = pf[1]
	occ3 = pf[2]
	N=occ1+occ2+occ3
	return (p1**occ1)*((p2)**occ2)*((1-p1-p2)**occ3)*m.factorial(N)/(m.factorial(occ1)*m.factorial(occ2)*m.factorial(occ3))


echant=100
pf=[1,4,6]

Z=[[0 for i in range(echant+1)] for i in range(echant+1)]


#le boucle qui crée la matrice Z par une similuation d'une statique de loi multinomiale à trois variable
for i in range (0,echant+1):
	for j in range(0,echant+1-i):
		Z[i][j]=F(i/echant,j/echant)
	for k in range(echant+1-i,echant+1):
		Z[i][k]=0
		
	#verifier la progression du programme
	print (m.trunc(((i/echant)*100)))

print(Z)	

#def des axes du meshgrid
ax = plt.axes(projection='3d')
X, Y = np.meshgrid( [j/echant for j in range (0,echant+1)],[i/echant for i in range (0,echant+1)] )
Z=np.array(Z)

# Data for three-dimensional scattered points
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')

plt.show()

k=input('zrg')









