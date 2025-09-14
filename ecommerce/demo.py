
from __future__ import annotations
from .domain import User, AdminUser, Product, Order
from .payments import PaymentMethod, CreditCardPayment, PayPalPayment
from .infra import InMemoryOrderRepository, ConsoleNotifier
from .services import PaymentService, OrderService

def demo():
    # Setup (compose via abstractions)
    repo = InMemoryOrderRepository()
    notifier = ConsoleNotifier()
    pay_svc = PaymentService()
    order_svc = OrderService(repo, notifier, pay_svc)

    # Data
    user = User("buyer@example.com")
    admin = AdminUser("admin@example.com")  # Inheritance
    prod = Product(sku="SKU123", name="Wireless Mouse", price=19.99)

    # Build order (Encapsulation: totals computed safely; cannot flip paid flag directly)
    order = Order(user=user)
    order.add_item(prod, 2)  # $39.98

    # Choose payment at runtime (Polymorphism via Abstraction)
    payment: PaymentMethod = CreditCardPayment(last4="4242")
    txn1 = order_svc.place_and_pay(order, payment)
    print("Paid with card:", txn1)

    # LSP: swap in another subclass and it still works
    another_payment: PaymentMethod = PayPalPayment(account_email="wallet@paypal.com")
    txn2 = pay_svc.charge(another_payment, 12.34)
    print("Paid with PayPal:", txn2)

    # Admin-specific behavior (Inheritance)
    print("Admin can refund?", admin.can_refund())

if __name__ == "__main__":
    demo()
