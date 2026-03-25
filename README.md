# Python och sql

## app.py - Python med mysql och server

Ett grundläggande exempel för hur du kan använda din SQL databas med python.

Du behöver installera mysql-connectorn och dotenv för pythong med pip.
Kopiera sedan .env-example till .env och fyll i värdena.

När du gjort det kan du testköra koden och förhoppningsvis komma åt din databas.

## app-sqlite.py

En app som använder sqlite istället för mysql. Den är enklare att komma igång med eftersom den inte kräver någon databasserver.

För att köra denna så använder vi `setup.py` för att skapa databasen och tabellen. Den skapar detta utifrån `schema.sql` filen. När du kört setup.py så kan du köra app-sqlite.py och se att det fungerar.

För att göra din egen databas så kan du ändra i `schema.sql` och sedan köra `setup.py` igen för att skapa den nya databasen.