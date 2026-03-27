def get_mask_card_number():#maskirovka nomera bankovskoi karty
    print(f"Зашифрованный номер карты: {enter_card[-16:-12]} **** **{enter_card[-6:-4]}  {enter_card[-4:0]}")


def get_mask_account():#maskirovka nomera bankovskogo cheta
    print(f"зашифрованный номер счета: **{enter_schet[-5:-1]}")


enter_card=input("Введите номер карты без пробелов: ")
enter_schet=input("Введите номер карты без пробелов: ")
get_mask_card_number()
get_mask_account()