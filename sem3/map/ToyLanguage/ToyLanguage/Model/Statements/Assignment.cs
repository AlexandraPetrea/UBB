using System;
using System.Collections.Generic;
using System.Text;
using ToyLanguage.Model.Expressions;

namespace ToyLanguage.Model.Statements
{
    public class Assignment : IStatement
    {
        private string id;
        private IExpression expression;

        public Assignment(string id, IExpression expression)
        {
            this.id = id;
            this.expression = expression;
        }

        public ProgramState Execute(ProgramState state)
        {
            int value = this.expression.Evaluate(state.getSymbolTable());
            state.getSymbolTable().Put(id, value);
            return state;
        }

        public override string ToString()
        {
            return id + " = " + this.expression.ToString();
        }
    }
}