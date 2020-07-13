using System;
using System.Collections.Generic;
using System.Text;

using ToyLanguage.Model;
using ToyLanguage.Model.Statements;
using ToyLanguage.Model.Expressions;

using ToyLanguage.Model.Commands;

using ToyLanguage.Model.Containers;

using ToyLanguage.Repository;
using ToyLanguage.Controller;
using static ToyLanguage.Model.Expressions.ArithmeticExpression;

namespace ToyLanguage.View
{
    class Intepreter
    {
        static void Main(string[] args)
        {
            IStatement ex1 = new CompoundStatement(new Assignment("v", new ConstantExpression(2)),
                new PrintStatement(new VariableExpression("v")));

            IStatement ex2 = new CompoundStatement(new Assignment("a",
                new ArithmeticExpression
                (new ConstantExpression(2),
                new ArithmeticExpression(new ConstantExpression(3),
                    new ConstantExpression(5), Operation.MULTIPLY), Operation.ADD)),
                    new CompoundStatement(new Assignment("b", new ArithmeticExpression(new VariableExpression("a"), new
                            ConstantExpression(1), Operation.ADD)), new PrintStatement(new VariableExpression("b"))));

            IStatement ex3 = new CompoundStatement(new Assignment("a",
                new ArithmeticExpression(new ConstantExpression(2),
                new ConstantExpression(2), Operation.SUBTRACT)),
                    new CompoundStatement(new IfStatement(new VariableExpression("a"), new Assignment("v", new ConstantExpression(2)),
                            new Assignment("v", new ConstantExpression(3))), new PrintStatement(new VariableExpression("v"))));

            /*
            IStatement ex4 = new CompoundStatement(new OpenStatement("var_f", "test1.in"),
                    new CompoundStatement(new ReadStatement(new VariableExpression("var_f"), "var_c"),
                            new CompoundStatement(new PrintStatement(new VariableExpression("var_c")),
                                    new CompoundStatement(new IfStatement(new VariableExpression("var_c"),
                                            new CompoundStatement(new ReadStatement(new VariableExpression("var_f"), "var_c"),
                                                    new PrintStatement(new VariableExpression("var_c"))), new PrintStatement(new ConstantExpression(0))),
                                            new CloseStatement(new VariableExpression("var_f"))))));
*/
            TextMenu menu = new TextMenu(new MyDictionary<string, Command>(new Dictionary<string, Command>()));

            menu.AddCommand(new ExitCommand("0", "exit"));
            menu.AddCommand(new RunCommand("1", ex1.ToString(), CreateController(ex1, "log1.txt")));
            menu.AddCommand(new RunCommand("2", ex2.ToString(), CreateController(ex2, "log2.txt")));
            menu.AddCommand(new RunCommand("3", ex3.ToString(), CreateController(ex3, "log3.txt")));
            //menu.AddCommand(new RunCommand("4", ex4.ToString(), CreateController(ex4, "log4.txt")));

            menu.show();
        }

        static TController CreateController(IStatement stmt, string log)
        {
            // if (File.Exists(log))
            {
                //   File.Delete(log);
                //}
                IRepo repo = new Repo(log);
                TController ctrl = new TController(repo);
                ctrl.SetMain(new ProgramState(stmt));
                return ctrl;
            }
        }
    }

}