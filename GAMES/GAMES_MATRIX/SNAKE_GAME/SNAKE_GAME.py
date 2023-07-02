
import json
import random
from flojoy import flojoy, DataContainer
import numpy as np 

from PYTHON.node_sdk.small_memory import SmallMemory


memory_key = "snake_game_info"
snake_dimension = 22

class SnakeData:
    def __init__(
            self, node_id, x_coords = [int(snake_dimension/2)], y_coords = [int(snake_dimension/2)], delta_x = 0, delta_y = 1, is_finished=False,
            food_x = int(snake_dimension/2), food_y = snake_dimension-4, to_grow = False,
    ) -> None:
        self.node_id = node_id
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.is_finished = bool(is_finished)
        self.food_x = food_x
        self.food_y = food_y
        self.to_grow = to_grow
    
    def get_data(self):
        return self.__dict__
    
    @staticmethod
    def from_data(node_id, data: dict):
        if len(data) == 0:
            return SnakeData(node_id)
        snake_data = SnakeData(**data)
        return snake_data
    
    def print(self, prefix=""):
        print(f"{prefix}snake Data:", json.dumps(self.get_data(), indent=2))

@flojoy
def SNAKE_GAME(dc_inputs: list[DataContainer], params: dict) -> dict:
    """The SNAKE_GAME node is a specialized node that iterates through the body nodes for a given number of times.
    To ensure proper functionality, the SNAKE_GAME node relies on a companion node called the `GOTO` node.

    Parameters
    ----------
    num_loops : int
        number of times to iterate through body nodes default is `-1` meaning infinity.
    """

    # get snake game data 
    control_input = dc_inputs[0]

    if control_input.type != 'ordered_pair':
        raise ValueError(f"unsupported DataContainer type passed for SNAKE_GAME: {control_input.type}")

    node_id = params.get("node_id", 0) # WARNING: special case, it gets the node id from the params despite not being specified 
    print("NODE ID IS: ", node_id)
    snake_data: SnakeData = load_data(node_id)

    # get control inputs
    delta_x = snake_data.delta_x
    delta_y = snake_data.delta_y
    if control_input.y[8]:
        delta_x = 1
        delta_y = 0
    elif control_input.y[9]:
        delta_x = 1
        delta_y = 0
    elif control_input.y[6]:
        delta_y = 1
        delta_x = 0
    elif control_input.y[7]:
        delta_y = 1
        delta_x = 0
    
    snake_data.delta_x = delta_x
    snake_data.delta_y = delta_y

    # update snake position
    snake_data.x_coords.insert(0, snake_data.x_coords[0] + snake_data.delta_x)
    snake_data.y_coords.insert(0, snake_data.y_coords[0] + snake_data.delta_y)
    if not snake_data.to_grow:
        snake_data.x_coords.pop()
        snake_data.y_coords.pop()
    else:
        snake_data.to_grow = False
    
    # check if out of bounds
    if snake_data.x_coords[0] < 0 or snake_data.x_coords[0] > snake_dimension-1 or snake_data.y_coords[0] < 0 or snake_data.y_coords[0] > snake_dimension-1:
        snake_data.is_finished = True
    
    # check if snake is eating itself
    for i in range(len(snake_data.x_coords)):
        if i == 0:
            continue
        if snake_data.x_coords[0] == snake_data.x_coords[i] and snake_data.y_coords[0] == snake_data.y_coords[i]:
            snake_data.is_finished = True

    if snake_data.is_finished:
        print("GAME OVER, RESETTING")
        snake_data = SnakeData(node_id)
        store_data(node_id, snake_data)
        return output_game(snake_data)


    # check if snake is eating food
    if snake_data.x_coords[0] == snake_data.food_x and snake_data.y_coords[0] == snake_data.food_y:
        snake_data.to_grow = True
        next_x, next_y = get_next_food_spot(snake_data)
        snake_data.food_x = next_x
        snake_data.food_y = next_y

    # store snake game data
    store_data(node_id, snake_data)

    # output game
    return output_game(snake_data)
    

def load_data(node_id) -> SnakeData:
    data = SmallMemory().read_memory(node_id, memory_key) or {}
    print("LOAD DATA IS ", data)
    snake_data = SnakeData.from_data(
        node_id=node_id, data=data
    )
    return snake_data

def store_data(node_id, snake_data: SnakeData):
    SmallMemory().write_to_memory(node_id, memory_key, snake_data.get_data())
    snake_data.print("store snake game data")

def get_next_food_spot(snake_data):
    taken = set()
    for i in range(len(snake_data.x_coords)):
        taken.add((snake_data.x_coords[i],snake_data.y_coords[i]))
    
    free = set()
    for i in range(snake_dimension):
        for j in range(snake_dimension):
            if ((i,j) not in taken):
                free.add((i,j))
    
    return random.choice(list(free))
    


# def delete_data(node_id):
#     SmallMemory().delete_object(node_id, memory_key)
#     print("delete snake game data")

def output_game(snake_data):
    r = [[10 for i in range(snake_dimension)] for j in range(snake_dimension)]
    g = [[10 for i in range(snake_dimension)] for j in range(snake_dimension)]
    b = [[10 for i in range(snake_dimension)] for j in range(snake_dimension)]
    for i in range(len(snake_data.x_coords)):
        x_coord = snake_data.x_coords[i]
        y_coord = snake_data.y_coords[i]
        g[y_coord][x_coord] = 255
    r[snake_data.food_y][snake_data.food_x] = 255
    dc =  DataContainer(type="image", r=np.array(r), g=np.array(g), b=np.array(b), a=None)
    print("OUTPUT GAME IS ", dc)
    return dc