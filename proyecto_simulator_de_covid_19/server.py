from framework_mesa.visualization.ModularVisualization import ModularServer
from framework_mesa.visualization.UserParam import UserSettableParameter
from framework_mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from framework_mesa.visualization.UserParam import UserSettableParameter
from framework_mesa.visualization.ModularVisualization import VisualizationElement

from proyecto_simulator_de_covid_19.individuos import Individuos
from proyecto_simulator_de_covid_19.model import Ambiente

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

import random

import numpy as np

#import tornado.web.RequestHandler

from framework_mesa.visualization.TextVisualization import (
    TextData, TextGrid, TextVisualization
)

class HistogramModule(VisualizationElement):
    #package_includes = ["<script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.4/Chart.min.js'></script>"]
    #package_includes = "<script src='Framework_Mesa1/visualization/templates/js/Chart.bundle.min.js'></script>"
    #package_includes  = ["Framework_Mesa/visualization/templates/js/Chart.bundle.min.js"]

    local_includes = ["framework_mesa/visualization/templates/js/HistogramModule9.js"]

    def __init__(self, bins, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.bins = bins
        new_element = "new HistogramModule({}, {}, {})"
        new_element = new_element.format(bins,
                                         canvas_width,
                                         canvas_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        #wealth_vals = [agent.wealth for agent in model.schedule.agents]
        #hist = np.histogram(wealth_vals, bins=self.bins)[0]
        #return [int(x) for x in hist]    

        porcentajeDeInfectados = model.schedule.PorcentajeDeIndividuosInfectados()

        porcentajeDeSusceptibles = model.schedule.PorcentajeDeIndividuosSusceptibles()

        porcentajeDeInmunizados = model.schedule.PorcentajeDeIndividuosInmunizados()

        porcentajeDeMuertos = model.schedule.PorcentajeDeIndividuosMuertos()

        return [porcentajeDeSusceptibles, porcentajeDeInfectados, porcentajeDeInmunizados, porcentajeDeMuertos]

def personalizacionDelAmbiente(individuo):
    if individuo is None:
        return

    portrayal = {}
        
    if individuo.EsSusceptible():
        portrayal["Shape"] = "proyecto_simulator_de_covid_19/resources/susceptible1.png"
        # https://icons8.com/web-app/36821/German-Shepherd

        portrayal["Id"] = individuo.unique_id

        portrayal["EsSusceptible"] = str(individuo.EsSusceptible())
        portrayal["EstaInmunizado"] = str(individuo.EstaInmunizado())
        portrayal["EstaInfectado"] = str(individuo.EstaInfectado())

        portrayal["HaceMasDeUnDiaQueEstaInfectado"] = individuo.HaceMasDeUnDiaQueEstaInfectado()

        if  (individuo.EstaInfectado() == True):
                cantidad_dias_infectado = individuo.CantidadDeDiasQueHaceQueEstaEnfermo() + 1
        else:
                cantidad_dias_infectado = 0

        portrayal["Cantidad_dias_infectado"] = cantidad_dias_infectado
        portrayal["Individuos_que_contagio"] = individuo.VerCantidadDeIndividuosQueContagio()

        portrayal["Layer"] = 1
        portrayal["text_color"] = "#FA5882"

    if individuo.EstaInfectado():
        portrayal["Shape"] = "proyecto_simulator_de_covid_19/resources/infectado.png"
        # https://icons8.com/web-app/36821/German-Shepherd

        portrayal["Id"] = individuo.unique_id

        portrayal["EsSusceptible"] = str(individuo.EsSusceptible())
        portrayal["EstaInmunizado"] = str(individuo.EstaInmunizado())
        portrayal["EstaInfectado"] = str(individuo.EstaInfectado())

        portrayal["HaceMasDeUnDiaQueEstaInfectado"] = individuo.HaceMasDeUnDiaQueEstaInfectado()
        if  (individuo.EstaInfectado() == True):
                cantidad_dias_infectado = individuo.CantidadDeDiasQueHaceQueEstaEnfermo() + 1
        else:
                cantidad_dias_infectado = 0

        portrayal["Cantidad_dias_infectado"] = cantidad_dias_infectado
        portrayal["Individuos_que_contagio"] = individuo.VerCantidadDeIndividuosQueContagio()

        portrayal["Layer"] = 1
        portrayal["text_color"] = "#8A0829"

    if individuo.EstaInmunizado():
        portrayal["Shape"] = "proyecto_simulator_de_covid_19/resources/inmunizado.png"
        # https://icons8.com/web-app/36821/German-Shepherd

        portrayal["Id"] = individuo.unique_id

        portrayal["EsSusceptible"] = str(individuo.EsSusceptible())
        portrayal["EstaInmunizado"] = str(individuo.EstaInmunizado())
        portrayal["EstaInfectado"] = str(individuo.EstaInfectado())

        portrayal["HaceMasDeUnDiaQueEstaInfectado"] = individuo.HaceMasDeUnDiaQueEstaInfectado()
        if  (individuo.EstaInfectado() == True):
                cantidad_dias_infectado = individuo.CantidadDeDiasQueHaceQueEstaEnfermo() + 1
        else:
                cantidad_dias_infectado = 0

        portrayal["Cantidad_dias_infectado"] = cantidad_dias_infectado
        portrayal["Individuos_que_contagio"] = individuo.VerCantidadDeIndividuosQueContagio()

        portrayal["Layer"] = 1
        portrayal["text_color"] = "#FA5882"


    if individuo.EstaMuerto():
        portrayal["Shape"] = "proyecto_simulator_de_covid_19/resources/muerto.png"
        # https://icons8.com/web-app/36821/German-Shepherd

        portrayal["Id"] = individuo.unique_id

        portrayal["EsSusceptible"] = str(individuo.EsSusceptible())
        portrayal["EstaInmunizado"] = str(individuo.EstaInmunizado())
        portrayal["EstaInfectado"] = str(individuo.EstaInfectado())

        portrayal["HaceMasDeUnDiaQueEstaInfectado"] = individuo.HaceMasDeUnDiaQueEstaInfectado()
        if  (individuo.EstaInfectado() == True):
                cantidad_dias_infectado = individuo.CantidadDeDiasQueHaceQueEstaEnfermo() + 1
        else:
                cantidad_dias_infectado = 0

        portrayal["Cantidad_dias_infectado"] = cantidad_dias_infectado
        portrayal["Individuos_que_contagio"] = individuo.VerCantidadDeIndividuosQueContagio()

        portrayal["Layer"] = 1
        portrayal["text_color"] = "#FA5882"


    return portrayal

canvas_element = CanvasGrid(personalizacionDelAmbiente, 20, 20, 500, 500)
chart_element = ChartModule([{"Label": "R", "Color": "#006600"},
                             {"Label": "Susceptibles", "Color": "#FFC533"},
                             {"Label": "Infectados", "Color": "#FFC4D1"},
                             {"Label": "Inmunizados", "Color": "#00CCFF"},
                             {"Label": "Muertos", "Color": "#FF3300"}])



poblacionInicial = UserSettableParameter('slider', 'Poblacion', 100, 0, 100) 
numeroDeInfectadosInicial = UserSettableParameter('slider', 'Numero inicial de individuos infectados', 2, 0, 100) 
distanciaDeContagioInicial = UserSettableParameter('slider', 'Distancia maxima de contagio', 1, 0, 20)
duracionDeEnfermedadInicial = UserSettableParameter('slider', 'Cantidad de dias de que un individuo infectado puede contagiar', 7, 0, 20)
probabilidadDeContagiarseInicial = UserSettableParameter('slider', 'Probabilidad de contagiarse estando dentro de la distancia maxima de contagio.', 100, 0, 100) 
probabilidadDeQueMueraInicial = UserSettableParameter('slider', 'Probabilidad de que un individuo infectado muera', 5, 0, 100)

histogram = HistogramModule(list(range(10)), 200, 500)

server = ModularServer(Ambiente, [canvas_element, chart_element, histogram], "Machos galanteadores y fieles. Hembras faciles y esquivas", 
		{"poblacionInicial": poblacionInicial,
		"numeroDeInfectadosInicial": numeroDeInfectadosInicial,
		"distanciaDeContagioInicial": distanciaDeContagioInicial,
		"duracionDeEnfermedadInicial": duracionDeEnfermedadInicial,
		"probabilidadDeContagiarseInicial": probabilidadDeContagiarseInicial,
		"probabilidadDeQueMueraInicial": probabilidadDeQueMueraInicial})


#server.port = 8257
server.port = int(os.environ.get("PORT", 5008))

server.launch()
