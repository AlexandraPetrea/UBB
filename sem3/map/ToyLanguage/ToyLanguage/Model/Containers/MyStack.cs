using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace ToyLanguage.Model.Containers
{
    public class MyIStack<T> : IStack<T>
    {
        private Stack<T> stk;

        public MyIStack(Stack<T> stk)
        {
            this.stk = stk;
        }

        public bool IsEmpty()
        {
            return this.stk.Count == 0;
        }

        public T Peek()
        {
            return this.stk.Peek();
        }

        public T Pop()
        {
            return this.stk.Pop();
        }

        public void Push(T element)
        {
            this.stk.Push(element);
        }

        public Stack<T> ToStack()
        {
            return this.stk;
        }

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            this.stk.ToList().ForEach(e => sb.Append(e.ToString() + "\n"));
            return sb.ToString();
        }
    }
}