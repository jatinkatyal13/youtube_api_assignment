import itertools as it
from typing import List, Callable, Any, Dict


def group_by(lizt: List[Any], key: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
    sorted_list = sorted(lizt, key=key)
    return {k: list(v) for k, v in it.groupby(sorted_list, key)}

def id_map(lizt: List[Any], key: Callable[[Any], Any]) -> Dict[Any, Any]:
    list_map = group_by(lizt, key=key)
    assert all(len(v) == 1 for v in list_map.values())
    return {k: v[0] for k, v in list_map.items()}
