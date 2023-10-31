from django import forms


class CarInfosForm(forms.Form):
    FABRICATION_YEARS = [
        ('2010','2010 et Après'),
        ('2000-2010','2000-2009'),
        ('1990-2000','1990-1999'),
        ('1980-1990','1980-1988'),
        ('1970-1980','1970-1979'),
        ('1960-1970','1960-1969')
    ]

    VEHICULES_TYPES = [
        ("city", "Citadine"),
        ("convertible", "Cabriolet"),
        ("sedan", "Berline"),
        ("suv", "SUV / 4x4")
    ]

    ENERGY = [
        ("electrique", "Electrique"),
        ("hybride", "Hybride"),
        ("gaz", "Gaz"),
        ("essence", "Essence"),
        ("diesel", "Diesel"),
    ]

    KM = [
        ("5000-10000", "5 000 - 9 000 km/an"),
        ("10000-15000", "10 000 - 14 000 km/an"),
        ("15000-20000", "15 000 - 19 000 km/an"),
        ("20000-25000", "20 000 - 24 000 km/an"),
        ("25000-30000", "25 000 - km/an et Plus")
    ]

    PASSAGERS = [
        ("4", "4 Passagers et Plus"),
        ("3", "3 Passagers"),
        ("2", "2 Passagers"),
        ("1", "1 Passager")
    ]

    fabyear = forms.ChoiceField(choices=FABRICATION_YEARS, required=True)
    type = forms.ChoiceField(choices=VEHICULES_TYPES, required=True)
    energy = forms.ChoiceField(choices=ENERGY, required=True)
    km = forms.ChoiceField(choices=KM, required=True)
    passagers = forms.ChoiceField(choices=PASSAGERS, required=True)