using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Containers;

namespace ToyLanguage.Model.Statements
{
    public class CompoundStatement : IStatement
    {
        private IStatement first;
        private IStatement second;

        public CompoundStatement(IStatement first, IStatement second)
        {
            this.first = first;
            this.second = second;
        }


        public ProgramState Execute(ProgramState state)
        {
            MyIStack<IStatement> stack = state.getExecutionStack();
            stack.Push(second);
            stack.Push(first);
            return null;
        }

        public override string ToString()
        {
            return first.ToString() + "; " + second.ToString();
        }
    }
}