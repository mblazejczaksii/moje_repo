# kalkulator do obliczania wysokości zarobków na umowie typu b2b
# Maciej Błażejczak MBQA

def liczba_dni_miesiaca(year, month):
    long_months = [1, 3, 5, 7, 8, 10, 12]
    short_months = [4, 6, 9, 11]

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = 1
            else:
                leap = 0
        else:
            leap = 1
    else:
        leap = 0

    if month == 2:
        days = 28 + leap
    elif month in long_months:
        days = 31
    else:
        days = 30
    return days

year = int(input("Podaj rok..."))
month = int(input("Podaj miesiąc..."))
liczba_dni = liczba_dni_miesiaca(year, month)
print(f"Liczba dni w miesiącu wynosi: {liczba_dni}")
