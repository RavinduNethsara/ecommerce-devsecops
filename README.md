
# E-commerce Mini-App (OOP + SOLID Demo)

This project demonstrates Abstraction, Encapsulation, Inheritance, and Polymorphism,
and applies SRP, LSP, and DIP using a small, clean Python design.

## Quick Start (VS Code)

1. **Open folder** `ecommerce_app` in VS Code.
2. **Create virtual env (optional):**
   ```bash
   python -m venv .venv
   # Activate:
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -U pip
   ```
3. **(Optional) Install pytest for tests**
   ```bash
   pip install pytest
   ```
4. **Run the demo**
   ```bash
   python -m ecommerce.demo
   ```

You should see console output for a placed order, transaction IDs, and an admin check.

## Where requirements are satisfied

- **Abstraction:** `payments.PaymentMethod`, `ports.Notifier`, `ports.OrderRepository`
- **Encapsulation:** `domain.Email`, `domain.User.email` property, `domain.Order.total/mark_paid`
- **Inheritance:** `domain.AdminUser(User)`
- **Polymorphism:** `CreditCardPayment` and `PayPalPayment` used via `PaymentMethod`
- **SRP:** `OrderService` (order orchestration), `PaymentService` (charging), `InMemoryOrderRepository`, `ConsoleNotifier`
- **LSP:** Both payment implementations pass through the same `PaymentMethod` interface in services/tests
- **DIP:** Services depend on abstractions (Protocols/ABCs) injected via constructors

## Run Tests
```bash
pytest -q
```

## Extend (OCP-friendly)
Add a new payment type by creating a new class implementing `PaymentMethod`. No changes needed in services.
