using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Containers
{
    public interface IStack<T>
    {
        void Push(T element);
        T Pop();
        T Peek();
        bool IsEmpty();
        Stack<T> ToStack();
        string ToString();
}
}
