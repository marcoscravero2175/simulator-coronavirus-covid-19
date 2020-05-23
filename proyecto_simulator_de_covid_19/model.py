from framework_mesa import Model
from framework_mesa.space import MultiGrid
from framework_mesa.datacollection import DataCollector

from proyecto_simulator_de_covid_19.individuos import Individuos
from proyecto_simulator_de_covid_19.schedule import RandomActivationByBreed


import random

class Ambiente(Model):
	height = 20
	width = 20

	poblacionInicial = 40 
	numeroDeInfectadosInicial = 2
	distanciaDeContagioInicial = 1
	probabilidadDeContagiarseInicial = 100
	duracionDeEnfermedadInicial = 1
	probabilidadDeQueMueraInicial = 1
	probabilidadDeQueMueraPorcentaje = 1

	epoca = 1
	
	description = 'Un modelo de juegete del covid-19.'
	
	def __init__(self, 
		alto = 20,
		ancho = 20,

		poblacionInicial = 40, 

		numeroDeInfectadosInicial = 2,
		distanciaDeContagioInicial = 1,
		duracionDeEnfermedadInicial = 1,
		probabilidadDeContagiarseInicial = 100,
		probabilidadDeQueMueraInicial = 1

		):
		
		super().__init__()
		self.epoca = 1
		
		self.alto = alto
		self.ancho = ancho
		
		self.poblacionInicial = poblacionInicial
		self.numeroDeInfectadosInicial = numeroDeInfectadosInicial
		self.distanciaDeContagioInicial = distanciaDeContagioInicial
		self.duracionDeEnfermedadInicial = duracionDeEnfermedadInicial
		self.probabilidadDeContagiarseInicial = probabilidadDeContagiarseInicial
		self.probabilidadDeQueMueraInicial = probabilidadDeQueMueraInicial
		
		self.schedule = RandomActivationByBreed(self)
		self.grid = MultiGrid(20, 20, torus = False)
		
		self.grid = MultiGrid(self.alto, self.ancho, torus=False)
		self.datacollector = DataCollector(
			{"Poblacion": lambda m: m.schedule.CantidadDeIndividuos1(),
			"R": lambda m: m.schedule.VerPromedioR(),
			"Susceptibles": lambda m: m.schedule.CantidadDeIndividuosSusceptibles(),
			"Infectados": lambda m: m.schedule.CantidadDeIndividuosInfectados(),
			"Inmunizados": lambda m: m.schedule.CantidadDeIndividuosInmunizados(),
			"Muertos": lambda m: m.schedule.CantidadDeIndividuosMuertos()
			})

		self.probabilidadDeQueMueraPorcentaje = probabilidadDeQueMueraInicial / 100.00
		
		i = 0
		while i < self.poblacionInicial -  self.numeroDeInfectadosInicial:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			pos = (x, y)
			
			id = self.next_id()

			estaInfectado = False
			cantidadDeDiasQueEstaInfectado = 0
			cantidadDeIndividuosQueContagio = 0
			
			individuo1 = Individuos(id, self)
			
			self.grid.place_agent(individuo1, pos)
			self.schedule.Add(individuo1)
			
			i = i + 1


		i = 0
		while i < self.numeroDeInfectadosInicial:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			pos = (x, y)
			
			id = self.next_id()

			estaInfectado = False
			cantidadDeDiasQueEstaInfectado = 0
			cantidadDeIndividuosQueContagio = 0
			
			individuo1 = Individuos(id, self)
			individuo1.Infectar()
			print("ver si esta infectdo--")
			print(individuo1.EstaInfectado())
			print("--finr si esta infectdo")
			self.grid.place_agent(individuo1, pos)
			self.schedule.Add(individuo1)
			
			i = i + 1




		print("-------")
		print(self.schedule.CantidadDeIndividuosInfectados())
		print(self.schedule.agents_by_breed[Individuos])
		print("-------")



		self.datacollector.collect(self)     
		self.running = True
	
	def step(self):

		#print("Paso: " + str(self.paso))
		print("")
		
		for individuo in self.schedule.agents:
			pos = individuo.pos
			
			if individuo.EstaInfectado():
				individuo.AgregarUnDiaDeEnfermedad()

		infectados = 0
		losInfectadosContagiaron = 0
		for individuo in self.schedule.agents:
			pos = individuo.pos
			print(individuo.HaceMasDeUnDiaQueEstaInfectado())
			if individuo.HaceMasDeUnDiaQueEstaInfectado():

				print("self.distanciaDeContagioInicial:"+str(self.distanciaDeContagioInicial))

				for vecino in self.grid.get_neighbors(pos, moore = True, include_center = True, radius = self.distanciaDeContagioInicial):
					#print("individuo.unique_id:"+str(individuo.unique_id)+" vecino.unique_id:" + str(vecino.unique_id))

					if (vecino.EsSusceptible() and not vecino.EstaInfectado()):

						nroAleatorioParaInfectar = random.randrange(100)
						print("nroAleatorioParaInfectar:" + str(nroAleatorioParaInfectar))
						if (nroAleatorioParaInfectar < self.probabilidadDeContagiarseInicial):
							vecino.Infectar()
							individuo.AgregarElContagioDeUnIndividuo()
							print("El id:" + str(individuo.unique_id) + " infecto al id:" + str(vecino.unique_id))

			print("individuo.CantidadDeDiasQueHaceQueEstaEnfermo()" + str(individuo.CantidadDeDiasQueHaceQueEstaEnfermo()))
			print("self.duracionDeEnfermedadInicial" + str(self.duracionDeEnfermedadInicial))
			if individuo.CantidadDeDiasQueHaceQueEstaEnfermo() >= self.duracionDeEnfermedadInicial:
				infectados = infectados + 1
				cantidadDeindividuosQueContagio = individuo.VerCantidadDeIndividuosQueContagio()
				losInfectadosContagiaron = losInfectadosContagiaron + cantidadDeindividuosQueContagio

				nroAleatorioParaMortalidad = random.randrange(100)
				print("nroAleatorioParaMortalidad:" + str(nroAleatorioParaMortalidad))
				if (nroAleatorioParaMortalidad < self.probabilidadDeQueMueraInicial):
					individuo.Morir()
				else:
					individuo.Curar()

				print("El id:" + str(individuo.unique_id) + " se inmunizo")
			if not individuo.EstaMuerto():

				posicionesVecinas  = self.grid.get_neighborhood(pos, True, True)
				posicionElejida = random.choice(posicionesVecinas)
				self.grid.move_agent(individuo, posicionElejida)


		if not (infectados == 0):
			promedioDeIndividuosContagiados = losInfectadosContagiaron/infectados
		else:
			promedioDeIndividuosContagiados = 0

		self.schedule.AgregarPromedioR(promedioDeIndividuosContagiados)
		self.schedule.step()
		self.datacollector.collect(self)

		print(" ")
		print(" ")
		print(" ")

		#self.paso = self.paso + 1

	
	def run_model(self, step_count = 200):
		a = 10
