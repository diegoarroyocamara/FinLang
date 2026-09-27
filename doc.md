# FinLang

DSL imperativo minimale per il calcolo di spese, budget e piani di accumulo.

## 1. Introduzione

FinLang è pensato per gestire calcoli di bilancio personale senza sintassi inutili. È un linguaggio a tipizzazione dinamica: le variabili non hanno bisogno di dichiarazione di tipo preliminare e vengono risolte direttamente a runtime tramite un interprete basato su Visitor.

## 2. Requisiti e Avvio

- Python 3.9 o superiore
- Runtime ANTLR4: `pip install antlr4-python3-runtime`

## genera parser:
```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener FinLang.g4 -o source

## exec di uno script:
python3 source/main.py programs/1_budget.fin
