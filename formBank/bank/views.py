from django.shortcuts import render
from django.http import HttpResponse

from .forms import SendRenta, SendFriend


def index(request):
    sendMoneyRentaForm = SendRenta()
    SendMoneyFriend = SendFriend()
    return render(request, "index.html",
                  {"send_renta": sendMoneyRentaForm,
                   "send_money": SendMoneyFriend,
                   })


def send_renta(request):
    form = SendRenta(request.POST)

    # все выше полусаеи значение полей в форме
    if form.is_valid():
        name = form.cleaned_data["nameSender"]
        nameReciever = form.cleaned_data["nameReceiver"]
        number = form.cleaned_data["numberFlat"]
        amount = form.cleaned_data["amountMoney"]
        return HttpResponse(
            f"<h2>Привет, {name}, ты живеш в кв№{number} и ты заплатил {nameReciever} за квартиру {amount} грн.")
    else:
        return HttpResponse("Invalid data")


def send_money(request):
    form = SendFriend(request.POST)

    if form.is_valid():
        name = form.cleaned_data["nameSender"]
        nameReciever = form.cleaned_data["nameReceiver"]
        number = form.cleaned_data["numberBill"]
        amount = form.cleaned_data["amountMoney"]
        return HttpResponse(
            f"<h3>{name}, вы успешно перевели {nameReciever} такую сумму: {amount} грн. Номер счета {nameReciever} такой: {number} "
        )
    else:
        return HttpResponse("Invalid data")
