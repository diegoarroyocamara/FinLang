# Generated from FinLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FinLangParser import FinLangParser
else:
    from FinLangParser import FinLangParser

# This class defines a complete generic visitor for a parse tree produced by FinLangParser.

class FinLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FinLangParser#program.
    def visitProgram(self, ctx:FinLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#statement.
    def visitStatement(self, ctx:FinLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#blockStmt.
    def visitBlockStmt(self, ctx:FinLangParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#ifStmt.
    def visitIfStmt(self, ctx:FinLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#whileStmt.
    def visitWhileStmt(self, ctx:FinLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#assignStmt.
    def visitAssignStmt(self, ctx:FinLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#printStmt.
    def visitPrintStmt(self, ctx:FinLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#breakStmt.
    def visitBreakStmt(self, ctx:FinLangParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#leaveStmt.
    def visitLeaveStmt(self, ctx:FinLangParser.LeaveStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#exitStmt.
    def visitExitStmt(self, ctx:FinLangParser.ExitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#AndExpr.
    def visitAndExpr(self, ctx:FinLangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#BoolExpr.
    def visitBoolExpr(self, ctx:FinLangParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#StringExpr.
    def visitStringExpr(self, ctx:FinLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#FloatExpr.
    def visitFloatExpr(self, ctx:FinLangParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#IdExpr.
    def visitIdExpr(self, ctx:FinLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#NonShortAndExpr.
    def visitNonShortAndExpr(self, ctx:FinLangParser.NonShortAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#NonShortOrExpr.
    def visitNonShortOrExpr(self, ctx:FinLangParser.NonShortOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:FinLangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#OrExpr.
    def visitOrExpr(self, ctx:FinLangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#CharExpr.
    def visitCharExpr(self, ctx:FinLangParser.CharExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:FinLangParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#MulDivModExpr.
    def visitMulDivModExpr(self, ctx:FinLangParser.MulDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#NotExpr.
    def visitNotExpr(self, ctx:FinLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#IntExpr.
    def visitIntExpr(self, ctx:FinLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#ParenExpr.
    def visitParenExpr(self, ctx:FinLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:FinLangParser.AddSubExprContext):
        return self.visitChildren(ctx)



del FinLangParser