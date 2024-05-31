using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Varich_app1
{
    public partial class VarichD_chart : Form
    {
        public VarichD_chart()
        {
            InitializeComponent();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // comboBox1.Items.AddRange(new string[] { "sinx", "cosx", "y=x", "y=x^2", "k/x"});

        }

        private void VarichD_chart_Load(object sender, EventArgs e)
        {

        }

        private void fileToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void mainFormToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new VarichD_MainForm().Show();
            this.Hide();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bindingSource1_CurrentChanged(object sender, EventArgs e)
        {

        }
    }
}
