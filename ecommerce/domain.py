
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

class Email:
    """Value object demonstrating encapsulation (validation hidden behind a property)."""
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, v: str):
        if "@" not in v:
            raise ValueError("Invalid email address")
        self._value = v

    def __str__(self) -> str:
        return self._value


class User:
    """Encapsulation: keep invariants safe (email validation handled by Email)."""
    def __init__(self, email: str):
        self._email = Email(email)

    @property
    def email(self) -> str:
        return self._email.value


class AdminUser(User):  # Inheritance
    def can_refund(self) -> bool:
        return True


@dataclass
class Product:
    sku: str
    name: str
    price: float


@dataclass
class OrderItem:
    product: Product
    quantity: int

    @property
    def line_total(self) -> float:
        return round(self.product.price * self.quantity, 2)


@dataclass
class Order:
    user: User
    items: List[OrderItem] = field(default_factory=list)
    _paid: bool = field(default=False, init=False, repr=False)

    def add_item(self, product: Product, qty: int) -> None:
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append(OrderItem(product, qty))

    @property
    def total(self) -> float:
        return round(sum(i.line_total for i in self.items), 2)

    @property
    def is_paid(self) -> bool:
        return self._paid

    def mark_paid(self) -> None:
        self._paid = True
