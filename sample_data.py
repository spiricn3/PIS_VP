import requests

# Definisanje BASE_URL adrese vašeg API-ja
BASE_URL = "http://127.0.0.1:8000/api/"

# Testni podaci za vozila
vozila = [
    {
        "marka": "Toyota", "model": "Corolla", "registracijski_broj": "BG1234AB", 
        "datum_isteka_registracije": "2024-06-01", "godina_proizvodnje": 2018, 
        "tip_goriva": "benzin", "status": "dostupno"
    },
    {
        "marka": "Honda", "model": "Civic", "registracijski_broj": "NS5678CD", 
        "datum_isteka_registracije": "2024-06-01", "godina_proizvodnje": 2020, 
        "tip_goriva": "dizel", "status": "dostupno"
    },
    {
        "marka": "Ford", "model": "Focus", "registracijski_broj": "KG9101EF", 
        "datum_isteka_registracije": "2024-06-01", "godina_proizvodnje": 2019, 
        "tip_goriva": "benzin", "status": "dostupno"
    },
    {
        "marka": "Volkswagen", "model": "Golf", "registracijski_broj": "SU2345GH", 
        "datum_isteka_registracije": "2024-06-01", "godina_proizvodnje": 2017, 
        "tip_goriva": "dizel", "status": "dostupno"
    },
    {
        "marka": "Skoda", "model": "Octavia", "registracijski_broj": "NI6789IJ", 
        "datum_isteka_registracije": "2024-06-01", "godina_proizvodnje": 2021, 
        "tip_goriva": "plin", "status": "dostupno"
    }
]

# Testni podaci za vozače
vozaci = [
    {
        "ime": "Marko", "prezime": "Markovic", "broj_vozacke_dozvole": "123456789", 
        "datum_isteka_dozvole": "2025-01-01", "kategorije_vozacke_dozvole": "B", 
        "kontakt_informacije": "marko@example.com", "ogranicenja_za_voznju": "Nema", "status": "aktivno"
    },
    {
        "ime": "Jovan", "prezime": "Jovanovic", "broj_vozacke_dozvole": "987654321", 
        "datum_isteka_dozvole": "2025-01-01", "kategorije_vozacke_dozvole": "C", 
        "kontakt_informacije": "jovan@example.com", "ogranicenja_za_voznju": "Nema", "status": "aktivno"
    },
    {
        "ime": "Petar", "prezime": "Petrovic", "broj_vozacke_dozvole": "567890123", 
        "datum_isteka_dozvole": "2025-01-01", "kategorije_vozacke_dozvole": "D", 
        "kontakt_informacije": "petar@example.com", "ogranicenja_za_voznju": "Nema", "status": "aktivno"
    }
]

# Testni podaci za radne naloge
radni_nalozi = [
    {"vozilo_id": 1, "vozac_id": 1, "opis_zadatka": "Transport robe", "datum_i_vrijeme_izdavanja": "2024-01-01T08:00:00", "rok_zavrsavanja": "2024-01-01T18:00:00", "status": "otvoren"},
    {"vozilo_id": 2, "vozac_id": 2, "opis_zadatka": "Prevoz putnika", "datum_i_vrijeme_izdavanja": "2024-01-02T08:00:00", "rok_zavrsavanja": "2024-01-02T18:00:00", "status": "otvoren"},
    {"vozilo_id": 3, "vozac_id": 3, "opis_zadatka": "Hitna dostava", "datum_i_vrijeme_izdavanja": "2024-01-03T08:00:00", "rok_zavrsavanja": "2024-01-03T18:00:00", "status": "otvoren"},
    {"vozilo_id": 4, "vozac_id": 1, "opis_zadatka": "Servis vozila", "datum_i_vrijeme_izdavanja": "2024-01-04T08:00:00", "rok_zavrsavanja": "2024-01-04T18:00:00", "status": "otvoren"},
    {"vozilo_id": 5, "vozac_id": 2, "opis_zadatka": "Dostava hrane", "datum_i_vrijeme_izdavanja": "2024-01-05T08:00:00", "rok_zavrsavanja": "2024-01-05T18:00:00", "status": "otvoren"},
    {"vozilo_id": 1, "vozac_id": 3, "opis_zadatka": "Prevoz materijala", "datum_i_vrijeme_izdavanja": "2024-01-06T08:00:00", "rok_zavrsavanja": "2024-01-06T18:00:00", "status": "otvoren"},
    {"vozilo_id": 2, "vozac_id": 1, "opis_zadatka": "Prevoz robe", "datum_i_vrijeme_izdavanja": "2024-01-07T08:00:00", "rok_zavrsavanja": "2024-01-07T18:00:00", "status": "otvoren"},
    {"vozilo_id": 3, "vozac_id": 2, "opis_zadatka": "Turistička tura", "datum_i_vrijeme_izdavanja": "2024-01-08T08:00:00", "rok_zavrsavanja": "2024-01-08T18:00:00", "status": "otvoren"},
    {"vozilo_id": 4, "vozac_id": 3, "opis_zadatka": "Službeni put", "datum_i_vrijeme_izdavanja": "2024-01-09T08:00:00", "rok_zavrsavanja": "2024-01-09T18:00:00", "status": "otvoren"},
    {"vozilo_id": 5, "vozac_id": 1, "opis_zadatka": "Prevoz opreme", "datum_i_vrijeme_izdavanja": "2024-01-10T08:00:00", "rok_zavrsavanja": "2024-01-10T18:00:00", "status": "otvoren"}
]

# Funkcija za popunjavanje vozila
def populate_vozila():
    for vozilo in vozila:
        response = requests.post(f"http://127.0.0.1:8000/api/vozila/", json=vozilo, verify=False)
        if response.status_code == 200 or response.status_code == 201:
            print(f"Uspešno dodato vozilo: {vozilo['marka']} {vozilo['model']}")
        else:
            print(f"Greška pri dodavanju vozila: {response.text}")

# Funkcija za popunjavanje vozača
def populate_vozaci():
    for vozac in vozaci:
        response = requests.post(f"http://127.0.0.1:8000/api/vozaci/", json=vozac, verify=False)
        if response.status_code == 200 or response.status_code == 201:
            print(f"Uspešno dodat vozač: {vozac['ime']} {vozac['prezime']}")
        else:
            print(f"Greška pri dodavanju vozača: {response.text}")

# Funkcija za popunjavanje radnih naloga
def populate_radni_nalozi():
    for nalog in radni_nalozi:
        response = requests.post(f"http://127.0.0.1:8000/api/radni-nalozi/", json=nalog, verify=False)
        if response.status_code == 200 or response.status_code == 201:
            print(f"Uspešno dodat radni nalog za vozilo ID {nalog['vozilo_id']} i vozača ID {nalog['vozac_id']}")
        else:
            print(f"Greška pri dodavanju radnog naloga: {response.text}")


if __name__ == "__main__":
    print("Početak popunjavanja baze podataka...")
    populate_vozila()
    populate_vozaci()
    populate_radni_nalozi()
    print("Popunjavanje baze podataka je završeno.")

