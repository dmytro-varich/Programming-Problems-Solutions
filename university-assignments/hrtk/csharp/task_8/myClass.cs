using System.Data;
using System.Runtime.CompilerServices;

namespace Varich
{
    public static class MyClass
    {
        public static void PrintArray(this int[,] A, int rows, int columns)
        {
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
        public static double LR1(int m, int l1, int l2)           
        {
            
            return Math.Pow(m, 2) + Math.Pow(l1, 2) - Math.Pow(l2, 2);
        }
        public static double LR1(byte m, byte l1, byte l2)
        {

            return Math.Pow(m, 2) + Math.Pow(l1, 2) - Math.Pow(l2, 2);
        }
        public static double LR1(double m, double l1, double l2)
        {

            return Math.Pow(m, 2) + Math.Pow(l1, 2) - Math.Pow(l2, 2);
        }
    }
}
