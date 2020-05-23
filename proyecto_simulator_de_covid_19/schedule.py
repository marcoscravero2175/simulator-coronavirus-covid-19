from collections import defaultdict

from framework_mesa.time import RandomActivation
from proyecto_simulator_de_covid_19.individuos import Individuos

class RandomActivationByBreed(RandomActivation):
    model = None

    def __init__(self, model):
        super().__init__(model)
        self.agents_by_breed = defaultdict(dict)
        self.model = model
        self.promedioTotalR = 0

    def Add(self, individuo):

        self._agents[individuo.unique_id] = individuo
        individuo_class = type(individuo)
        self.agents_by_breed[individuo_class][individuo.unique_id] = individuo
        
    def Remove(self, individuo):

        del self._agents[individuo.unique_id]

        individuo_class = type(individuo)
        del self.agents_by_breed[individuo_class][individuo.unique_id]

    def CantidadDeIndividuos1(self):
        n = len(self.agents_by_breed[Individuos])
        return n
        
    def PorcentajeDeIndividuosSusceptibles(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EsSusceptible() and (not individuo.EstaInfectado()):
                n = n + 1
        if not n == 0:
            n = round(n/todos, 2)
        else:
            n = 0
        
        return n
        
    def PorcentajeDeIndividuosInfectados(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EstaInfectado():
                n = n + 1
        if not n == 0:
            n = round(n/todos, 2)
        else:
            n = 0
        
        return n
        
    def PorcentajeDeIndividuosInmunizados(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EstaInmunizado():
                n = n + 1
        if not n == 0:
            n = round(n/todos, 2)
        else:
            n = 0
        
        return n
        
    def PorcentajeDeIndividuosMuertos(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EstaMuerto():
                n = n + 1
        if not n == 0:
            n = round(n/todos, 2)
        else:
            n = 0
        
        return n
        
    def CantidadDeIndividuosSusceptibles(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EsSusceptible() and (not individuo.EstaInfectado()):
                n = n + 1
        
        return n

    def CantidadDeIndividuosInfectados(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EstaInfectado():
                n = n + 1
        return n

    def CantidadDeIndividuosInmunizados(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EstaInmunizado():
                n = n + 1
        
        return n

    def CantidadDeIndividuosMuertos(self):
        todos = len(self.agents_by_breed[Individuos])
        n = 0
        for i in self.agents_by_breed[Individuos]:
            individuo = self.agents_by_breed[Individuos][i]
            if individuo.EstaMuerto():
                n = n + 1
        
        return n

    def AgregarPromedioR(self, promedioDeIndividuosContagiados):
        self.promedioTotalR = (0.50)*self.promedioTotalR + (0.50)*promedioDeIndividuosContagiados


    def VerPromedioR(self):
        
        return self.promedioTotalR

