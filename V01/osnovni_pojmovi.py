# komentar
print("ABCD")

print("latinica, ћирилица")

print("Hello world")
print(3.2)
print(650)

#identifikator je naziv koji jedinstveno oznacava element programa
#imenovanje promenljivih
iznos_kamate = 0.003
pocetni_ulog = 10000
inflacija = 0.001

iznos_nakon_1_godine_bez_inflacije = pocetni_ulog*(1+iznos_kamate)
iznos_nakon_1_godine_sa_inflacijom = pocetni_ulog/(1+inflacija)

print("iznosi nakon 1 godine bez i sa inflacijom ",iznos_nakon_1_godine_bez_inflacije, iznos_nakon_1_godine_sa_inflacijom)

#upotreba funkcije eval
iznos = eval(input("Unesite neki broj: "))
novi_iznos = iznos + 1000
print("Nov iznos = "+str(novi_iznos))

a = 0.1*0.1
b = 0.01
print("Da li su 0.1*0.1 i 0.01 jednaki?", a==b)
