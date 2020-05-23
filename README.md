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
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image011.png)

Un individuo enfermo al cabo del tiempo que dura la enfermedad se cura o muere. Si se cura adquiere inmunidad y no se vuelve a contagiar.

![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image013.png)
La probabilidad de que se muera estando enfermo se configura con la barra deslizable. Si es 0,5% de 20 individuo que se enferman 1 muere.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image015.png)
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image017.png)


Un individuo muerto queda fijo en el lugar donde murió y no contagia a nadie mas.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image019.png)

Todos los individuos sanos son susceptibles de contraer la enfermedad. Tanto los individuos sanos como los enfermos caminan por el tablero deslizándose aleatoriamente a una posición vecina con cada paso del tiempo.

![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image021.png)

Si un individuo no respeta la distancia social con un individuo enfermo se puede enfermar. La distancia social se configura con la barra deslizable que dice distancia máxima de contagio. Si la distancia social es 1 todos los individuos que se encuentran en casilleros adyacentes de un individuo enfermo se pueden contagiar.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image023.png)

La probabilidad de que alguien se contagie si no se respeta la distancia social se configura con la barra deslizable que dice probabilidad de contagio. Si la probabilidad de contagio es 100% nos dice que siempre que alguien no respete la distancia social con alguien enfermo se contagia.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image025.png)
Un individuo no puede contagiar a una persona que esta inmunizado por haber pasado por la enfermedad. Tampoco puede contagiar a alguien que se encuentra a una distancia mayor que la distancia social. Mientras mayor sea la duración de la enfermedad mayor sera la cantidad de personas que pueda contagiar. La probabilidad de contagio de alguien que no respeta la distancia social se puede configurar. Un 100% significa que siempre que no se respeta la distancia social se va a contagiar.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image027.png)

¿Como se calcula R? Si hoy se curaron o murieron n individuos y esos individuos en total contagiaron a k individuos, el r del día de hoy lo calculo como n/k y lo pondero con el r histórico, el r de ayer, dando mas peso al r actual que al r ayer. Por ejemplo, si hoy se curo un individuo y en el transcurso de la enfermedad ese individuo contagio a 2 individuo, y también hoy murió un individuo que en el transcurro de la enfermedad no contagio a nadie, en este caso el r actual seria la cantidad de contagios de la persona que se curo mas los contagios de la persona que murió dividido 2, el individuo que se curo mas el individuo que murio. Este R, el R actual, es ponderado con el R del dia anterior, el R histórico, esto es, lo pondero con la cantidad de contagios que produjeron las personas que se curaron, o murieron, ayer. Por ejemplo si ayer se curaron 2 personas que contagiaron a 4 y murió una persona que contagio a 2, el r del día anterior seria 2.
![Crop options](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/blob/master/readme/image029.png)

***Aplicación web online: 
https://simulator-coronavirus-covid-19.herokuapp.com/***



![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)


![](https://github.com/marcoscravero2175/simulator-coronavirus-covid-19/readme/image001.png)
dddd
https://github.com/pandao/editor.md/tree/master/images

.. image:: https://api.travis-ci.org/projectmesa/mesa.svg?branch=master
        :target: https://travis-ci.org/projectmesa/mesa

.. image:: https://codecov.io/gh/projectmesa/mesa/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/projectmesa/mesa

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

`Mesa`_ is an Apache2 licensed agent-based modeling (or ABM) framework in Python.

It allows users to quickly create agent-based models using built-in core components (such as spatial grids and agent schedulers) or customized implementations; visualize them using a browser-based interface; and analyze their results using Python's data analysis tools. Its goal is to be the Python 3-based alternative to NetLogo, Repast, or MASON.


.. image:: https://github.com/projectmesa/mesa/blob/master/docs/images/Mesa_Screenshot.png
   :width: 100%
   :scale: 100%
   :alt: A screenshot of the Schelling Model in Mesa

*Above: A Mesa implementation of the Schelling segregation model,
being visualized in a browser window and analyzed in a Jupyter
notebook.*

.. _`Mesa` : https://github.com/projectmesa/mesa/


Features
------------

* Modular components
* Browser-based visualization
* Built-in tools for analysis
* Example model library

Using Mesa
------------

Getting started quickly:

.. code-block:: bash

    $ pip install mesa

You can also use `pip` to install the github version:

.. code-block:: bash

    $ pip install -e git+https://github.com/projectmesa/mesa#egg=mesa

Take a look at the `examples <https://github.com/projectmesa/mesa/tree/master/examples>`_ folder for sample models demonstrating Mesa features.

For more help on using Mesa, check out the following resources:

* `Intro to Mesa Tutorial`_
* `Docs`_
* `Email list for users`_
* `PyPI`_

.. _`Intro to Mesa Tutorial` : http://mesa.readthedocs.org/en/master/tutorials/intro_tutorial.html
.. _`Docs` : http://mesa.readthedocs.org/en/master/
.. _`Email list for users` : https://groups.google.com/d/forum/projectmesa
.. _`PyPI` : https://pypi.python.org/pypi/Mesa/

Running Mesa in Docker
------------------------

You can run Mesa in a Docker container in a few ways.

If you are a Mesa developer, first `install docker-compose <https://docs.docker.com/compose/install/>`_ and then run:

.. code-block:: bash

    $ docker-compose build --pull
    ...
    $ docker-compose up -d dev # start the docker container
    $ docker-compose exec dev bash # enter the docker container that has your current version of Mesa installed at /opt/mesa
    $ mesa runserver examples/Schelling # or any other example model in examples


The docker-compose file does two important things:

* It binds the docker container's port 8521 to your host system's port 8521 so you can interact with the running model as usual by visiting localhost:8521 on your browser
* It mounts the mesa root directory (relative to the docker-compose.yml file) into /opt/mesa and runs pip install -e on that directory so your changes to mesa should be reflected in the running container.


If you are a model developer that wants to run Mesa on a model (assuming you are currently in your top-level model
directory with the run.py file):

.. code-block:: bash

    $ docker run --rm -it -p127.0.0.1:8521:8521 -v${PWD}:/code comses/mesa:dev mesa runserver /code

Contributing back to Mesa
----------------------------

If you run into an issue, please file a `ticket`_ for us to discuss. If possible, follow up with a pull request.

If you would like to add a feature, please reach out via `ticket`_ or the `dev email list`_ for discussion. A feature is most likely to be added if you build it!

* `Contributors guide`_
* `Github`_

.. _`ticket` : https://github.com/projectmesa/mesa/issues
.. _`dev email list` : https://groups.google.com/forum/#!forum/projectmesa-dev
.. _`Contributors guide` : https://github.com/projectmesa/mesa/blob/master/CONTRIBUTING.rst
.. _`Github` : https://github.com/projectmesa/mesa/
