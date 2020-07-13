using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Repository;
using ToyLanguage.Model.Exceptions;

namespace ToyLanguage.Controller
{
    class TController {
        private Repo repo;
        public string Output { get; set; }

        public TController(Repo repo)
        {
            this.repo = repo;

        }

        public void AllStep()
        {
            try
            {
                while (true)
                {
                    repo.First.OneStep();
                    Output = repo.First.Output;
                }
            }
            catch (RuntimeException)
            {

            }

        }

        public override string ToString()
        {
            return repo.First.ToString();
        }
    }
}