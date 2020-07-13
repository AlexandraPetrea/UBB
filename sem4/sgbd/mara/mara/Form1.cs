using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace mara
{
    public partial class Form1 : Form
    {
        private BindingSource bsUsers, bsPosts;
        private SqlDataAdapter daUsers, daPosts;
        private DataSet ds = new DataSet();
        private SqlCommandBuilder cmdBuilder;
        public Form1()
        {
            InitializeComponent();
        }

        private void GetData()
        {
            String connString = "Server=DESKTOP-5D8G6BA\\SQLEXPRESS;" +
                "Database=bunny;" +
                "Trusted_Connection=True";

            SqlConnection dbConn = new SqlConnection(connString);

            daUsers = new SqlDataAdapter("SELECT * FROM Bunny", dbConn);
            daUsers.Fill(ds, "Bunny");
            bsUsers = new BindingSource(ds, "Bunny");
            daPosts = new SqlDataAdapter("SELECT * FROM Easter", dbConn);
            daPosts.Fill(ds, "Easter");
            DataRelation dr = new DataRelation("BunnyEaster",
                ds.Tables["Bunny"].Columns["id"],
                ds.Tables["Easter"].Columns["bunny_id"]);
            ds.Relations.Add(dr);
            bsPosts = new BindingSource(bsUsers, "BunnyEaster");
        }

        private void Form1_Load_1(object sender, EventArgs e)
        {
            GetData();
            dgvUsers.DataSource = bsUsers;
            dgvPosts.DataSource = bsPosts;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            cmdBuilder = new SqlCommandBuilder(daPosts);
            daPosts.Update(ds, "Easter");
            MessageBox.Show("Changes saved in the database!");
        }

    }
}