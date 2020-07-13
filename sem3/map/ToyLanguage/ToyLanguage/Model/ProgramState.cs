using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using ToyLanguage.Model.Containers;
using ToyLanguage.Model.Statements;
namespace ToyLanguage.Model
{
    public class ProgramState
    {
        private MyIStack<IStatement> executionStack;
        private MyIDictionary<string, int> symbolTable;
        private MyIList<int> outputList;
        private MyIDictionary<int, Tuple<string, TextReader>> fileTable;

        public ProgramState(IStatement statement)
        {
            executionStack = new MyIStack<IStatement>(new Stack<IStatement>());
            executionStack.Push(statement);
            symbolTable = new MyDictionary<string, int>(new Dictionary<string, int>());
            outputList = new MyList<int>(new List<int>());
            fileTable = new MyDictionary<int, Tuple<string, TextReader>>(new Dictionary<int, Tuple<string, TextReader>>());
        }

        public MyIDictionary<string, int> getSymbolTable()
        {
            return this.symbolTable;
        }

        public MyIDictionary<int, Tuple<string, TextReader>> getFileTable()
        {
            return this.fileTable;
        }

        public MyIList<int> getOutputList()
        {
            return this.outputList;
        }

        public MyIStack<IStatement> getExecutionStack()
        {
            return this.executionStack;
        }
        public override string ToString()
        {
            string ret = "";
            ret += "+++++++++++++PrgState+++++++++++++\n";
            ret += "-------------ExeStack-------------\n";
            ret += this.getExecutionStack().ToString() + "\n";
            ret += "-------------SymTable-------------\n";
            ret += this.getSymbolTable().ToString() + "\n";
            ret += "--------------Output--------------\n";
            ret += this.getOutputList().ToString() + "\n";
          //  ret += "\n";
            return ret;
        }
    }
}