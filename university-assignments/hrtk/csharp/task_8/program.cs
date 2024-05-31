using System.Security.Cryptography;
using System;
using System.Text;
using System.Drawing;
using System.Runtime.InteropServices;

Console.OutputEncoding = Encoding.Unicode;
Console.OutputEncoding = System.Text.Encoding.UTF8;

Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("  -------------------      -------------------  ");
Console.WriteLine(" |       MENU        |    | 0 |     EXIT      | ");
Console.WriteLine("  -------------------      -------------------  ");
Console.WriteLine(" | Laboratory work 1 |                          ");
Console.WriteLine("  -------------------                           ");
Console.WriteLine(" | Laboratory work 2 |                          ");
Console.WriteLine("  -------------------                           ");
Console.WriteLine(" | Laboratory work 4 |                          ");
Console.WriteLine("  -------------------                           ");
Console.WriteLine(" | Laboratory work 5 |                          ");
Console.WriteLine("  -------------------                           "); 
Console.WriteLine();
Console.ResetColor();
bool exit = true;

while (exit)
{
    Console.SetCursorPosition(0, 12);
    Console.ForegroundColor = ConsoleColor.Yellow;
    Console.Write(">Please, choose to Laboratory work: ")   ;
    Console.ResetColor();
    Console.ForegroundColor = ConsoleColor.Green;
    int number = int.Parse(Console.ReadLine());
    Console.ResetColor();

    switch (number)
    {
        case 1:
            {
                int m, l1, l2;
                for (int i = 0; i < 22; i++)
                {   
                        Console.WriteLine("                                                                                       ");  
                }
                Console.SetCursorPosition(0, 13);      
                Console.Write("Please, Enter number 'M': ");
                m = int.Parse(Console.ReadLine());
                Console.Write("Please, Enter number 'L1': ");
                l1 = int.Parse(Console.ReadLine());
                Console.Write("Please, Enter number 'L2': ");
                l2 = int.Parse(Console.ReadLine());
                Lr1(m, l1, l2);

                
                break;
            }
        case 2:
            {
                double h, a, b;
                for (int i = 0; i < 22; i++)
                {
                    Console.WriteLine("                                                                                       ");
                }
                Console.SetCursorPosition(0, 13);
                Console.Write("Please, Enter step number 'h': ");
                h = double.Parse(Console.ReadLine());
                Console.Write("Please, Enter start number 'a': ");
                a = double.Parse(Console.ReadLine());
                Console.Write("Please, Enter final number 'b': ");
                b = double.Parse(Console.ReadLine());
                Lr2(h, a, b);
                
                
                break;
            }
        case 4:
            {

                int rows, columns;
                for (int i = 0; i < 30; i++)
                {
                    Console.WriteLine("                                                                                       ");
                }
                Console.SetCursorPosition(0, 13);
                Console.Write("Please, Enter rows: ");
                rows = int.Parse(Console.ReadLine());
                Console.Write("Please, Enter columns: ");
                columns = int.Parse(Console.ReadLine());
                Lr4(rows, columns);
                
                break;
            }
        case 5:
            {
                for (int i = 0; i < 22; i++)
                {
                    Console.WriteLine("                                                                                       ");
                }
                Console.SetCursorPosition(0, 13);
                Console.Write("Enter your Full Name: ");//1
                string? str = Console.ReadLine();
                int l = str.Length;
                Lr5(str);
                
                break;
            }
        case 0:
            {
                for (int i = 0; i < 22; i++)
                {
                    Console.WriteLine("                                                                                       ");
                }
                Console.SetCursorPosition(0, 13);
                exit = false;
                break;
            }
        default:
            {
                for (int i = 0; i < 22; i++)
                {
                    Console.WriteLine("                                                                                       ");
                }
                Console.ForegroundColor = ConsoleColor.Red;
                Console.SetCursorPosition(0, 13);
                Console.WriteLine("Sorry! this Laboratory work doesn't exist.");
                Console.ResetColor();
                break;
            }
            
       
    }
    
    void Lr1(int m, int l1, int l2)
    {
        try
        {
            double p = Math.Pow(m, 2) + Math.Pow(l1, 2) - Math.Pow(l2, 2);
            Console.WriteLine($"Answer: Z = {((m / p) - l1 * p) / (m * l1)}");
            Console.WriteLine($"Answer: Y = {(l2 * Math.Pow(p, 2) * m) / p}");
            
        }
        catch (DivideByZeroException)
        {
            Console.SetCursorPosition(0, 13);
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("ERROR 404");
            Console.ResetColor();
            for (int i = 0; i < 22; i++)
            {
                Console.WriteLine("                                                                                       ");
            }
        }
    }
    
    void Lr2(double h, double a, double b)
    {
        try
        {
            Console.WriteLine();
            Console.WriteLine(" ---------------------");
            while (a <= b)
            {
                double y = 1 + Math.Pow(Math.Log(a), 2);
                a += h;
                Console.WriteLine(" | {0:f2} | {1:f2} | {2:f2} |", a, b, y);
                
            }
            Console.WriteLine(" ---------------------");
            Console.WriteLine();
            
        }
        catch (Exception)
        {
            Console.SetCursorPosition(0, 13);
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("ERROR 404"); 
            Console.ResetColor();
            for (int i = 0; i < 22; i++)
            {
                Console.WriteLine("                                                                                       ");
            }
        }
    }
    void Lr4(int rows, int columns)
    {
        try
        {
            Random r = new Random();

            Console.WriteLine();
            Console.WriteLine("   The Matrix А: "); //Массив А

            int[,] A = new int[rows, columns];
            Console.WriteLine("  ---------------- ");
            for (int i = 0; i < rows; i++)
            {
                Console.Write(" |");
                for (int j = 0; j < columns; j++)
                {
                    A[i, j] = r.Next(0, 100); //Рандомные значения
                    
                    Console.Write(" "+ A[i, j] + " "); //Вывод массива А
                    
                }
                Console.Write("|");                
                Console.WriteLine();
            }
            Console.WriteLine("  ---------------- ");

            Console.WriteLine();
            Console.WriteLine("  -------------------------------------------");
            Console.WriteLine(" |                 STATISTICS                |");
            Console.WriteLine("  -------------------------------------------");

            double sum = 0;

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    sum += A[i, j] / columns; ; //Формула Среднего Арифмитического

                }
                Console.Write(" | Среднее арифметическое " + (i + 1) + " строки равна: " + sum + " |\n");
                sum = 0;
                Console.WriteLine(" --------------------------------------------");
            }           
            Console.WriteLine();
            
           
        }
        catch (IndexOutOfRangeException)
        {
            Console.SetCursorPosition(0, 13);
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("ERROR 404");
            Console.ResetColor();
            for (int i = 0; i < 22; i++)
            {
                Console.WriteLine("                                                                                       ");
            }
        }
    }
    void Lr5(string str)
    {
        try
        {

            Console.WriteLine("Full Name: " + str);

            int l = str.Length;
            Console.WriteLine("String Length: " + l); 

            string[] st = str.Split(' '); 
            string st1 = st[0];
            string st2 = st[1];
            string st3 = st[2];

            int count = 0;
            foreach (var item in str)
            {
                if (str[1] == item)
                {
                    count++;
                }

            }
            Console.WriteLine("Your Last Name - " + st1);
            Console.WriteLine("The second letter of your last name: " + st1[1]);
            Console.WriteLine("Number of letters matching the second letter of the last name: " + (count - 1));

            StringBuilder stb = new StringBuilder(st1 + ' ' + st2); //3
            StringBuilder stb1 = new StringBuilder(st3);

            int n = 0;
            for (int i = 0; i < stb.Length; i++)
            {
                n = i + 1;
                if (n != stb.Length && i != 0)
                {
                    if (stb[n] == ' ')
                    {
                        n += 2;
                        i += 2;

                    }

                }
                if (n == stb.Length)
                {
                    break;
                }


                stb.Insert(n, "-");

                i++;
            }

            char[] holosni = new char[] { 'а', 'у', 'э', 'о', 'и', 'ю', 'е', 'ё', 'ы', 'я' };
            for (int i = 0; i < stb1.Length; i++)
            {
                for (int j = 0; j < holosni.Length; j++)
                {
                    if (stb1[i] == holosni[j])
                    {
                        stb1.Replace(stb1[i], char.ToUpper(stb1[i]));
                    }
                }
            }

            Console.WriteLine("Student group KI-419: " + stb + ' ' + stb1);
            
        }
        catch (FormatException)
        {
            Console.SetCursorPosition(0, 13);
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("ERROR 404");
            Console.ResetColor();
            for (int i = 0; i < 22; i++)
            {
                Console.WriteLine("                                                                                       ");
            }
        }
    }
}
