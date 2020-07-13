using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Deadlock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            ThreadStart deadlock1 = new ThreadStart(Deadlock1);
            ThreadStart deadlock2 = new ThreadStart(Deadlock2);

            Thread d1 = new Thread(deadlock1);
            Thread d2 = new Thread(deadlock2);

            d1.Start();
            d2.Start();
        }

        private void Deadlock2()
        {
            Deadlock("query2", 0);
      
        }

        private void Deadlock1()
        {

            Deadlock("query1", 0);
      
        }

        void Deadlock(String deadlock, int tries)
        {
            SqlConnection connection = new SqlConnection("Data Source=DESKTOP-5D8G6BA\\SQLEXPRESS;Initial Catalog=SecretServices;Integrated Security=True;");
            MessageBox.Show(deadlock + " started!");
            SqlCommand command = new SqlCommand(deadlock, connection);
            connection.Open();
            //command.Connection.Open();
            command.CommandType = CommandType.StoredProcedure;

            int rows_affected = 0;
            try
            {
                tries = tries + 1;
                rows_affected = command.ExecuteNonQuery();
        
            }
            catch (Exception ex)
            {
                MessageBox.Show(deadlock + " failed!");
               // int tries = 1;
                while (rows_affected < 2 && tries < 5)
                {
                  
                    MessageBox.Show(deadlock + " failed! rows affected: " + rows_affected + " tries: " + tries);
                    try
                    {
                        rows_affected = command.ExecuteNonQuery();
                        MessageBox.Show(deadlock + " tries: " + (tries));
                        //MessageBox.Show("Ex message " + ex.Message);
            
                    }
                    catch (Exception exe)
                    {
                        MessageBox.Show(deadlock + " failed!");
                        //  MessageBox.Show("Exe message!!! " + exe.Message);
                        tries = tries + 1;
                        Deadlock(deadlock, tries);
                    }
                 
                }
            }
            MessageBox.Show(deadlock + " done!");
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}