from django import forms


class SendRenta(forms.Form):
    nameSender = forms.CharField(label="Имя отправителя", min_length=2, max_length=20)
    numberFlat = forms.IntegerField(label="Номер квартиры отправителя", min_value=1, max_value=100)
    nameReceiver = forms.CharField(label="Имя приниманеля", min_length=2, max_length=20)
    amountMoney = forms.FloatField(label="К-ло денег", help_text="ведите в грн", min_value=1)
    field_order = ["nameSender", "nameReceiver", "numberFlat", "amountMoney"]


class SendFriend(forms.Form):  # клас перечисление денег на другой счет
    nameSender = forms.CharField(label="Имя отправителя", min_length=2, max_length=20)
    numberBill = forms.IntegerField(label="номер счета принимателя")
    nameReceiver = forms.CharField(label="Имя приниманеля", min_length=2, max_length=20)
    amountMoney = forms.FloatField(label="К-ло перечисляемых денег", help_text="ведите в грн", min_value=1, max_value=5000)
