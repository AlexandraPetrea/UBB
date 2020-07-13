using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Containers;

namespace ToyLanguage.Model.Expressions
{
    public abstract class IExpression
    {
        public abstract int Evaluate(MyIDictionary<string, int> symbolTable);
        public abstract override string ToString();
    }
}