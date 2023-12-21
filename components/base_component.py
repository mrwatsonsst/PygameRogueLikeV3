from __future__ import annotations
# f
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity
    from game_map import GameMap

class BaseComponent:
    parent: Entity

    @property
    def gamemap(self) -> GameMap:
        return self.parent.game_map

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine
