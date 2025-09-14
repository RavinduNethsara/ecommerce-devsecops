
from __future__ import annotations
from .payments import PaymentMethod
from .ports import Notifier, OrderRepository
from .domain import Order

class PaymentService:
    """SRP: only handles charging; DIP: depends on PaymentMethod abstraction."""
    def charge(self, method: PaymentMethod, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return method.pay(amount)  # polymorphic call

class OrderService:
    """
    SRP: orchestrates orders (create/pay/notify).
    DIP: takes OrderRepository + Notifier abstractions via constructor injection.
    """
    def __init__(self, repo: OrderRepository, notifier: Notifier, payment_service: PaymentService):
        self.repo = repo
        self.notifier = notifier
        self.payment_service = payment_service

    def place_and_pay(self, order: Order, payment: PaymentMethod) -> str:
        if not order.items:
            raise ValueError("Cannot place empty order")
        txn = self.payment_service.charge(payment, order.total)  # DIP + polymorphism
        order.mark_paid()
        self.repo.save(order)
        self.notifier.send(
            to_email=order.user.email,
            subject="Your order was placed",
            body=f"Total: ${order.total} | Transaction: {txn}"
        )
        return txn
