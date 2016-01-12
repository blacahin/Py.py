#testes para evolução de um gráfico

import matplotlib.pyplot as p

#Criar uma lista com os meses respetivos para os periodos (1971-200)
meses = list(range(1,13))

#Listas das estações meteorológicas em Análise e valores (Temperatura Máxima)
Angra_do_Heroismo1 = [20.2, 20.2, 20.6, 21.6, 24.6, 25.7, 29.1, 29.2, 28.7, 25.9, 25, 21.1]
Aveiro1 = [21.5, 25, 28, 32.5, 33.5, 36.5, 39, 38, 34, 34, 26, 24]
Beja1 = [22, 24.5, 30, 31.5, 36.6, 43.3, 45.2, 41.5, 42, 33.8, 28.1, 22]
Braganca1 = [17.4,20.4, 25.7, 28.1, 31, 36.4, 38.8, 38.4, 37.7, 30.6, 22.4, 18.8]
Braga1 = [22.4, 23.5, 28, 31, 34.4, 38.5, 38.5, 39.3, 38.5, 33.3, 26.7, 24.1]
Castelo_Branco1 = [25.4, 22.3, 27, 29.9, 32.8,38.5,40.6,40.3,40.2,31.6,24.4,20.3]
Coimbra1 = [23, 25.5, 29.5, 32.5, 35, 41.6, 40.2, 40, 40, 34.6, 27.6, 25.2]
Evora1 = [21, 24.2, 27.4, 30.5, 34.2, 41, 42, 39.6, 39.7, 32.4, 26.6,21.5]
Faro1 = [21.2, 25.6, 28.9, 30.1, 33.8, 37.1, 39.8, 39.4, 37.4, 33.3, 28.8, 25.4]
Funchal1 = [25.5, 26.6, 30.1, 30.2, 33, 34.7, 29.6, 38.5, 38.4, 34.1, 30, 25.6]
Guarda1 = [15.2, 17.6, 21.9, 24.5, 27.7, 33.4, 38.3, 34.6, 36, 27, 21.3, 17.1]
Lisboa1 = [20.6, 24.8, 28.3, 29.4, 35, 41.5, 40.6, 37.9, 37.1, 32.6, 25.6, 23.2]
Ponta_Delgada1 = [19.8, 20.4, 21.9, 21.3, 24, 25.6, 27.8, 28.8, 28.6, 26.2,24.6, 21.6]
Portalegre1 = [20.4, 22.5, 25.5, 29.6, 32.3, 39.4, 40.4, 39.1, 39.5, 31, 25.7, 23.2]
Porto1 = [22.3, 23.2, 28, 28.9, 34.1, 38.7, 38.3, 37.6, 39.6, 32.2, 26.3, 24.8]
Santa_Cruz1 = [20.2, 20.7, 21.8,22.5, 24.8, 26.5, 29.8, 30, 29.4, 27.4, 25, 21.9]
Santarem1 = [20.6, 24.8, 29, 31.6, 36, 43.5, 43, 40.5, 40.2, 33.6, 26.5, 23]
Setubal1 = [21, 25, 29, 32, 36, 41.9, 43.5, 40, 41.3, 33.5, 28.8, 22.9]
Vila_Real1 = [17.8, 22, 26.1, 28.1,32.2, 37.5, 39.8, 39, 38.3, 30.9, 22.3, 19.5]
Viana_do_Castelo1 = [23, 25, 28.6, 31.6, 34.3, 38.6, 38, 38.2, 36.4, 32.8, 26.2, 24.6]
Viseu1 = [20, 22.5, 27.4, 30.3,33, 39, 40.5, 40.4, 39.6, 31.2, 24.6, 22.5]

#Valores Médios da temperatura
Angra_do_Heroismo2 = [13.7, 13.5, 14, 14.6, 16, 18.2, 20.7, 21.8, 21, 18.7, 16.5, 14.8]
Aveiro2 = [10.2, 11.3, 13.2, 14, 16.1, 18.7, 20.1, 20.2, 19.3, 16.7, 13.7, 11.5]
Beja2 = [9.6, 10.7, 12.6, 14, 16.9, 21, 24.2, 24.3, 22.2, 17.8, 13.5, 10.8]
Braganca2 = [4.4, 6.2, 8.6, 10.2, 13.4, 17.9, 21.3, 21.1, 18.1, 12.8, 8.2, 5.5]
Braga2 = [8.7, 9.8, 11.5, 12.6, 15, 18.6, 20.9, 20.6, 19, 15.3,11.8,10]
Castelo_Branco2 = [7.9, 9.6, 12.7, 13.1, 16.8, 21, 25, 24.4, 21.3, 16.3, 11.7,9]
Coimbra2 = [9.6, 10.9, 12.6, 13.9, 16.2, 19.4, 21.6, 21.5,20.2, 16.6, 12.9, 10.8]
Evora2 = [9.3, 10.4, 12.4, 13.5, 16.2, 20.2, 23.2, 23.3, 21.4, 17, 13, 10.4]
Faro2 = [11.7, 12.5, 13.9, 15.2, 17.6, 20.7, 23.6, 23.7, 22, 18.7, 15.4, 13.2]
Funchal2 = [16.2, 16.1, 16.6, 16.9, 17.9, 19.7, 21.4, 22.6, 22.6, 21.2, 19.2, 17.4]
Guarda2 = [4, 5.2,7.1, 8, 11.6, 15.9, 19.1, 19.4, 16.4, 11.3, 7.5, 4.9]
Lisboa2 = [11.3, 12.6, 14.3, 15.3, 17.3, 20.3, 22.7, 23, 21.7, 18.4, 14.8, 12.4]
Ponta_Delgada2 = [14.1, 13.7, 14.2, 14.7, 15.9, 18.1, 20.4, 21.7, 21, 18.9, 16.8, 15.1]
Portalegre2 = [8.5, 9.4, 11.5, 12.3, 15.3, 19.9, 23.5, 23.5, 21.2, 16.2, 12.1,9.5]
Porto2 = [9.3, 10.4, 11.9, 13.2, 15.2, 18.3, 20.2, 20.1, 18.9, 16, 12.6, 10.6]
Santa_Cruz2 = [14, 13.6, 14.3, 15, 16.6, 18.9, 21.3, 22.3, 21.1, 18.8, 16.7, 15.1]
Santarem2 = [9.6, 11, 12.9, 14.1, 16.5, 20, 22.6, 22.7, 21, 17.1, 13.2, 10.8]
Setubal2 = [9.9, 11.3, 13, 14.4, 16.8, 20, 22.6, 22.7, 20.9, 17.4, 13.7, 11.3]
Vila_Real2 = [5.8, 7.7, 9.5, 11.3, 14.1, 18.6, 21.5, 21.3, 19.4, 14, 9.5, 7]
Viana_do_Castelo2 = [9.5, 10.5, 12, 13.4, 15.4, 18.6, 20.5, 20.3, 18.9, 15.7, 12.5, 10.7]
Viseu2 = [6.9, 8.4, 10.3, 11.5, 14.3, 18.4, 21.4, 21.1, 18.8, 14.2, 10.2, 8.1]

#Valores Minimos da temperatura
Angra_do_Heroismo3 = [3.7, 4.2, 3.8, 5.7, 6.4, 10.2, 12.5, 13.2, 13.3, 10.2, 7.6, 5.5]
Aveiro3 = [-3, -2.5, 0, 1.5, 5.5, 8.5, 11.4, 10, 8.5, 3.5, 1, -3]
Beja3 = [-3, -3.2, -3.2, 0.3, 3.6, 6.2, 8.7, 9, 6.4, 3.2, -0.5, -2]
Braganca3 = [-11.4, -11.6, -6, -5.1, -1.4, 3.4, 4.4, 4.4, 1.4, -3.8, -5.3, -7.1]
Braga3 = [-6.3, -4.5, -2.6, -1.3, -0.5, 3.3, 6.7, 6.5, 2.6, -1, -3.2, -3.2]
Castelo_Branco3 = [-3.9, -1.5, -3.4, 0.4, 2.8, 7.9, 8.9, 10, 6.2, 3.4, -2.4, -2.8]
Coimbra3 = [-4.9, -4, -3.3, -1.5, 2, 4.1, 6.8, 6, 2, -2.6, -3.1, -2.8]
Evora3 = [-2.9, -1.4, -1.8, 2, 4.9, 6.7, 9.8, 11, 7.6, 4, 1.4, -1.5]
Faro3 = [-1.2, -1.2, 1.8, 3.6, 5.6, 7.4, 10.5, 11.6, 9.9, 6, 2.2, -1.4]
Funchal3 = [8.8, 7.4, 7.7, 9.3, 9.7, 12.8, 14.6, 16.3, 14.9, 10.3, 10.8, 8]
Guarda3 = [-10.8, -6.2, -8.8, -4.5, -1.8, 1.2, 4.4, 4.9, 1.8, -0.6, -7.5, -6.7]
Lisboa3 = [0.4, 1.2, 2.9, 5.5, 6.9, 10.3, 13.1, 13.8, 10.7, 8, 3.9, 2.4]
Ponta_Delgada3 = [4.4, 3.5, 4.2, 5.3, 6.6, 8.3, 11.9, 11.9, 9.6, 8.6, 7.4, 5.7]
Portalegre3 = [-4.5, -3.7, -2.8, -0.2, 2.1, 5, 8.2, 8.6, 6, 3.5, 1, -1.1]
Porto3 = [-3.3, -2.8, -1.3, 0.1, 2.6, 5.6, 9.5, 8, 5.5, 1.4, -0.3, -1.2]
Santa_Cruz3 = [2.1, 4, 3.4, 5, 7.2, 9.2, 11.4, 12.6, 11.1, 9.1, 6.5, 4]
Santarem3 = [-4.4, -3.5, -3.5, 0, 4, 7, 9, 8.5, 7, -0.5, -3.7, -3.2]
Setubal3 = [-5.1, -4.6, -2.5, -0.7, 3, 5.4, 7.9, 8.5, 6.8, 2, -2.4, -4.1]
Vila_Real3 = [-6.5, -6.3, -3.6, -2, 0, 4, 7.5, 6.2, 2.4, -0.8, -3.4, -5]
Viana_do_Castelo3 = [-3.9, -2.9, -1.1, -0.6, 0.8, 4.7, 8.7, 8, 3.8, 2.4, -1.9, -4]
Viseu3 = [-6.6, -7.3, -5.4, -3.8, -0.5, 2, 0.6, 6, 2, -2.8, -3.6, -5]

#Fundo
fig = p.figure()
rect = fig.patch
rect.set_facecolor('white')

#Grafico 1.1
ax1 = fig.add_subplot(3,1,1, axisbg='white')
ax1.plot(meses,Angra_do_Heroismo1,'r', linewidth=4.0, linestyle='-')
ax1 = fig.add_subplot(3,1,1, axisbg='white')
ax1.plot(meses,Angra_do_Heroismo2,'b', linewidth=4.0, linestyle='-')
ax1 = fig.add_subplot(3,1,1, axisbg='white')
ax1.plot(meses,Angra_do_Heroismo3,'c', linewidth=4.0, linestyle='-')
ax1.set_title("Angra do Heroísmo")

#Grafico 1.2
ax2 = fig.add_subplot(3,1,2, axisbg='white')
ax2.plot(meses,Aveiro1,'r', linewidth=4.0, linestyle='-')
ax2 = fig.add_subplot(3,1,2, axisbg='white')
ax2.plot(meses,Aveiro2,'b', linewidth=4.0, linestyle='-')
ax2 = fig.add_subplot(3,1,2, axisbg='white')
ax2.plot(meses,Aveiro3,'c', linewidth=4.0, linestyle='-')
ax2.set_title("Aveiro")

p.show()
