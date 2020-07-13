using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Expressions;

namespace ToyLanguage.Model.Statements
{
    class Print : IStatement
    {
        private IExpression exp;

        public Print(IExpression exp)
        {
            this.exp = exp;
        }

        public override string ToString()
        {
            return "print(" + this.exp.ToString() + ")";
        }

        public ProgramState Exec(ProgramState state)
        {
            state.AppendOutput(exp.Eval(state) + "\n");
            return state;
        }
    }
}