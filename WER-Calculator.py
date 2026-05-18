from jiwer import wer, cer, process_words
import re

def normalize(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^\wæøå\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s).strip()
    return s

ref = normalize('''

Nordmenn er nordlendinger, trøndere, sørlendinger – og folk fra alle de andre regionene. Nordmenn har også innvandret fra Afghanistan, Pakistan og Polen, Sverige, Somalia og Syria.
        Det er ikke alltid så lett å si hvor vi er fra, hvilken nasjonalitet vi tilhører. Det vi kaller hjem, er der hjertet vårt er – og det kan ikke alltid plasseres innenfor landegrenser.
        Nordmenn er jenter som er glad i jenter, gutter som er glad i gutter, og jenter og gutter som er glad i hverandre.
        Nordmenn tror på Gud, Allah, Altet og Ingenting. Nordmenn liker Grieg og Kygo, Hellbillies og Kari Bremnes. Med andre ord: Norge er dere.                
        Norge er oss. Mitt største håp for Norge er at vi skal klare å ta vare på hverandre. At vi skal bygge dette landet videre – på tillit, felleskap og raushet.
 


''')

text = normalize('''

Nordmenn er nordlendinger, trøndere, sørlendinger og folk fra alle andre regioner. Nordmenn er også innvandrere fra Afghanistan, Pakistan og Polen, Sverige, Somalia og Syria. Det er ikke alltid så lett å si hvor vi er fra, hvilken nasjonalitet. Det vi kaller hjem, er der hjertet vårt er. Og det kan ikke alltid plasseres innenfor landegrenser. Nordmenn er jenter som er glad i jenter, gutter som er glad i gutter, og jenter og gutter som er glad i hverandre. Nordmenn tror på Gud, Allah, altet og ingenting. Hellbillies og Kari Bremnes. Med andre ord - Norge er dere. Norge er oss. Mitt største håp for Norge er at vi skal klare å ta vare på hverandre. At vi skal bygge dette landet videre på tillit, fellesskap og raushet.                 
                 
                 
                 
                    ''')


print(wer(ref, text))




