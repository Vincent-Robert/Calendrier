## Un calendrier des mesures et chiffres du covid


Overview

Pour éviter de perdre du temps, pour que personne n’ait à le refaire, j'ai rempli un calendrier sous forme d'un csv une ligne une date. Il a vocation à être accessible facilement et son mérite principal est sûrement de synthétiser la chronologie des restrictions liées au covid, qui est fusionnée aux stats de Our World in Data

Fonctionnement

Construction à la main d'un tableau des dates de début et fin des mesures gouvernementales importantes. Concrètement c’est un csv à 3 colonnes et la liste des mesures peut être modifiée/allongée à souhait, si la mesure est en cours alors je ne donne pas de date de fin

Fusion avec le calendrier jour par jour des statistiques importantes venant de Our World in Data. Différentes statistiques peuvent être ajoutées, éliminées ; pour le moment il y a le nombre de vaccinés (>2 doses), le nombre de cas cumulés, le nombre de nouveaux cas pour le jour, le nombre de morts cumulés et le nombre de morts pour le jour, le nombre de patients en soins intensifs, le taux de positivité et l’âge médian des malades

Refresh pour la date du jour en relançant le script

Concernant les mesures restrictives qui prennent la valeur 1 si elles sont appliquées et 0 sinon. J’ai fait des choix logiques, par exemple quand le confinement est strict alors la variable confinement partiel a la valeur 0

Sources

ICU data from European Centre for Disease Prevention and Control (ECDC) for a select number of European countries and government sources for the United Kingdom, the United States, Canada, Israel, Algeria, Switzerland, Serbia, Malaysia

Cases/deaths data COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (JHU)

Vaccination data Mathieu, E., Ritchie, H., Ortiz-Ospina, E. et al. A global database of COVID-19 vaccinations. Nat Hum Behav (2021). https://doi.org/10.1038/s41562-021-01122-8
