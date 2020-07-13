using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Containers
{
    interface IStack<T>
    {
        bool Empty();
        T Peek();
        T Pop();
        void Push(T item);

        string ToString();
    }
}
