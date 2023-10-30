from django.shortcuts import render

from.forms import CarInfosForm


def index(request):
    if request.method == "POST":
        form = CarInfosForm(request.POST)
        if form.is_valid():
            note_eco = 0

            match form.cleaned_data["fabyear"]:
                case "2010":
                    note_eco += 7
                case "2000-2010":
                    note_eco += 5
                case "1990-2000":
                    note_eco += 4
                case "1980-1990":
                    note_eco += 3
                case "1970-1980":
                    note_eco += 2
                case "1960-1970":
                    note_eco += 1

            match form.cleaned_data["type"]:
                case "city":
                    note_eco += 8
                case "convertible":
                    note_eco += 6
                case "sedan":
                    note_eco += 6.5
                case "suv":
                    note_eco += 4

            match form.cleaned_data["energy"]:
                case "electrique":
                    note_eco += 9
                case "hybride":
                    note_eco += 7
                case "gaz":
                    note_eco += 6
                case "essence":
                    note_eco += 5
                case "diesel":
                    note_eco += 4

            match form.cleaned_data["km"]:
                case "5000-10000":
                    note_eco += 9
                case "10000-15000":
                    note_eco += 7
                case "15000-20000":
                    note_eco += 5
                case "20000-25000":
                    note_eco += 3
                case "25000-30000":
                    note_eco += 1

            if note_eco <= 10:
                rate = 3
            elif note_eco <= 15:
                rate = 2.74
            elif note_eco <= 25:
                rate = 2.52
            elif note_eco <= 33:
                rate = 2.1
            elif note_eco >= 34:
                rate = 1.85

            print(rate)

            match form.cleaned_data["passagers"]:
                case "4":
                    rate -= 0.53
                case "3":
                    rate -= 0.29
                case "2":
                    rate -= 0.17
                case "1":
                    rate += 0.11
            #                                                                                   Note Eco a un max de 33  10 = Plus Basse note    Permet de mettre l'aiguille a fond quand on a une bonne empreinte
            return render(request, "index.html", {"form": form, "rate": format(rate, ".2f"), "rotate": (note_eco + int(form.cleaned_data["passagers"]) - 11) / 26 * 270})
        
    else:
        form = CarInfosForm()
        return render(request, "index.html", {"form": form, "rate": "0.00"})
