import sys
from FinLangVisitor import FinLangVisitor
from memory import Environment

class BreakException(Exception): pass
class LeaveException(Exception): pass
class ExitException(Exception): pass
class RuntimeError(Exception): pass

class Interpreter(FinLangVisitor):
    def __init__(self):
        self.memory = Environment()

    def visitProgram(self, ctx):
        try:
            for s in ctx.statement():
                self.visit(s)
        except ExitException:
            pass
        except LeaveException:
            pass
        except RuntimeError as err:
            print(f"[Errore Runtime]: {err}")

    def visitBlockStmt(self, ctx):
        self.memory.push_scope()
        try:
            for s in ctx.statement():
                self.visit(s)
        except LeaveException:
            # Uscita prematura dal blocco corrente verso il blocco esterno
            pass
        finally:
            self.memory.pop_scope()

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if not isinstance(cond, bool):
            raise RuntimeError("La condizione dell'if deve essere un booleano")
        
        if cond:
            self.visit(ctx.statement(0))
        elif ctx.statement(1):
            self.visit(ctx.statement(1))

    def visitWhileStmt(self, ctx):
        while True:
            cond = self.visit(ctx.expr())
            if not isinstance(cond, bool):
                raise RuntimeError("La condizione del while deve essere un booleano")
            if not cond:
                break
            try:
                self.visit(ctx.statement())
            except BreakException:
                break

    def visitAssignStmt(self, ctx):
        var_name = ctx.ID().getText()
        val = self.visit(ctx.expr())
        self.memory.assign(var_name, val)

    def visitPrintStmt(self, ctx):
        print(self.visit(ctx.expr()))

    def visitBreakStmt(self, ctx):
        raise BreakException()

    def visitLeaveStmt(self, ctx):
        raise LeaveException()

    def visitExitStmt(self, ctx):
        raise ExitException()

    # --- Operatori logici Short-Circuit ---

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        if not isinstance(left, bool):
            raise RuntimeError("Operatore 'and' solo per booleani")
        if not left:
            return False
        right = self.visit(ctx.expr(1))
        if not isinstance(right, bool):
            raise RuntimeError("Operatore 'and' solo per booleani")
        return right

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        if not isinstance(left, bool):
            raise RuntimeError("Operatore 'or' solo per booleani")
        if left:
            return True
        right = self.visit(ctx.expr(1))
        if not isinstance(right, bool):
            raise RuntimeError("Operatore 'or' solo per booleani")
        return right

    # --- Operatori logici Non Short-Circuit (& e |) ---

    def visitNonShortAndExpr(self, ctx):
        # Valuta sempre entrambi i lati prima di decidere
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if not isinstance(left, bool) or not isinstance(right, bool):
            raise RuntimeError("Operatore '&' richiede entrambi gli operandi booleani")
        return left and right

    def visitNonShortOrExpr(self, ctx):
        # Valuta sempre entrambi i lati prima di decidere
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if not isinstance(left, bool) or not isinstance(right, bool):
            raise RuntimeError("Operatore '|' richiede entrambi gli operandi booleani")
        return left or right

    def visitNotExpr(self, ctx):
        val = self.visit(ctx.expr())
        if not isinstance(val, bool):
            raise RuntimeError("Operatore 'not' solo per booleani")
        return not val

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left == right if op == '==' else left != right

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if isinstance(left, bool) or isinstance(right, bool):
            raise RuntimeError("Confronti relazionali non ammessi sui booleani")
        
        op = ctx.op.text
        try:
            if op == '<': return left < right
            if op == '<=': return left <= right
            if op == '>': return left > right
            if op == '>=': return left >= right
        except TypeError:
            raise RuntimeError("Confronto tra tipi non compatibili")

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if isinstance(left, str) and isinstance(right, str) and ctx.op.text == '+':
            return left + right

        if isinstance(left, bool) or isinstance(right, bool):
            raise RuntimeError("Operazione + o - non valida su booleani")

        try:
            return left + right if ctx.op.text == '+' else left - right
        except TypeError:
            raise RuntimeError("Operazione + o - non supportata su questi tipi")

    def visitMulDivModExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if isinstance(left, bool) or isinstance(right, bool):
            raise RuntimeError("Operazioni aritmetiche non valide su booleani")

        op = ctx.op.text
        if op in ('/', '%') and right == 0:
            raise RuntimeError("Divisione o modulo per zero")

        try:
            if op == '*': return left * right
            if op == '/': return left / right
            if op == '%': return left % right
        except TypeError:
            raise RuntimeError("Operazioni aritmetiche solo tra numeri")

    def visitIdExpr(self, ctx):
        return self.memory.get(ctx.ID().getText())

    def visitIntExpr(self, ctx):
        return int(ctx.getText())

    def visitFloatExpr(self, ctx):
        return float(ctx.getText())

    def visitStringExpr(self, ctx):
        return ctx.getText()[1:-1]

    def visitCharExpr(self, ctx):
        return ctx.getText()[1:-1]

    def visitBoolExpr(self, ctx):
        return ctx.getText() == 'true'

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())