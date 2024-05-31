using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.Button;
using System.Text.RegularExpressions;
using System.Security.Policy;


namespace Varich_app1
{

    public partial class VarichD_MainForm : Form
    {
        public VarichD_MainForm()
        {
            InitializeComponent();
        }

        private void VarichD_MainForm_Load(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            
            if (allow_btn.Text == "Allowed")
            {
                // blocked elements
                row_field.Enabled = false;
                column_field.Enabled = false;
                range_field.Enabled = false;
                start_btn.Enabled = false;
                button3.Enabled = false; // btn_clear
                

                // color btn
                start_btn.BackColor = Color.Gray;
                button3.BackColor = Color.Gray;
                start_btn.ForeColor = Color.White;
                button3.ForeColor = Color.White;

                // show message
                string message = "YOU LOCKED THE INPUT FIELDS FOR THE ARRAY!";
                string title = "Warning";
                MessageBox.Show(message, title, MessageBoxButtons.OK, MessageBoxIcon.Warning);

                // rename button
                allow_btn.BackColor = Color.Red;
                allow_btn.Text = "Blocked";

                
            }
            else
            {
                // actives elements
                row_field.Enabled = true;
                column_field.Enabled = true;
                range_field.Enabled = true;
                start_btn.Enabled = true;
                button3.Enabled = true; // btn_clear

                // show message
                string message = "YOU UNLOCKED THE INPUT FIELDS FOR THE ARRAY!";
                string title = "Warning";
                MessageBox.Show(message, title, MessageBoxButtons.OK, MessageBoxIcon.Warning);

                // color btn
                start_btn.BackColor = Color.Black;
                button3.BackColor = Color.Black ;
                start_btn.ForeColor = Color.White;
                button3.ForeColor = Color.White;

                // rename button
                allow_btn.BackColor = Color.Green;
                allow_btn.Text = "Allowed";
                
            }
            


             
        }

        private void row_field_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void column_field_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void range_field_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void start_btn_Click(object sender, EventArgs e)
        {
            int row = 0, column = 0, range = 0;
            Random r = new Random();

            row = Convert.ToInt32(row_field.Text);
   
            column = Convert.ToInt32(column_field.Text);
      
            range = Convert.ToInt32(range_field.Text);
            
            

            int[,] array = new int[row, column];

            for (int i = 0; i < row; i++)
            {
                for (int j = 0; j < column; j++)
                {
                    array[i, j] = r.Next(0, range); // random 
                }
            }

            try
            {
                dataGridView1.ColumnCount = column;
                dataGridView1.RowCount = row;

            }
            catch (Exception)
            {
                label6.ForeColor = Color.Red;
                label6.Text = "Error Syntax";
            }

           

            for (int j = 0; j < column; j++)
            {
                dataGridView1.Columns[j].Name = j.ToString();
                dataGridView1.Columns[j].Width = 25;
                dataGridView1.Columns[j].SortMode = DataGridViewColumnSortMode.NotSortable;

            }

            for (int i = 0; i < row; i++)
                for (int j = 0; j < column; j++)
                    dataGridView1.Rows[i].Cells[j].Value = array[i, j].ToString();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {

                // rename 
                checkBox1.Text = "Passive Form";

                
                // Create an instance of a form and assign it the currently active form.
                Form VarichD_MainForm = Form.ActiveForm;

                

                // Loop through all the controls on the active form.
                for (int i = 0; i < VarichD_MainForm.Controls.Count; i++)
                {
                    // Disable each control in the active form's control collection.
                    VarichD_MainForm.Controls[i].Enabled = false;
                    
                }
                checkBox1.Enabled = true;


            }
            else
            {
                

                // rename 
                checkBox1.Text = "Active Form";


                Form VarichD_MainForm = Form.ActiveForm;

                // Loop through all the controls on the active form.
                for (int i = 0; i < VarichD_MainForm.Controls.Count; i++)
                {
                    // Disable each control in the active form's control collection.
                    VarichD_MainForm.Controls[i].Enabled = true;
                }

                checkBox1.Enabled = true;

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            new VarichD_chart().Show();
            this.Hide();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void autorizationToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new VarichD_login().Show();
            this.Hide();
        }

        private void chartToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new VarichD_chart().Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            DialogResult rez = MessageBox.Show("Do you really want to clear the data of the array?", "Clear Array Data", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
        
            if (rez == DialogResult.Yes)
            {
                // clear array data
                row_field.Clear();
                column_field.Clear();
                range_field.Clear();
                dataGridView1.Rows.Clear();
                dataGridView1.Columns.Clear();
                dataGridView1.Refresh();

            }
            
        }
    }
}
