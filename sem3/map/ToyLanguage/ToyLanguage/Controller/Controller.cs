using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using ToyLanguage.Model;
using ToyLanguage.Model.Statements;
using ToyLanguage.Model.Containers;
using ToyLanguage.Repository;

namespace ToyLanguage.Controller
{
    public class TController
    {

        private IRepo repo;
        public TController(IRepo repo)
        {
            this.repo = repo;
        }

        public void SetMain(ProgramState prgState)
        {
            this.repo.GetPrgList().Clear();
            this.repo.GetPrgList().Add(prgState);
        }

        public ProgramState OneStep(ProgramState prgState)
        {
            MyIStack<IStatement> exeStack = prgState.getExecutionStack();
            if (exeStack.IsEmpty())
                throw new Exception("stack is empty");
            return exeStack.Pop().Execute(prgState);
        }

        public void AllSteps()
        {
            ProgramState prgState = this.repo.GetPrgList().ElementAt(0);
            repo.LogPrgStateExec(prgState);
            while (prgState.getExecutionStack().IsEmpty() == false)
            {
                OneStep(prgState);
                repo.LogPrgStateExec(prgState);
            }
        }
    }
}