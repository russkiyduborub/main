def mask_account_card():
    count = sum(c.isdigit() for c in enter)
    if count == 20:
        print(f"Зашифрованный номер счета: {enter[-30:-21]} **{enter[-5:-1]}")
    elif count == 16:
        print(f"Зашифрованный номер карты: {enter[-30:-17]} {enter[-16:-12]} **** **{enter[-6:-4]}  {enter[-4:0]}")


enter=input("Введите тип и номер карты или счета: ")
mask_account_card()