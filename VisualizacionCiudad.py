from ModeladoCiudad import *  # type: ignore
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

    elif isinstance(agent, GlorietaYCamellones):
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
        if agent.unique_id % 2:
            portrayal = {"Shape": "circle",
                        "Filled": "true",
                        "Layer": 0,
                        "Color": "purple",
                        "r": 0.8
                        }
        else:
            portrayal = {"Shape": "circle",
                        "Filled": "true",
                        "Layer": 0,
                        "Color": "orange",
                        "r": 0.8
                        }

    elif isinstance(agent, Peaton):
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "black",
                     "r": 0.5
                     }

    return portrayal


# Indicar el número de peatones
numPeatones = 50
numCoches = 500

model = SimulacionCiudad(numPeatones, numCoches)

grid = CanvasGrid(agentPortrayal, 25, 25, 750, 500)

server = ModularServer(SimulacionCiudad, [grid], "Simulacion Ciudad", {
                       "numPeatones": numPeatones, "numCoches": numCoches})
server.port = 8521

server.launch()
model.step()
