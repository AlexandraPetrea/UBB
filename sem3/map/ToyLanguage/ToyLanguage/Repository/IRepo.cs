using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model;

namespace ToyLanguage.Repository
{
    public interface IRepo
    {
        List<ProgramState> GetPrgList();
        void LogPrgStateExec(ProgramState state);
        void SetPrgList(List<ProgramState> prgList);
    }
}