using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;


namespace lab1
{
    public partial class Form1 : Form
    {
        private DataSet dataset;
        private SqlDataAdapter agencyAdapter;
        private SqlDataAdapter agentsAdapter;

        public Form1()
        {
            InitializeComponent();
            fillData();
        }

        private string getConnectionString()
        {
            return "Data Source=DESKTOP-5D8G6BA\\SQLEXPRESS;" +
                   "Initial Catalog=SecretServices;" +
                   "Integrated Security = true;";
        }

        private void fillData()
        {
            agencyAdapter = new SqlDataAdapter("select * from Agencies", getConnectionString());
            agentsAdapter = new SqlDataAdapter("select * from Agents", getConnectionString());

            dataset = new DataSet();

            agencyAdapter.Fill(dataset, "Agencies");
            agentsAdapter.Fill(dataset, "Agents");

            dataset.Relations.Add(new DataRelation("Relation", dataset.Tables["Agencies"].Columns["Agency_id"], dataset.Tables["Agents"].Columns["Agency_id"]));
            this.dataGridView1.DataSource = dataset.Tables["Agencies"];
            this.dataGridView2.DataSource = this.dataGridView1.DataSource;
            this.dataGridView2.DataMember = "Relation";

           
        }

        private void refreshButton_Click(object sender, EventArgs e)
        {
            try
            {
                SqlCommandBuilder cmdbl = new SqlCommandBuilder(agentsAdapter);
                agentsAdapter.Update(dataset, "Agents");
                MessageBox.Show("Succes!");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error");
            }
        }


        private void deleteButton_Click(object sender, EventArgs e)
        {
        
            string id =(string)dataGridView2.CurrentRow.Cells[0].Value;
            string agencyId = (string)dataGridView1.CurrentRow.Cells[0].Value;

            SqlCommand selectCommand = new SqlCommand("SELECT * FROM Agents WHERE Agency_id = @id", new SqlConnection(getConnectionString()));

            selectCommand.Parameters.AddWithValue("@id", agencyId);

            SqlDataAdapter adapter = new SqlDataAdapter(selectCommand);

            DataSet dataset = new DataSet();

            adapter.Fill(dataset, "Agents");
            dataset.Tables["Agents"].PrimaryKey = new[] { dataset.Tables["Agents"].Columns[0] };
            dataset.Tables["Agents"].Rows.Find(id).Delete();
                
            SqlCommandBuilder objCommandBuilder = new SqlCommandBuilder(adapter);
            adapter.Update(dataset, "Agents");
        }

        private void Form1_Load(object sender, EventArgs e)
        {


        }
    }
}