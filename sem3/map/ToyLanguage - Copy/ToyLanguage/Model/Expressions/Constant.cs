using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Expressions
{
    internal class Constant : IExpression
    {
        private int value;

        public Constant(int value)
        {
            this.value = value;
        }

        public int Eval(ProgramState state)
        {
            return value;
        }

        public override string ToString()
        {
            return value.ToString();
        }
    }
}