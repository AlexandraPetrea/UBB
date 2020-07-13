using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Controller;

namespace ToyLanguage.Model.Commands
{
    public class RunCommand : Command
    {
        private TController ctr;

        public RunCommand(string key, string desciption, TController ctr) : base(key, desciption)
        {
            this.ctr = ctr;
        }

        public override void Execute()
        {
            try
            {
                ctr.AllSteps();
            }
            catch (Exception exception)
            {
                Console.WriteLine(exception.Message);
            }
        }
    }
}