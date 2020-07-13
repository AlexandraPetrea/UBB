using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Statements
{
    public interface IStatement
    {
        string ToString();
        ProgramState Execute(ProgramState state);

    }
}