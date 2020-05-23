Simulador de juguete de Covid-19
=========================================

Parámetros de la simulación: población, individuos infectados, distancia social, cantidad de días que un individuo infectado puede contagiar, probabilidad de un individuo se contagie estando dentro de la distancia social, probabilidad de que un individuo infectado muera.

Aplicación web online: 
https://simulator-coronavirus-covid-19.herokuapp.com/


![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image001.png)
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image003.png)





Se acaba de contagiar el individuo con el numero único de identificación 77. Como se puede leer en su ficha hace menos de un día que se contagio, todavía el no infecto a nadie mas.

![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image005.png)


El individuo con numero único de identificación 99 se infecto hace 2 días. A su vez el infecto a 2 personas.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image007.png)

Mientras esta enfermo un individuo puede contagiar. La duración de la enfermedad se configura con la barra deslizable.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image009.png)
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image010.png)

Un individuo enfermo al cabo del tiempo que dura la enfermedad se cura o muere. Si se cura adquiere inmunidad y no se vuelve a contagiar.

![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image011.png)
La probabilidad de que se muera estando enfermo se configura con la barra deslizable. Si es 0,5% de 20 individuo que se enferman 1 muere.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image012.png)
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image013.png)


Un individuo muerto queda fijo en el lugar donde murió y no contagia a nadie mas.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image014.png)

Todos los individuos sanos son susceptibles de contraer la enfermedad. Tanto los individuos sanos como los enfermos caminan por el tablero deslizándose aleatoriamente a una posición vecina con cada paso del tiempo.

![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image015.png)

Si un individuo no respeta la distancia social con un individuo enfermo se puede enfermar. La distancia social se configura con la barra deslizable que dice distancia máxima de contagio. Si la distancia social es 1 todos los individuos que se encuentran en casilleros adyacentes de un individuo enfermo se pueden contagiar.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image016.png)

La probabilidad de que alguien se contagie si no se respeta la distancia social se configura con la barra deslizable que dice probabilidad de contagio. Si la probabilidad de contagio es 100% nos dice que siempre que alguien no respete la distancia social con alguien enfermo se contagia.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image018.png)
Un individuo no puede contagiar a una persona que esta inmunizado por haber pasado por la enfermedad. Tampoco puede contagiar a alguien que se encuentra a una distancia mayor que la distancia social. Mientras mayor sea la duración de la enfermedad mayor sera la cantidad de personas que pueda contagiar. La probabilidad de contagio de alguien que no respeta la distancia social se puede configurar. Un 100% significa que siempre que no se respeta la distancia social se va a contagiar.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image020.png)

¿Como se calcula R? Si hoy se curaron o murieron n individuos y esos individuos en total contagiaron a k individuos, el r del día de hoy lo calculo como n/k y lo pondero con el r histórico, el r de ayer, dando mas peso al r actual que al r ayer. Por ejemplo, si hoy se curo un individuo y en el transcurso de la enfermedad ese individuo contagio a 2 individuo, y también hoy murió un individuo que en el transcurro de la enfermedad no contagio a nadie, en este caso el r actual seria la cantidad de contagios de la persona que se curo mas los contagios de la persona que murió dividido 2, el individuo que se curo mas el individuo que murio. Este R, el R actual, es ponderado con el R del dia anterior, el R histórico, esto es, lo pondero con la cantidad de contagios que produjeron las personas que se curaron, o murieron, ayer. Por ejemplo si ayer se curaron 2 personas que contagiaron a 4 y murió una persona que contagio a 2, el r del día anterior seria 2.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image022.png)

***Aplicación web online: 
https://simulator-coronavirus-covid-19.herokuapp.com/***


