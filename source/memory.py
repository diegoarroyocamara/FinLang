class Environment:
    def __init__(self):
        # stack dei blocchi: il primo dizionario è lo scope globale
        self.scopes = [{}]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def assign(self, name, value):
        # cerco se la variabile esiste già salendo dallo scope interno
        for s in reversed(self.scopes):
            if name in s:
                s[name] = value
                return
        # se è nuova la creo nel blocco corrente
        self.scopes[-1][name] = value

    def get(self, name):
        for s in reversed(self.scopes):
            if name in s:
                return s[name]
        raise RuntimeError(f"Variabile '{name}' non definita")