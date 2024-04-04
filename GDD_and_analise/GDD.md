# (STU) THE END
## DISCLAIMER:
- GDD które widzisz to bardzo okrojona wersja mojej oryginalnej wizji która była o wiele bardziej rozbudowana, szczegółowa i napewno ciekawsza.
  Aktualna wersja to tylko opis tego co udało mi się zrobić i co rzeczywiście znajduję się w grze.
  Niestety przez studia i inne obowiązki porzuciłem projekt ale mam plan do niego wrócić w wolnym czasie i dokończyć tak abym był w 100% zadowolony.
  Jeśli więc interesuje Cię pierwotna wizja jaką miałem na tą grę to proszę o kontakt a chętnie się nią podziele.
## STORY:
- Główny bohater wciela się w studenta pierwszego roku informatyki
i próbuje walczyć z przeciwnościami losu.
Na jego drodzę będą stawać wrogowie próbujący pokrzyżować mu plany
ale pomimo braku zaangażowania i ogromnego lenistwa spróbuje stawić im czoła,
żeby w końcu zdać wszystkie semestry i żeby mama była dumna.
## CHARACTERS:
### Postacie przyjazne:
- Postać w którą się wcielamy w grze to zwykły szary student, posiada on takie cechy jak:
    - Zdrowie
    - Wiedza (odpowienik DMG)
    - Spryt (zdolność do uniku podstawowych ataków)
### Przeciwnicy:
- Magistrzy, najczęściej spotykany rodzaj przeciwników.
- Doktorzy Habilitowani, będą to final bossy których będzie można spotkać po przejściu każdego etapu.
## LEVEL/ENVIROMENT DESIGN:
- Gra będzie podzielona na 3 etapy, odpowiadające latom na studiach,
a każdy z etapów będzie zakończony "sesją" (boss),
aby podejść do sesji trzeba będzię przejść przez określoną liczbe pokoi w których mogą
czekać na nas zarówno wrogowie jak i przyjazne jednostki.
 
Lista przedmiotów i przeciwników znajduje się w klasie data.

## GENEROWANIE MAPY
- Do funkcji generowania mapy podajemy 4 główne argumenty:

  - Wysokość.
      
  - Szerokość.
      
  - Liczba pokoi.
      
  - Rozmiar pokoi.
  
  Po wywołaniu funkcji mapa 'wypełaniania jest' ścianami na podaną wysokość i szerokość, następnie umieszany jest pierwszy pokój o podanej przez nas wielkości (zmodyfikowanej o losową wartość).
  Pokoje tak dodają się aż do momentu kiedy powstanie kolizja już z istniejącym pokojem lub do momentu kiedy narysujemy wszystkie wymagane pokoje.
  Jeśli następuje kolizja to zmniejszamy rozmiar pokoju który chcemy ustawić aż do momentu kiedy nie będzie kolizji lub kiedy pokój będzie już za mały żeby go wstawiać.
  Po tym wszystkim pokoje łączone są korytarzami do sąsiadujących pokoi.
  (Mapa generowana jest losowo i za każdym razem kiedy zaczynamy grę lub przejdziemy do następnego poziomu)

## GAMEPLAY
- Celem gracza jest przejście przez wszytskie pokoje pokonując przeciwników
nie umierając przy tym.
- Gdy gracz umrze grę trzeba zacząć od nowa ale będzie miał możliwość wzięcia warunku (szybkiego odrodzenia).
Warunek można wziąć maksymalnie 2 razy na etap oraz 5 razy podczas jednej rozgrywki.
- Ważnym elementem gry będzie zbieranie przedmiotów oraz ulepszanie broni co będzie można zrobić po wbiciu lvl.

## COMBAT SYSTEM
Cechami liczącymi się w walce są:
- obrażenia
- punkty życia
- inicjatywa

To kto wykonuje atak jest uzależnione od wartości inicjatywy oraz rzutu 20 ścienną kostką aby nadać temu losowości i niepowtarzalności w wynikach. Następnie liczony jest "attack roll" czyli wartość ataku jednostki która wykonuje atak plus wartość rzutu 20 ścienną kostką, jeśli wartość "attack roll" przekracza np. 16 wtedy atak wykona się i zadane zostaną obrażenia istocie broniącej (dmg jednostki + wartość rzutu 6 ścienną kostką), natomiast jeśli "atak roll" nie przekroczy podanej wartości wtedy istota broniąca się wykona unik.

W późniejszych etapach tworzenia gry dodane zostaną dodatkowe cechy liczące się w walce, to kto wykona pierwszy atak będzie uzależnione od tego kto zainicjował walkę oraz wartość z którą porównujemy "atak roll" będzie zależna od zręczności przeciwnika.

