using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Containers
{
    interface IHeap<T>
    {
        int Put(int key, T value);
        T Get(int key);

        string ToString();
    }
}
