using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using ToyLanguage.Model;

namespace ToyLanguage.Repository
{
    public class Repo : IRepo
    {
        private List<ProgramState> list;
        string log;
        public Repo(string log)
        {
            this.list = new List<ProgramState>();
            this.log = log;
        }
        public List<ProgramState> GetPrgList()
        {
            return this.list;
        }

        public void LogPrgStateExec(ProgramState state)
        {
            File.WriteAllText(this.log, state.ToString());
            Console.WriteLine(state.ToString());
        }

        public void SetPrgList(List<ProgramState> prgList)
        {
            this.list = prgList;
        }
    }
}