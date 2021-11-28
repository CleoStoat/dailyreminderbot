from dataclasses import dataclass
from typing import Callable, Optional
from telegram.ext.filters import Filters

@dataclass
class HandlerModel:
    priority: int

@dataclass
class CommandModel(HandlerModel):
    name: str
    description: str
    hidden: bool = False
    callback: Callable = None

@dataclass
class MessageModel(HandlerModel):
    name: str
    filters: Filters
    callback: Callable = None
