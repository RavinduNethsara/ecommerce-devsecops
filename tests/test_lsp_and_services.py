
from ecommerce.domain import User, Product, Order
from ecommerce.payments import CreditCardPayment, PayPalPayment, PaymentMethod
from ecommerce.services import PaymentService, OrderService
from ecommerce.infra import InMemoryOrderRepository, ConsoleNotifier

def setup_order():
    user = User("buyer@example.com")
    p = Product("SKU", "Thing", 10.0)
    o = Order(user)
    o.add_item(p, 3)  # 30.0
    return o

def test_lsp_creditcard_and_paypal():
    svc = PaymentService()
    assert isinstance(svc.charge(CreditCardPayment("1234"), 10.0), str)
    assert isinstance(svc.charge(PayPalPayment("a@b.com"), 5.0), str)

def test_order_service_works_with_any_payment():
    repo = InMemoryOrderRepository()
    notifier = ConsoleNotifier()
    pay = PaymentService()
    orders = OrderService(repo, notifier, pay)

    order = setup_order()
    txn = orders.place_and_pay(order, CreditCardPayment("4242"))
    assert order.is_paid
    assert isinstance(txn, str)

def test_amount_validation():
    svc = PaymentService()
    try:
        svc.charge(CreditCardPayment("0000"), 0)
        assert False, "Should raise"
    except ValueError:
        assert True
