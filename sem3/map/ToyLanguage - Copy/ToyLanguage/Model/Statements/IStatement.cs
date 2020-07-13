using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Statements
{
    interface IStatement
    {
        ProgramState Exec(ProgramState state);
        string ToString();
    }
}

