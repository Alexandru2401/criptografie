import collections
import string

def analiza_statistica(nume_fisier):
    # 1. Citirea textului
    try:
        with open(nume_fisier, 'r', encoding='utf-8') as f:
            text_brut = f.read()
    except FileNotFoundError:
        print("Eroare: Fișierul nu a fost găsit!")
        return

    # 2. Contorizare total caractere (N) - inclusiv spații/punctuatie conform cerintei
    N_total = len(text_brut)
    print(f"Număr total de caractere (N): {N_total}")

    # 3. Identificarea caracterelor distincte
    caractere_distincte = set(text_brut.lower())
    
    # 4. Definirea alfabetului limbii române (include diacriticele)
    alfabet_ro = set("abcdefghijklmnopqrstuvwxyzăâîșț")
    
    # 5. Compararea cu alfabetul
    litere_text = {c for c in text_brut.lower() if c in alfabet_ro}
    lipsa = alfabet_ro - litere_text
    print(f"Litere din alfabet lipsă în text: {sorted(list(lipsa)) if lipsa else 'Niciuna'}")

    # 6. Numărarea aparițiilor pentru fiecare literă (Na, Nb...)
    # Ne concentrăm doar pe literele din alfabet pentru matricea finală
    aparitii = collections.Counter(text_brut.lower())
    
    # 7 & 8. Calcul frecvențe și Construire Matrice (Model Probabilistic)
    print("\n--- Model Probabilistic (Matricea de frecvențe) ---")
    
    alfabet_ordonat = sorted(list(alfabet_ro))
    linie_litere = []
    linie_frecvente = []

    for litera in alfabet_ordonat:
        n_indice = aparitii[litera]
        frecventa = n_indice / N_total
        
        linie_litere.append(litera)
        linie_frecvente.append(round(frecventa, 6))

    # Afișare sub formă de matrice (tabel)
    print("Litere:    " + " | ".join(linie_litere))
    print("Frecvențe: " + " | ".join(map(str, linie_frecvente)))

    print("Litere:    " + " | ".join(linie_litere))
    print("Frecvențe: " + " | ".join(map(str, linie_frecvente)))
    
    print("Litere:    " + " | ".join(linie_litere))
    print("Frecvențe: " + " | ".join(map(str, linie_frecvente)))



# Execuție
# Asigură-te că ai un fișier numit 'text.txt' în același folder
# analiza_statistica('text.txt')