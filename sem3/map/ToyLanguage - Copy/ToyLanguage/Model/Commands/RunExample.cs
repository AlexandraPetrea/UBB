using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Controller;

namespace ToyLanguage.Model.Commands
{
    class RunExample : Command
    {
        private TController controller;

        public RunExample(string key, string description, TController controller) : base(key, description)
        {
            this.controller = controller;
        }

        public override void Execute()
        {
            try
            {
                Console.WriteLine(controller.ToString());
                
                controller.AllStep();
                Console.WriteLine(controller.Output);
            }
            catch (Exception e)
            {
                
                Console.WriteLine("From RunExample" + e.ToString());
            }
        }
    }
}