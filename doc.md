# FinLang

DSL imperativo minimale orientato al dominio finanziario e al calcolo di bilanci personali.

---

## 1. Introduzione

FinLang è un Domain Specific Language (DSL) imperativo ideato per semplificare la gestione di calcoli finanziari, piani di accumulo, interessi composti e bilanci personali. Il linguaggio adotta una tipizzazione dinamica per permettere una scrittura snella e priva di ridondanze sintattiche. L'interprete è implementato in Python 3 sfruttando il framework ANTLR4 tramite il pattern Visitor.

Il progetto include il supporto completo per la funzionalità avanzata di **Flusso di Controllo Incondizionato**:
- Valutazione **short-circuit** (`and`, `or`) e valutazione **non short-circuit** (`&`, `|`).
- Comandi per l'uscita prematura: `leave;` per uscire dal blocco corrente ritornando al contesto esterno, ed `exit;` per terminare l'esecuzione dell'intero programma.

---

## 2. Guida Rapida

### Requisiti
- Python 3.9 o superiore
- Runtime ANTLR4 per Python:
```bash
pip install antlr4-python3-runtime==4.13.2
```

### Generazione dell'interprete da grammatica
Dalla root di progetto (`FinLang/`):
```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener FinLang.g4 -o source
```

### Esecuzione di uno script
```bash
python3 source/main.py programs/1_budget.fin
```

### Esempio introduttivo ("Hello World")
```finlang
messaggio = "FinLang pronto all'uso";
print messaggio;
```

---

## 3. Sintassi

### Tipi di dato supportati
Oltre a `Bool` e `String`, FinLang include tre tipi atomici distinti per soddisfare i requisiti minimi:
1. `Int`: numeri interi (es. `10`, `0`, `42`).
2. `Float`: numeri in virgola mobile (es. `150.50`, `0.04`).
3. `Char`: singoli caratteri delimitati da apici singoli (es. `'E'`, `'%'`).
4. `String`: sequenze di caratteri racchiuse tra doppi apici (es. `"Risparmio"`).
5. `Bool`: valori booleani (`true`, `false`).

### Costrutti e Istruzioni
- **Assegnamento:** `nome = espressione;`
- **Blocchi delimitati:** `{ ... }` con visibilità locale.
- **Scelta condizionale:** `if (condizione) statement` oppure `if (condizione) statement else statement`
- **Ciclo iterativo:** `while (condizione) statement`
- **Stampa a terminale:** `print espressione;`
- **Uscita incondizionata:** `leave;` (uscita dal blocco), `break;` (uscita dal ciclo), `exit;` (terminazione programma).

### Operatori ed Espressioni
- **Aritmetici:** `+`, `-`, `*`, `/`, `%`
- **Relazionali:** `==`, `!=`, `<`, `<=`, `>`, `>=`
- **Logici Short-Circuit:** `and`, `or`, `not`
- **Logici Eager (Non Short-Circuit):** `&`, `|`

---

## 4. Semantica

### Gestione dell'Ambiente e Visibilità
La memoria (`memory.py`) è implementata tramite uno stack di ambienti (tabelle di simboli).
All'ingresso in un blocco `{ ... }`, viene aggiunto un nuovo record di attivazione (`push_scope`). Le variabili definite internamente hanno visibilità locale e possono mascherare variabili con lo stesso nome definite in scope più esterni (shadowing). All'uscita dal blocco viene invocato `pop_scope`.

### Flusso di Controllo Incondizionato
1. **Short-Circuit vs Non Short-Circuit:**
   - In `a and b`, se `a` è falso, `b` non viene valutato.
   - In `a or b`, se `a` è vero, `b` non viene valutato.
   - Nelle espressioni con `&` e `|`, entrambi gli operandi vengono sempre valutati prima di calcolare il risultato logico.
2. **Uscita Prematura:**
   - `leave`: interrompe il blocco di codice corrente e restituisce il controllo al blocco racchiudente immediato.
   - `exit`: interrompe istantaneamente l'esecuzione del programma terminando l'interprete.

### Regole di Transizione Operazionale

Valutazione di un blocco di comandi:
$$\text{Block} \frac{-}{(\overline{\sigma}, \{ c \}) \rightarrow (\sigma \cdot \overline{\sigma}, \mathtt{block}(c))} \quad \sigma = \varnothing$$

Uscita da un blocco al termine dei comandi:
$$\text{PopScope} \frac{-}{(\sigma \cdot \overline{\sigma}, \mathtt{block}(\epsilon)) \rightarrow (\overline{\sigma}, \epsilon)}$$

Ciclo While:
$$\text{While} \frac{-}{(\overline{\sigma}, \mathtt{while} \, (e) \, \{ c \}) \rightarrow (\overline{\sigma}, \mathtt{if} \, (e) \, \{ c \,;\, \mathtt{while} \, (e) \, \{ c \} \})}$$

---

## 5. Implementazione

L'interprete estende la classe generata `FinLangVisitor` tramite la classe `Interpreter` in `source/interpreter.py`.

- **Controllo di flusso tramite eccezioni:** I comandi `break`, `leave` ed `exit` alzano eccezioni Python dedicate (`BreakException`, `LeaveException`, `ExitException`). `LeaveException` viene intercettata dal metodo `visitBlockStmt`, permettendo l'uscita anticipata verso lo scope genitore. `ExitException` viene intercettata esclusivamente da `visitProgram` per arrestare l'intera computazione.
- **Gestione degli errori runtime:** Errori come la divisione per zero, l'incompatibilità dei tipi o l'accesso a identificatori non definiti sollevano l'eccezione `RuntimeError`, intercettata a livello globale da `visitProgram` per produrre messaggi diagnostici leggibili a terminale senza causare crash non gestiti.

---

## 6. Programmi di Test

### 1. `programs/1_budget.fin`
Calcolo di entrate, uscite e verifica risparmio.
```text
Totale uscite mese:
860.5
Soldi messi via:
739.5
```

### 2. `programs/2_interessi.fin`
Simulazione calcolo rendimento con ciclo `while` e interruzione con `break`.
```text
Mesi impiegati:
15
Saldo raggiunto:
900.4717527534577
```

### 3. `programs/3_short_circuit.fin`
Verifica di `and`/`or` short-circuit, operatori `&`/`|` eager, e comandi `leave` ed `exit`.
```text
Short-circuit su AND: OK
Short-circuit su OR: OK
Operatori non short-circuit (& e |): OK
Entrato nel blocco locale
Uscita dal blocco con leave riuscita: OK
```

### 4. `programs/4_errori.fin`
Intercettazione controllata degli errori a tempo d'esecuzione.
```text
[Errore Runtime]: Divisione o modulo per zero
```