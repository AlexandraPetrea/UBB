using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Expressions;

namespace ToyLanguage.Model.Statements
{
    public class PrintStatement : IStatement
    {
        IExpression expression;

        public PrintStatement(IExpression expression)
        {
            this.expression = expression;
        }


        public override string ToString()
        {
            return "print( " + expression.ToString() + " )";
        }


        public ProgramState Execute(ProgramState state)
        {
            state.getOutputList().Add(expression.Evaluate(state.getSymbolTable()));
            return state;
        }
    }
}