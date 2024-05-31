using System.Diagnostics;

Console.Write("Введите кол-во строк: "); 
int size = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите кол-во столбиков: ");
int longs = Convert.ToInt32(Console.ReadLine());

Random r = new Random();

Console.WriteLine();

int[,] A = new int[size, longs]; // Массив А

Console.WriteLine("Двумерный массив А : ");
for (int i = 0; i < size; i++)
{ 
    for (int j = 0; j < longs; j++)
    {
        A[i,j] = r.Next(2, 100); //диапазон рандомных чисел
        Console.Write(A[i,j] + "\t"); //Вывод массива А
    }
    Console.WriteLine();
}

Console.WriteLine("===================СТАТИСТИКА=====================");

int count = 0; 
int prost = A[0, 0];//присвоим переменную
for (int i = 0; i < size; i++)
{
    for (int j = 0; j < longs; j++)
    {
        //Условный оператор, чтобы найти простое число и вывести его
        if (A[i, j] % A[i, j] == 0 && A[i, j] % 1 == 0 &&  A[i, j] % 2 >= 1 && A[i, j] % 3 >= 1 && 
            A[i, j] % 4 >= 1 && A[i, j] % 5 >= 1 && A[i, j] % 6 >= 1 && A[i, j] % 7 >= 1 && A[i, j] % 8 >= 1 && A[i, j] % 9 >= 1 || A[i, j] == 2)
        {
            prost = A[i, j];
            count ++ ;
            
            Console.Write("Простое число: " + prost + "\t");
            
        }
    }
    Console.WriteLine(); 
}
Console.WriteLine("Кол-во простых чисел в массиве A: " + count + "\t");
