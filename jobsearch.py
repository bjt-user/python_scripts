import webbrowser

AKTUALITAET = 10  #nur Stellenangebote der letzten 10 Tage anzeigen
ANGEBOTE = 20  #es werden 20 Angebote pro Seite angezeigt

print("Aktualitaet = " + str(AKTUALITAET) + " (kann im Skript geaendert werden)")
print("Angebote pro Seite = " + str(ANGEBOTE) + " (kann im Skript geaendert werden)") 



print("\nAls was moechten Sie sich bewerben?")
was = input()

print("\nWo wollen Sie sich bewerben?")
wo = input()

url = "https://con.arbeitsagentur.de/prod/jobboerse/jobsuche-ui/?was=" + was
url = url + "&wo=" + wo
url = url + "&page=1&size=" + str(ANGEBOTE)
url = url + "&FCT.ANGEBOTSART=ARBEIT&FCT.BEHINDERUNG=AUS&aktualitaet=" + str(AKTUALITAET)

webbrowser.open(url)
