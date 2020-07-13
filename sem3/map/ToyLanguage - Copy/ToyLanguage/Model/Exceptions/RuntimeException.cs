using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Exceptions
{
    class RuntimeException : Exception
    {
        public RuntimeException(string message) : base(message)
        {
        }
    }
}