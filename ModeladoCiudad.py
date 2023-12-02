from mesa import Agent, Model  # type: ignore
from mesa.time import SimultaneousActivation  # type: ignore
from mesa.space import MultiGrid  # type: ignore
import networkx as nx  # type: ignore
from typing import Iterator
from collections import deque

from posiciones import celdas_peatones, posicionesEdificios, posicionesEstacionamientos, posicionesGlorietayCamellones, posicionesSemaforos, sigPosEstacionamiento, direcciones_calle, posicionesSemaforosSolas


class Edificio(Agent):
    """
    Un edificio en la ciudad
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class Estacionamiento(Agent):
    """
    Un estacionamiento en la ciudad
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class GlorietaYCamellones(Agent):
    """
    Una glorieta y los camellones en la ciudad
    """

    def __init__(self, model):
        super().__init__("glorietacamellones", model)


class Semaforo(Agent):
    """
    Un semáforo en la ciudad
    """

    def __init__(self, unique_id, model, color, position):
        super().__init__(unique_id, model)
        self.color = color
        self.count = 0
        self.pos = position

    def solicitar_paso(self):
        pareja = self.encontrar_pareja(self.pos)
        celdaPareja = self.model.grid.get_cell_list_contents(pareja)
        for agente in celdaPareja:
            if isinstance(agente, Semaforo):
                agente.color = "red"
                agente.count = 0
        correspondientes = self.encontrar_correspondientes(self.pos)
        celda1 = self.model.grid.get_cell_list_contents(correspondientes[0])
        for agente in celda1:
            if isinstance(agente, Semaforo):
                agente.color = "green"
                agente.count = 0
        celda2 = self.model.grid.get_cell_list_contents(correspondientes[1])
        for agente in celda2:
            if isinstance(agente, Semaforo):
                agente.color = "green"
                agente.count = 0
        self.color = "red"
        self.count = 0

            
    def encontrar_pareja(self, posicion_dada):
        for par in posicionesSemaforos:
            if posicion_dada in par:
                if par[0] == posicion_dada:
                    return par[1] 
                else:
                    return par[0]
            
    def encontrar_correspondientes(self, posicion_dada):
        for par in posicionesSemaforos:
            if posicion_dada in par:
                if posicionesSemaforos.index(par) % 2 == 0:
                    return posicionesSemaforos[posicionesSemaforos.index(par) + 1]
                else:
                    return posicionesSemaforos[posicionesSemaforos.index(par) - 1]


    def step(self):
        self.count += 1
        # Cambiar el color del semaforo cada 5 pasos
        if self.count == 5:
            if self.color == "green":
                self.color = "red"
                self.count = 0
            elif self.color == "red":
                self.color = "green"
                self.count = 0


class Coche(Agent):
    """
    Un coche en la ciudad
    """
    def __init__(self, unique_id, model, estOrigen, estDestino):
        super().__init__(unique_id, model)
        self.estOrigen = estOrigen
        self.estDestino = estDestino
        self.pos = posicionesEstacionamientos[estOrigen - 1]
        self.countPos = 1
        self.path = self.BFS(direcciones_calle, sigPosEstacionamiento[self.estOrigen], sigPosEstacionamiento[self.estDestino])
        self.cochesVecinos = []

    def step(self):
        # Si el coche está frente al estacionamiento destino, meterlo y dejarlo ahí
        if self.pos == sigPosEstacionamiento[self.estDestino] or self.pos == posicionesEstacionamientos[self.estDestino - 1]:
            posicion = posicionesEstacionamientos[self.estDestino - 1]
            self.model.grid.move_agent(self, posicion)
            self.pos = posicion
        else:
            companeros = self.model.grid.get_cell_list_contents(self.pos)
            for companero in companeros:
                if isinstance(companero, Semaforo) and companero.color == "red":
                    return
            sigPos = self.path[0]
            ocupados = self.model.grid.get_cell_list_contents(sigPos)
            for agente in ocupados:
                # if isinstance(agente, Semaforo) and agente.color == "red":
                #     return
                if isinstance(agente, Coche):
                    if self.pos in direcciones_calle.keys():
                        for value in direcciones_calle[self.pos]:
                            ocupados2 = self.model.grid.get_cell_list_contents(value)
                            contCoches = 0
                            for ocupado in ocupados2:
                                if isinstance(ocupado, Coche):
                                    contCoches += 1
                            if value != sigPos and contCoches == 0:
                                sigPos = value
                                self.path = self.BFS(direcciones_calle, value, sigPosEstacionamiento[self.estDestino])
                                break
                            else:
                                sigPos = self.pos
                    else:
                        return
            
            self.model.grid.move_agent(self, sigPos)
            self.pos = sigPos
            if sigPos == self.path[0]:
                self.path.remove(sigPos)

    def BFS(self, graph, start, end):
        if start not in graph or end not in graph:
            raise ValueError("Los nodos de inicio o fin no existen en el grafo.")
        
        queue = deque()
        queue.append(start)
    
        visited = set()
    
        visited.add(start)
    
        pred = {start: None}
    
        while queue:
            current_node = queue.popleft()
            
            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = pred[current_node]
                return path[::-1]
    
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    pred[neighbor] = current_node
                    queue.append(neighbor)
    
        return None


class Peaton(Agent):
    def __init__(self, unique_id, model, posicion):
        super().__init__(unique_id, model)
        self.pos = posicion

    def step(self):
        if self.pos in celdas_peatones:
            possibleSteps = celdas_peatones[self.pos]
            posicion = self.random.choice(possibleSteps)
            vecinos = self.model.grid.get_neighbors(self.pos, False)
            for vecino in vecinos:
                if isinstance(vecino, Semaforo) and vecino.pos == posicion and vecino.color == "green":
                    vecino.solicitar_paso()
                elif isinstance(vecino, Coche) and vecino.pos == posicion and posicion in posicionesEstacionamientos:
                    return
            self.model.grid.move_agent(self, posicion)
            self.pos = posicion
        else:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)


class SimulacionCiudad(Model):
    """
    Una simulacion de una ciudad
    """

    def __init__(self, numPeatones, numCoches):
        self.schedule = SimultaneousActivation(self)
        self.running = True
        self.grid = MultiGrid(25, 25, False)
        # self.estOrigen = estOrigen
        # self.estDestino = estDestino

        # Crear agentes de edificio
        for i in range(len(posicionesEdificios)):
            edificio = Edificio(i, self)
            self.grid.place_agent(edificio, posicionesEdificios[i])

        # Crear agentes de estacionamiento
        for j in range(len(posicionesEstacionamientos)):
            estacionamiento = Estacionamiento(j, self)
            self.grid.place_agent(
                estacionamiento, posicionesEstacionamientos[j])

        # Crear agentes de glorieta
        for k in posicionesGlorietayCamellones:
            glorietacamellones = GlorietaYCamellones(self)
            self.grid.place_agent(glorietacamellones, k)

        # Crear agentes de semáforo
        for l in range(len(posicionesSemaforos)):
            for m in range(2):
                semaforoPos = posicionesSemaforos[l][m]
                # Si la posicion del semaforo es par, ponerlo en verde, si es impar, ponerlo en rojo
                if l % 2 == 0:
                    semaforo = Semaforo(
                        str(semaforoPos), self, "green", semaforoPos)
                else:
                    semaforo = Semaforo(
                        str(semaforoPos), self, "red", semaforoPos)
                self.grid.place_agent(semaforo, semaforoPos)
                self.schedule.add(semaforo)

        # Crear agentes de peatones
        for n in range(numPeatones):
            posicion = self.random.choice(list(celdas_peatones.keys()))
            otros = self.grid.get_cell_list_contents(posicion)
            otrosPeatones = [otro for otro in otros if isinstance(otro, Peaton)]
            while posicion in posicionesSemaforosSolas or len(otrosPeatones) >= 3:
                posicion = self.random.choice(list(celdas_peatones.keys()))
                otros = self.grid.get_cell_list_contents(posicion)
                otrosPeatones = [otro for otro in otros if isinstance(otro, Peaton)]
            peaton = Peaton(f"peaton{n+1}", self, posicion)
            self.grid.place_agent(peaton, posicion)
            self.schedule.add(peaton)

        # Crear agentes de coche
        for o in range(numCoches):
            # TODO: Estacionamientos random
            estOrigen = self.random.choice(range(1, 18))
            estDestino = self.random.choice(range(1, 18))
            while estDestino == estOrigen:
                estDestino = self.random.choice(range(1, 18))
            coche = Coche(o+1, self, estOrigen, estDestino)
            self.grid.place_agent(coche, posicionesEstacionamientos[estOrigen - 1])
            self.schedule.add(coche)

    def step(self):
        self.schedule.step()
        # print(self.getDatos())


    def getDatos(self):
        result = {"coches": {},
                "semaforos": {},
                "peatones": {}}
        for agent in self.schedule.agents:
            if isinstance(agent, Coche):
                result["coches"][agent.unique_id] = {"x": agent.pos[0], "y": agent.pos[1]}
            elif isinstance(agent, Semaforo):
                result["semaforos"][agent.unique_id] = {"estado": agent.color}
            elif isinstance(agent, Peaton):
                result["peatones"][agent.unique_id] = {"x": agent.pos[0], "y": agent.pos[1]}
        return result
