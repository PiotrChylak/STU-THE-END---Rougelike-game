# (STU) THE END
## STORY:
- Główny bohater wciela się w studenta pierwszego roku informatyki
i próbuje walczyć z przeciwnościami losu.
Na jego drodzę będą stawać wrogowie próbujący pokrzyżować mu plany
ale pomimo braku zaangażowania i ogromnego lenistwa spróbuje stawić im czoła,
żeby w końcu zdać wszystkie semestry i żeby mama była dumna.
## CHARACTERS:
### Postacie przyjazne:
- Postać w którą się wcielamy w grze to zwykły szary student
w zależności od wybranej klasy trochę różniący się wyglądem, cechami charakterystycznymi, atrybutami oraz początkową bronią. Każda z postaci posiada:
    - Zdrowie
    - Wiedza (odpowienik DMG)
    - Spryt (zdolność do uniku podstawowych ataków)

  **Dostępne "klasy" postaci:**
    - technik informatyk:
        - większa bazowa wiedza.
        - większe doświadczenie na start ale też zmniejszony xp z bosów.
        - podstawowy atak to "odór":
            - zadaje dmg wrogom dookoła niego, z początku na małym obszarze.

    - student debil:
        - większy bazowy spryt.
        - podstawowe doświadczenie na start i podstawowy jego przyrost.
        - podstawowy atak to "lanie wody":
            - strzela w Profesorów losowymi słowami zadając im DMG (podstawowy DMG zmniejszony ale może trafić krytycznie).
    - ambitny student:
        - większe bazowe HP
        - mniejsze doświadczenie na start ale więcej XP z bosów.
        - podstawowy atak to "Konsultacje":
            - zadaje Profesorom DMG podchodząc do nich na krótki dystans.
- Pani z żabki w roli handlarza.
- koledzy ze starszego roku którzy działają na zasadzie skrzynki z przedmiotami. Będzie można ich spotkać w "Parku Akademickim".
### Przeciwnicy:
- Magistrzy, najczęściej spotykany rodzaj przeciwników.
- Doktorzy Habilitowani, będą to final bossy których będzie można spotkać po przejściu każdego etapu.
## LEVEL/ENVIROMENT DESIGN:
- Gra będzie podzielona na 6 etapów, odpowiadające semestrom na studiach,
a każdy z etapów będzie zakończony "sesją" (boss),
aby podejść do sesji trzeba będzię przejść przez określoną liczbe pokoi w których mogą
czekać na nas zarówno wrogowie jak i przyjazne jednostki.

- Pokoje będą to (losowo): sale lekcyjne, aule, korytarz, park akademicki oraz żabka.
W salach oraz aulach można znaleźć złoto za które kupimy przedmioty w żabce.

- Po pokonaniu jednego z bosów odblokujemy możliwość wchodzenia do świata funkcji tworzących (podziemia).

- w jednym etapie pojawia się 3 park akademicki, 2 żabka, 7 sala lekcyjna oraz 1 aula na koniec etapu.

- W parku akademickim możesz spotkać kolegę ze starszego roku. Może on ci wręczyć takie przedmioty jak np:
 
    - skrypt profesora pana Kromki (+wiedza)
    - ściąga (+spryt)
    - piwo (+hp)
    - (rzadkie) podrobione zwolnenie lekarskie (daje możliwość ucieczki z jednego pokoju "nie wliczając pokoju z bosem).
    - (rzadkie) zdjęcia egzaminów z tamtego roku 
      (+wiedza, +spryt, +hp)
    - (bardzo rzadkie i jednorozowo) dostęp do tuptupa 
      (++wiedza, ++spryt, ++hp)


- W żabce będzie można kupić takie przedmioty jak np:

    - hot dog (odnawia hp)
    - Monster Energy (chwilowe zwiększenie obrażeń)
    - papierosy (chwilowe zwiększenie sprytu)
(każdego z tych przedmiotów będą różne rodzaje i w zależności od rzadkości będą one dodawły odpowiednio więcej statystyk)

- W salach lekcyjnych spotkamy podstawowych przeciwników natomiast w auli bossy.

- Gra teoretycznie kończy się po przejściu wszytskich etapów (zdaniu studiów) ale wtedy wszystkie pokoje zostą otwarte oraz opustoszałe a gracz dostanie zadanie aby "znaleźć pracę.

- Bronie dostępne do zdobycia:
    - pospolite:
        - myszka na kablu (zadaje obrażenia dookoła bohatera)
        - patchcord (Atakuje poziomo, przechodzi przez wrogów.)
        - kurtka (co jakiś czas zadaje pasywny DMG wszystkim w pokoju)
    - rzadkie:
        - pilot do projektora (na krótko unieruchamia przeciwników)
        - notatki z wykładu (orbitują dookoła postaci)
    - legendarne: 
        - DSM-51 (co jakiś czas uruchamia "brzęczek" który zadaje duże obrażenia w całym pokoju, możliwy do zdobycia tylko po pokonaniu jednego, konkretnego bosa).
    - niespotykanie rzadkie:
        - NAND 5-wejściowy (nikt nie wie co to robi, czy to nawet istnieje?).

## GAMEPLAY
- Celem gracza jest przejście przez wszytskie pokoje pokonując przeciwników
nie umierając przy tym.
- Gdy gracz umrze grę trzeba zacząć od nowa ale będzie miał możliwość wzięcia warunku (szybkiego odrodzenia).
Warunek można wziąć maksymalnie 2 razy na etap oraz 5 razy podczas jednej rozgrywki.
- Ważnym elementem gry będzie zbieranie przedmiotów oraz ulepszanie broni co będzie można zrobić po wbiciu lvl.

# ANALIZA WSTĘPNA ŁOTROPODBNOŚCI:

- Generowanie losowego środowiska [2] (środowisko będzie generowane losowo ale z pewnymi wytycznymi które będą ograniczały tą losowość)
- Trwała śmierć [3] (Trwała śmierć ale będzie możliwość szybkiego odrodzenia po zdobyciu przeznaczoncyh do tego przedmiotów)
- Turowość [3] (Gra będzie przeważnie turowa)
- Plansza, mapa oparta o siatkę [4] (tak)
- Niemodalność [?]
- Złożoność [?]
- Zarządzanie zasobami/ekwipunek [4] (zarządzanie przedmiotami oraz złotem będzie bardzo ważne)
- Walka [4] (główny elemnt gry)
- Eksploracja / Odkrywanie [2] 
 
- Jedne gracz i jedna Postać [4]
- Potwory podobne do bohatera [3]
- Wyzwanie taktyczne [3]
- Wyświetlanie ASCII [4] (gra będzie wyświetlana w ASCII)
- Podziemia [3] (tak, ale mało rozbudowane)
- Liczby [3] (statyski oraz inne)

- Nieliniowość [?]
- Duża zawartość [3] 
- Losowość wyników [2] (obrażenia krtyczne, ilość złota z przeciników, przedmioty dostępne w 'skrzynakch', umiejętności do zdobycia)
- Rozwój bohatera [4] (zwiększanie statystyk, bronie, umiejętności)
- Imersja, Klimat, Atmosfera [4] (orignalna i ciekawa tematyka)
- Ściśle określone warunki zwycięstwa [4] (tak)
