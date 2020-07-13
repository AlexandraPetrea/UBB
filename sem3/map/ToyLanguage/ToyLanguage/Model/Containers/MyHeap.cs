using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Containers
{
    class MyHeap<T> : MyIHeap<T>
    {
        private Dictionary<int, T> dict;

        public MyHeap()
        {
            dict = new Dictionary<int, T>();
        }

        public T Get(int key)
        {
            T result = default(T);
            dict.TryGetValue(key, out result);
            return result;
        }

        public int Put(int key, T value)
        {
            dict.Add(key, value);
            return key;
        }
    }
}