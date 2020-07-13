using System;
using System.Collections.Generic;
using System.Text;
using ToyLanguage.Model.Containers;
using ToyLanguage.Model.Exceptions;

namespace ToyLanguage.Model.Expressions
{
    internal class Arithmetic : IExpression {
        private IExpression e1, e2;
        private char op;

        public Arithmetic(IExpression e1, IExpression e2, char op)
        {
            this.e1 = e1;
            this.e2 = e2;
            this.op = op;
        }

      
        public int Eval(ProgramState program)
        {
            if (op == '+')
                return e1.Eval(program) + e2.Eval(program);
            else if (op == '-')
                return e1.Eval(program) - e2.Eval(program);
            else if (op == '*')
                return e1.Eval(program) * e2.Eval(program);
            else
            if (e2.Eval(program) == 0)
                throw new RuntimeException("Division by 0 exception");
            return e1.Eval(program) / e2.Eval(program);
        }


         public override String ToString()
        {
            return e1.ToString() + " " + op + " " + e2.ToString();
        }
    }
}