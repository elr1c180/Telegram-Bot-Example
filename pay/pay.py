from yoomoney import Quickpay

# Создаем функцию, которая возвращает ссылку на оплату 2р
def payment_link():
    quickpay = Quickpay(
                receiver="",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=2,
                )
    return quickpay.redirected_url
