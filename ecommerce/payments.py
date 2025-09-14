
from __future__ import annotations
from abc import ABC, abstractmethod

class PaymentMethod(ABC):  # Abstraction
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Process payment and return a transaction id"""

class CreditCardPayment(PaymentMethod):
    def __init__(self, last4: str):
        self.last4 = last4

    def pay(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        # polymorphic override
        return f"cc_txn_{self.last4}_{int(amount * 100)}"

class PayPalPayment(PaymentMethod):
    def __init__(self, account_email: str):
        self.account_email = account_email

    def pay(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return f"pp_txn_{self.account_email.split('@')[0]}_{int(amount * 100)}"
