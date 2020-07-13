using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Containers;

namespace ToyLanguage.Model.Statements
{
    internal class Composite : IStatement
    {
        private IStatement first;
        private IStatement second;

        public Composite(IStatement first, IStatement second)
        {
            this.first = first;
            this.second = second;
        }

        public ProgramState Exec(ProgramState state)
        {
            IStack<IStatement> stack = state.ExeStack;
            stack.Push(second);
            stack.Push(first);
            return null;
        }

        public override string ToString()
        {
            return this.first.ToString() + ";\n" + this.second.ToString();
        }
    }
}