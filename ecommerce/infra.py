
from __future__ import annotations
from typing import Dict, Optional
from .domain import Order
from .ports import Notifier, OrderRepository

class ConsoleNotifier:
    def send(self, to_email: str, subject: str, body: str) -> None:
        print(f"[MAIL to {to_email}] {subject}\n{body}\n")

class InMemoryOrderRepository:
    def __init__(self):
        self._db: Dict[str, Order] = {}

    def save(self, order: Order) -> None:
        order_id = f"{order.user.email}:{len(self._db)+1}"
        self._db[order_id] = order

    def get(self, order_id: str) -> Optional[Order]:
        return self._db.get(order_id)
