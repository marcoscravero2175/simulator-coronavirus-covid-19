from framework_mesa import Agent

import random

class Individuos(Agent):

	estadoDeSalud = "Susceptible"
	cantidadDeDiasQueEstaInfectado = 0
	cantidadDeIndividuosQueContagio = 0

	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)

		self.estadoDeSalud = "Susceptible"
		self.cantidadDeDiasQueEstaInfectado = 0
		self.cantidadDeIndividuosQueContagio = 0
        
	def Step(self):
		self.edad = self.edad + 1

	def EsSusceptible(self):
		devolver = (self.estadoDeSalud == "Susceptible") or (self.estadoDeSalud == "Infectado") 
		return devolver

	def EstaInfectado(self):
		devolver = (self.estadoDeSalud == "Infectado")
		return devolver


	def EstaInmunizado(self):
		devolver = self.estadoDeSalud == "Inmunizado"
		return devolver

	def EstaMuerto(self):
		devolver = self.estadoDeSalud == "Muerto"
		return devolver

	def AgregarUnDiaDeEnfermedad(self):
		self.cantidadDeDiasQueEstaInfectado = self.cantidadDeDiasQueEstaInfectado + 1

	def HaceMasDeUnDiaQueEstaInfectado(self):
		devolver = (self.cantidadDeDiasQueEstaInfectado > 0)
		return devolver

	def CantidadDeDiasQueHaceQueEstaEnfermo(self):
		devolver = self.cantidadDeDiasQueEstaInfectado
		return devolver


	def VerCantidadDeIndividuosQueContagio(self):
		devolver = self.cantidadDeIndividuosQueContagio
		return devolver

	def AgregarElContagioDeUnIndividuo(self):
		self.cantidadDeIndividuosQueContagio = self.cantidadDeIndividuosQueContagio + 1


	def Infectar(self):
		self.cantidadDeDiasQueEstaInfectado = 0
		self.estadoDeSalud = "Infectado"

	def Curar(self):
		self.cantidadDeDiasQueEstaInfectado = 0
		self.estadoDeSalud = "Inmunizado"

	def Morir(self):
		self.cantidadDeDiasQueEstaInfectado = 0
		self.estadoDeSalud = "Muerto"





