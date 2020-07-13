using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Containers;


namespace ToyLanguage.Model.Expressions
{
    public class VariableExpression : IExpression
    {
        private String name;

        public VariableExpression(String name)
        {
            this.name = name;
        }

        public override int Evaluate(MyIDictionary<string, int> symbolTable)
        {
            return symbolTable.Get(name);
        }

        public override string ToString()
        {
            return name;
        }
    }
}