using System.Drawing;

Console.Write("Введите кол-во строк: ");
int size = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите кол-во столбцов: ");
int longs = Convert.ToInt32(Console.ReadLine());

Random r = new Random();

Console.WriteLine();
Console.WriteLine("Массив А: "); //Массив А

int[,] A = new int[size, longs];

for (int i=0; i<size; i++)
{
    for (int j=0; j<longs; j++)
    {
        A[i, j] = r.Next(0, 100); //Рандомные значения
        Console.Write(A[i, j] + "\t"); //Вывод массива А
    }
    Console.WriteLine();
}

Console.WriteLine();
Console.WriteLine("=======================СТАТИСТИКА=============================");

double sum = 0;

for (int i = 0; i < size; i++)
{
    for (int j = 0; j < longs; j++)
    {
        sum += A[i, j] / longs; ; //Формула Среднего Арифмитического

    }
    Console.WriteLine();
    Console.Write("Среднее арифметическое " + (i + 1) + " строки равна: " + sum);
    sum = 0;
}
Console.WriteLine();
