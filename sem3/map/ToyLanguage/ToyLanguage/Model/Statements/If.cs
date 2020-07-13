using System;
using System.Collections.Generic;
using System.Text;
using ToyLanguage.Model.Containers;
using ToyLanguage.Model.Expressions;

namespace ToyLanguage.Model.Statements
{
    public class IfStatement : IStatement
    {
        private IExpression expression;
        private IStatement thenStatement;
        private IStatement elseStatement;

        public IfStatement(IExpression expression, IStatement thenStatement, IStatement elseStatement)
        {
            this.expression = expression;
            this.thenStatement = thenStatement;
            this.elseStatement = elseStatement;
        }

        public ProgramState Execute(ProgramState state)
        {
            MyIStack<IStatement> stack = state.getExecutionStack();
            int value = 0;
            value = expression.Evaluate(state.getSymbolTable());
            if (value != 0) stack.Push(thenStatement);
            else stack.Push(elseStatement);
            return state;
        }

        public override string ToString()
        {
            return "if(" + expression.ToString() + ") then " + thenStatement.ToString() + " else " + elseStatement.ToString();
        }
    }
}