kilo = int (input("Kaç Kilo Olduğunuzu Giriniz:"))
boy = int (input("Boyunuzun Kaç Cm Olduğunu Giriniz:"))
boy = boy/100
indeks = kilo/(boy*boy)
print("Vücut kitle index'iniz {}".format(round(indeks)))
print ("İndeks: ", indeks)


if  indeks <=18.5 :
    print("zayıfsınız")
    print("{} Kilo Almalısınız".format(round(25*(boy*boy) -kilo)))
elif indeks< 25 :
    print("Kilonuz Normaldir.")
elif indeks < 30:
    print("fazla kilolusunuz")
    print("{} Kilo Vermelisiniz".format(kilo- round(25*(boy*boy) )))
elif indeks < 35:
    print("1. derece obezsiniz")
    print("{} Kilo Vermelisiniz".format(kilo- round(25*(boy*boy) )))
elif indeks < 40:
    print("2. derece obezsiniz")
    print("{} Kilo Vermelisiniz".format(kilo- round(25*(boy*boy) )))
elif indeks < 45:
    print("3. derece obezsiniz")
    print("{} Kilo Vermelisiniz".format(kilo- round(25*(boy*boy) )))
