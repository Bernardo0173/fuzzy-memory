from ActividadIntegradora import *  # type: ignore
from mesa.visualization.modules import CanvasGrid  # type: ignore
from mesa.visualization.ModularVisualization import ModularServer  # type: ignore


def agentPortrayal(agent):

    portrayal = {}

    if isinstance(agent, Edificio):
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "#5B9BD5",
                     "h": 1,
                     "w": 1
                     }

    elif isinstance(agent, Estacionamiento):
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "yellow",
                     "h": 1,
                     "w": 1
                     }

    elif isinstance(agent, Glorieta):
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "grey",
                     "h": 1,
                     "w": 1
                     }

    elif isinstance(agent, Semaforo):
        if agent.color == "red":
            portrayal = {"Shape": "circle",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "red",
                         "r": 0.8
                         }
        elif agent.color == "green":
            portrayal = {"Shape": "circle",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "green",
                         "r": 0.8
                         }

    elif isinstance(agent, Coche):
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "purple",
                     "r": 0.8
                     }

    return portrayal


# Indicar estacionamiento origen y destino
origen = 1
destino = 11


model = SimulacionCiudad(origen, destino)

grid = CanvasGrid(agentPortrayal, 24, 24, 750, 500)

server = ModularServer(SimulacionCiudad, [grid], "Simulacion Ciudad", {
                       "estOrigen": origen, "estDestino": destino})
server.port = 8521

server.launch()
model.step()