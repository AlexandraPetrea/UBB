using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model.Containers;

namespace ToyLanguage.Model.Expressions
{
    interface IExpression
    {
        int Eval(ProgramState state);
       // int eval(MyDictionary<String, int> tbl, MyHeap<int> heap);
        string ToString();
    }

}