print("Nasz program wylicza BMI")

masa = int(input("Podaj masę w kg "))
wzrost = float(input("podaj wzrost w Metrach "))
bmi = masa/wzrost**2

print("Twoje BMI to:", bmi)

if  bmi < 18.5:
    print("niedowaga")
elif 18.5 >=  bmi < 25:
    print("dobra waga")
elif  25 >= bmi < 29:
    print("Nadwaga")
else :
    print("Otyłość")
    