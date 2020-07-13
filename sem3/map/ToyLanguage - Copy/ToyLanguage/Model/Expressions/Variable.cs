using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Expressions
{   internal class Variable : IExpression
{
    private string id;

    public Variable(string id)
    {
        this.id = id;
    }

    public int Eval(ProgramState state)
    {
        return state.SymTable.Get(id);
    }

    public override string ToString()
    {
        return id;
    }
}
}