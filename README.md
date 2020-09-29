## VÄLKOMMEN TILL BIBLIOTEKET

Kör igång programmet med **python.py** 
   -Library klassen initieras
   -vid avslut körs koden i den här filen, som sparar listorna i csv format

**klasser.py** har 
   -funktionen som hanterar val från menyval, tar emot användarens input för resp. media
   -funktionen som lägger till (efter att objektet har skapats) objektet i listan som är i fråga.
   -funktion som sorterar och skriver ut listorna
   -funktion som räknar ut angivna cdns värde

**klasser_2.py**
   -klasserna Book, Cd och Movie som skapar objekt och
   -__repr__ för utskriftsformat

**funktioner.py**
   -funktioner som räknar ut:
      -ålder för objekten
      -värden för objekten

1. Kör igång programmet i filen python.py

2. Om det finns filer sparade sen innan laddas de in *annars* 
   visas en utskrift på att filen inte gick att hitta.

3. Du knappar in det alternativet du vill utifrån det menyvalet visar
   * Mata in en ny bok
   * Mata in en ny skiva
   * Mata in en ny film
   * Skriv ut listan som finns. Om filer fanns sedan tidigare, kommer de också att skrivas ut.
   * Avslut med att trycka på '0'

4. Vid avslut, sparas alla värden - även det som laddades in i början (förutsatt det fanns något att ladda in)