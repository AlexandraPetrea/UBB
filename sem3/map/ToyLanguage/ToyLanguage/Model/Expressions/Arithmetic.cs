using System;
using System.Collections.Generic;
using System.Text;
using ToyLanguage.Model.Containers;
using ToyLanguage.Model.Exceptions;

namespace ToyLanguage.Model.Expressions
{
    public class ArithmeticExpression : IExpression
    {
        public enum Operation
        {
            ADD,
            SUBTRACT,
            MULTIPLY,
            DIVIDE
        }

        private IExpression left;
        private IExpression right;
        Operation op;

        public ArithmeticExpression(IExpression left, IExpression right, Operation op)
        {
            this.op = op;
            this.left = left;
            this.right = right;
        }

        public override int Evaluate(MyIDictionary<string, int> symbolTable)
        {
            int l = this.left.Evaluate(symbolTable);
            int r = this.right.Evaluate(symbolTable);

            int ret = l;
            switch (this.op)
            {
                case Operation.ADD:
                    ret += r;
                    break;
                case Operation.SUBTRACT:
                    ret -= r;
                    break;
                case Operation.MULTIPLY:
                    ret *= r;
                    break;
                case Operation.DIVIDE:
                    if (r == 0)
                        throw new Exception("Division by zero");
                    ret /= r;
                    break;
            }
            return ret;
        }

        public override string ToString()
        {
            string ret = this.left.ToString();

            switch (this.op)
            {
                case Operation.ADD:
                    ret += " + ";
                    break;
                case Operation.SUBTRACT:
                    ret += " - ";
                    break;
                case Operation.MULTIPLY:
                    ret += " * ";
                    break;
                case Operation.DIVIDE:
                    ret += " / ";
                    break;
            }

            ret += this.right.ToString();
            return ret;
        }
    }
}