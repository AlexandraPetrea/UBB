using System;
using System.Collections.Generic;
using System.Text;
using ToyLanguage.Model.Expressions;

namespace ToyLanguage.Model.Statements
{
    class Assignment : IStatement
    {
        private string var;
        private IExpression exp;
        private string v;
        private Constant constant;

        public Assignment(string var, IExpression exp)
        {
           
            this.var = var;
            this.exp = exp;
        }

        public Assignment(string v, Constant constant)
        {
            this.v = v;
            this.constant = constant;
        }

        public ProgramState Exec(ProgramState state)
        {
            
            int value = exp.Eval(state);
            state.SymTable.Put(var, value);
            Console.WriteLine(value);
            return state;
        }

        public override string ToString()
        {

            return var + "=" + exp.ToString();
        }
    }
}