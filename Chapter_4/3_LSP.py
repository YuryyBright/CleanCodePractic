# Liskov's substitution principle


### Useful tools:  Mypy, Pylint


# BAD WAY

class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden.")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processed credit card payment of ${amount}"


class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processed PayPal payment of ${amount}"


class CashPayment(Payment):
    def process_payment(self, amount):
        raise Exception("Cash payment cannot be processed online.")


def make_payment(payment: Payment, amount):
    print(payment.process_payment(amount))


# Використання
credit_card_payment = CreditCardPayment()
make_payment(credit_card_payment, 100)  # Виведе: Processed credit card payment of $100

paypal_payment = PayPalPayment()
make_payment(paypal_payment, 50)  # Виведе: Processed PayPal payment of $50

cash_payment = CashPayment()
make_payment(cash_payment, 20)  # Викине виключення: Cash payment cannot be processed online.


### BEST WAY

class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden.")


class OnlinePayment(Payment):
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden for online payments.")


class CreditCardPayment(OnlinePayment):
    def process_payment(self, amount):
        return f"Processed credit card payment of ${amount}"


class PayPalPayment(OnlinePayment):
    def process_payment(self, amount):
        return f"Processed PayPal payment of ${amount}"


class CashPayment(Payment):
    def process_payment(self, amount):
        return f"Processed cash payment of ${amount}"


def make_online_payment(payment: OnlinePayment, amount):
    print(payment.process_payment(amount))


# Використання
credit_card_payment = CreditCardPayment()
make_online_payment(credit_card_payment, 100)  # Виведе: Processed credit card payment of $100

paypal_payment = PayPalPayment()
make_online_payment(paypal_payment, 50)  # Виведе: Processed PayPal payment of $50

# Готівковий платіж обробляється окремо
cash_payment = CashPayment()
print(cash_payment.process_payment(20))  # Виведе: Processed cash payment of $20
