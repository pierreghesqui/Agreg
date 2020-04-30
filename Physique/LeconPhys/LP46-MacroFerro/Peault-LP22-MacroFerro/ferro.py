import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#read csv data
a, EAO, b, Epince, c, d, e, f = np.genfromtxt('peault_ferro.txt', delimiter=';', unpack=True)


P=0.3 #Périmètre du noyau de fer en m (pas pu faire de mesure donc j'estime)
B=0.2/250/(0.0016)*EAO
H=5000*Epince/(P)
print(B)

plt.figure()
plt.plot(H,B, 'k,')
plt.xlabel('Excitation H')
plt.ylabel('Champ Magnétique B')
plt.title('5 périodes')


plt.figure()
plt.plot(H[2022:4021], B[2022:4021], 'g,')
plt.plot(H[4022:6022], B[4022:6022], 'r,')
plt.title('Vert:Aller, Rouge:Retour. 1 période')

integaller = 0.0
integretour = 0.0
for i in range(2022,4021):

    integaller = integaller + (B[i] + B[i+1]) / 2 * (H[i+1] - H[i])

for i in range(4022,6021):
    integretour = integretour + (B[i] + B[i+1]) / 2 * (H[i+1] - H[i])

Aire=integretour-integaller
print('Aire du cycle hystérésis=',-Aire, 'W')


plt.show()
