from typing import Tuple, List, Dict

Node: Tuple[int, int] = (0, 0)
Grid: List[List[int]] = [[0]]
NodeList: List[Tuple[int, int]] = [(0, 0)]
Edge: Tuple[Tuple[int, int], Tuple[int, int]] = ((0, 0), (0, 0))
Edges: List[Tuple[Tuple[int, int], Tuple[int, int]]] = [((0, 0), (0, 0))]
Path: Dict[Tuple[int, int]: Tuple[int, int]] = {(0, 0) : (0, 0)}
