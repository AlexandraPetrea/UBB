using System;
using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Model.Commands
{
    class ExitCommand : Command
    {
        public ExitCommand(string key, string description) : base(key, description)
        {
        }

        public override void Execute()
        {
            Environment.Exit(0);
        }
    }
}