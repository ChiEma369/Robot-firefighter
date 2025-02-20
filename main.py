'''mv : move
- temp : temperature
- forw: forward
-backw: backward

'''
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, List, Dict
import numpy as np
import heapq

def f():
    pass

@dataclass(frozen=True)
class State:  #kgian 3D
    x : int
    y : int
    z : int
    temp: int # 0: normal 1: high 2:dangerous
    pressure: int # 0: safe 1:dangerous
    obstacle: int # 0 1: debris 3: exit
    victim: int # 0 1

class action(Enum):
    mv_forw = 0
    mv_backw = 1
    turn_left = 2
    turn_right = 3
    jupm = 4
    crouch = 5
    rescue_victim = 6
    scan_temp = 7
    scan_pressure = 8
    pass_overObstacle = 9
    clear_debris = 10

def heuristic(state: State, goal: State) -> float:
    return abs(state.x - goal. x) + abs(state.y - goal.y) + abs(state.z - goal.z)


