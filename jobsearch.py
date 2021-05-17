import webbrowser

AKTUALITAET = 10  #Anzahl der Tage, die das Stellenangebot alt sein darf
ANGEBOTE = 20  #Anzahl der Angebote, die pro Seite angezeigt werden

print("Aktualitaet = " + str(AKTUALITAET) + " (kann im Skript geaendert werden)")
print("Angebote pro Seite = " + str(ANGEBOTE) + " (kann im Skript geaendert werden)") 



print("\nAls was moechten Sie sich bewerben?")
was = input()

print("\nWo wollen Sie sich bewerben?")
wo = input()

url = "https://con.arbeitsagentur.de/prod/jobboerse/jobsuche-ui/?was=" + was + "&wo=" + wo
+ "&page=1&size=" + str(ANGEBOTE) + "&FCT.ANGEBOTSART=ARBEIT&FCT.BEHINDERUNG=AUS&aktualitaet=" + str(AKTUALITAET)

webbrowser.open(url)
