using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Containers
{
    interface IFileTable<T>
    {
        int Put(T value);
        T Get(int key);
        void Remove(int key);

        string ToString();
    }
}
