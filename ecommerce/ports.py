
from __future__ import annotations
from typing import Protocol, Optional
from .domain import Order

class Notifier(Protocol):  # ISP: small focused interface
    def send(self, to_email: str, subject: str, body: str) -> None: ...

class OrderRepository(Protocol):  # DIP boundary for persistence
    def save(self, order: Order) -> None: ...
    def get(self, order_id: str) -> Optional[Order]: ...
