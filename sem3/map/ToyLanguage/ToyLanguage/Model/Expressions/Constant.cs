using System;
using System.Collections.Generic;
using System.Text;
using ToyLanguage.Model.Containers;


namespace ToyLanguage.Model.Expressions
{
    public class ConstantExpression : IExpression
    {
        private int value;

        public ConstantExpression(int val)
        {
            this.value = val;
        }

        public override int Evaluate(MyIDictionary<string, int> symbolTable)
        {
            return value;
        }

        public override string ToString()
        {
            return value.ToString();
        }
    }
}