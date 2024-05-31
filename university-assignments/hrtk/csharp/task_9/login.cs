using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using System.Text.RegularExpressions;
using System.Reflection.Emit;

namespace Varich_app1
{
    public partial class VarichD_login : Form
    {
        public VarichD_login()
        {
            InitializeComponent();

            

        }                

        private void button1_Click(object sender, EventArgs e)
        {


            if (loginfield.TextLength == 0)
            {
                label2.ForeColor = Color.Red;
                label2.Text = "Заповніть поле.";
            }
            else if (passfield.TextLength == 0)
            {
                label3.ForeColor = Color.Red;
                label3.Text = "Заповніть поле.";
            }
            


            if (((Regex.Match(loginfield.Text, "^\\+32\\+?-[0-9]{2,2}\\+?-[0-9]{ 3,3}\\+? -[0 - 9]{ 4,4}$").Success) || (Regex.Match(loginfield.Text, " ^\\+32[0 -9]{ 7,14}$").Success) || (Regex.Match(loginfield.Text,"^\\S+\\@ukr\\.net+$").Success)) && Regex.Match(passfield.Text, "(?=.*^[AZ])(?=.*[a-z])(?=.*[0-9]{3,})(?=.*\\d)\\S{6,}$").Success)
             {
                new VarichD_MainForm().Show();
                this.Hide();
            }
             else if ((Regex.Match(loginfield.Text, "^\\+32\\+?-[0-9]{2,2}\\+?-[0-9]{ 3,3}\\+? -[0 - 9]{ 4,4}$").Success) || (Regex.Match(loginfield.Text, " ^\\+32[0 -9]{ 7,14}$").Success) || (Regex.Match(loginfield.Text, "^\\S+\\@ukr\\.net+$").Success))
            {
                label3.ForeColor = Color.Red;
                label3.Text = "Пароль має починатися з великої літери, \nмістити мінімум 3 цифри, та не містити знаків\nпробілів. Довжина паролю мінімум 6 символів. ";

                label2.Text = "";
                
                passfield.Clear();
            }
            else if (Regex.Match(passfield.Text, "(?=.*^[AZ])(?=.*[a-z])(?=.*[0-9]{3,})(?=.*\\d)\\S{6,}$").Success)
            {
                label2.ForeColor = Color.Red;
                label2.Text = "Потрібно ввести мобільний телефон або \nадресу електронної пошти.";

                label3.Text = "";

                loginfield.Clear();
            }
            else if (loginfield.TextLength == 0 && passfield.TextLength == 0)
            {
                
                    label2.ForeColor = Color.Red;
                    label2.Text = "Заповніть поле.";

                    label3.ForeColor = Color.Red;
                    label3.Text = "Заповніть поле.";
                
            }
            else
            {
                label2.ForeColor = Color.Red;
                label2.Text = "Потрібно ввести мобільний телефон або адресу\nелектронної пошти.";

                label3.ForeColor = Color.Red;
                label3.Text = "Пароль має починатися з великої літери, \nмістити мінімум 3 цифри, та не містити знаків\nпробілів. Довжина паролю мінімум 6 символів. ";

                loginfield.Clear();
                passfield.Clear();
            }

        }

      

        private void button2_Click_2(object sender, EventArgs e)
        {
            label3.Text = "";
            passfield.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            loginfield.Clear();
            label2.Text = "";
        }

        private void VarichD_login_Load(object sender, EventArgs e)
        {

        }
    }
}
