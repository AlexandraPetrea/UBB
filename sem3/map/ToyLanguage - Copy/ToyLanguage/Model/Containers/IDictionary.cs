using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Containers
{
    interface IDictionary<K, V>
    {
        V Get(K key);
        V Put(K key, V value);

        string ToString();
    }
}
