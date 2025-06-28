from fastapi import FastAPI
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Inicjalizacja aplikacji FastAPI
app = FastAPI()

# Inicjalizacja stemmera (lematyzatora) dla języka indonezyjskiego
# Ten proces może zająć chwilę przy pierwszym uruchomieniu
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Definiujemy główny endpoint aplikacji
@app.get("/")
def read_root():
    return {"message": "Witaj! To jest API do lematyzacji języka indonezyjskiego. Użyj endpointu /lemmatize"}

# Definiujemy endpoint do lematyzacji
@app.get("/lemmatize")
def lemmatize_word(word: str):
    """
    Przyjmuje słowo jako parametr 'word' i zwraca jego formę podstawową (lemat).
    Przykład użycia: /lemmatize?word=membaca
    """
    if not word:
        return {"error": "Parametr 'word' nie może być pusty."}

    # Używamy stemmera do znalezienia formy podstawowej
    lemma = stemmer.stem(word)

    # Zwracamy wynik w formacie JSON
    return {"original_word": word, "lemma": lemma}

# Definiujemy endpoint do testowania stanu usługi
@app.get("/health")
def health_check():
    return {"status": "ok"}
