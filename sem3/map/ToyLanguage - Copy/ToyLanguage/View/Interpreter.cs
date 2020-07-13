using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model;
using ToyLanguage.Model.Statements;
using ToyLanguage.Model.Expressions;
using ToyLanguage.Model.Commands;

using ToyLanguage.Repository;
using ToyLanguage.Controller;

namespace ToyLanguage.View
{
    class Interpreter
    {
        static void Main(string[] args)
        {
           // ToyProgram prg1 = new ToyProgram(new Composite( nPrint(new Constant(2)));
            
            ToyProgram prg1 = new ToyProgram(
                   new Composite(
                           new Assignment(
                                   "v",
                                   new Constant(2)
                           ),
                           new Print(
                                   new Variable("v")
                           )
                   )
           );
           

            Repo repo1 = new Repo(prg1, "prg1.txt");
            TController ctrl1 = new TController(repo1);


            ToyProgram prg2 = new ToyProgram(
                    new Composite(
                        new Assignment(
                                "a",
                                new Arithmetic(
                                        new Constant(2),
                                        new Constant(2), '-'
                                )
                        ),
                        new Composite(
                                new If(
                                        new Variable("a"),
                                        new Assignment(
                                                "v",
                                                new Constant(2)),
                                        new Assignment(
                                                "v",
                                                new Constant(3)
                                        )
                                ),
                                new Print(
                                        new Variable("v")
                                )
                        )
                    )
            );

            Repo repo2 = new Repo(prg2, "prg2.txt");
            TController ctrl2 = new TController(repo2);


            ToyProgram prg3 = new ToyProgram(
                    new Composite(
                        new Assignment(
                                "a",
                                new Arithmetic(
                                        new Constant(2),
                                        new Arithmetic(
                                                new Constant(3),
                                                new Constant(5), '+'
                                        ),
                                        '+')
                        ),
                        new Composite(
                                new Assignment(
                                        "b",
                                        new Arithmetic(
                                                new Variable("a"),
                                                new Constant(1), '+'
                                        )
                                ),
                                new Print(
                                        new Variable("b")
                                )
                        )
                    )
            );

            Repo repo3 = new Repo(prg3, "prg3.txt");
            TController ctrl3 = new TController(repo3);

            TextMenu textMenu = new TextMenu();
            textMenu.AddCommand(new ExitCommand("exit", "exit the interpreter"));
            textMenu.AddCommand(new RunExample("1", "run program 1", ctrl1));
            textMenu.AddCommand(new RunExample("2", "run program 2", ctrl2));
            textMenu.AddCommand(new RunExample("3", "run program 3", ctrl3));


            textMenu.Show();


            Console.Write("Press <ENTER> to continue.");
            Console.ReadLine();
        }
    }
}