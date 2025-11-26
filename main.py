from conversions.conversions import c_to_f, f_to_c, km_to_miles, miles_to_km, L_to_gal, gal_to_L
from finance_tools.finance_tools import add_tax, tip, split_bill, monthly_payment
from text_tools.text_tools import shout, reverse, count_words

def conversion_menu():
    print("\nTemperature Converter")
    print("1. Celsius to Farenheit")
    print("2. Farenehit to Celsius")
    choice = input("Choose (1/2): ")

    if choice == "1":
        c = float(input("Celsius: "))
        print(f"{c}°C = {c_to_f(c):.2f}°F")
    elif choice == "2":
        f = float(input("Farenheit: "))
        print(f"{f}°F = {f_to_c(f):.2f}°C")
    else:
        print("Invalid choice")

    print("\nDistance Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose (1/2): ")

    if choice == "1":
        km = float(input("Kilometers: "))
        print(f"{km}km = {km_to_miles(km):.2f}")
    elif choice == "2":
        miles = float(input("Miles: "))
        print(f"{miles}miles = {miles_to_km(miles):.2f}")
    else:
        print("Invalid choice")

    print("\nVolume Converter")
    print("1. Liters to Gallons (US)")
    print("2. Gallons (US) to Litres")
    choice = input("Choose (1/2): ")

    if choice == "1":
        L = float(input("Litres: "))
        print(f"{L}L = {L_to_gal(L):.2f}")
    elif choice == "2":
        gal = float(input("Gallons (US): "))
        print(f"{gal}gallons = {gal_to_L(gal):.2f}")
    else:
        print("Invalid choice")


print("30°C in F: ", c_to_f(30))
print("104°F in C: ", f_to_c(104))
print("10 km in miles: ", km_to_miles(10))
print("50 mi in kilometers: ", miles_to_km(50))
print("30 L in gallons (US): ", L_to_gal(30))
print("20 gallons (US) in L: ", gal_to_L(20))

print("Total with tax:", add_tax(100, 0.12))
print("Tip on $40:", tip(40))
print("Amount per person: ", split_bill(238, 3))
print("Monthly payment total: ", monthly_payment(740, 0.18, 13 ) )

print(shout("hello world"))
print(reverse("hello world"))
print("Word count:", count_words("This has been a fun learning engagement!"))
