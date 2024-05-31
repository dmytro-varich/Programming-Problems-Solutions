using System;
using System.Globalization;

Console.Write("Введите количество строк: "); 
int size = Convert.ToInt32(Console.ReadLine());

int[] S = new int[size];
Random r = new Random(); 

Console.WriteLine();
Console.WriteLine("Содержимое Матрицы S: ");

for (int i = 0; i < S.Length; i++)
{
    S[i] = r.Next(0, 10);
    Console.Write(S[i] + "\t"); 
}

int[][] M = new int[size][];

for (int i = 0; i < M.Length; i++)
{
    M[i] = new int[S[i]];
}

Console.WriteLine();
Console.WriteLine();
Console.WriteLine("Содержимое Матрицы E: ");

int max = S.Max(); 

int[,] E = new int[size, max];

for (int i = 0; i < size; i++)
{
    for (int j = 0; j < max; j++)
    {
        E[i, j] = r.Next(0, 100);

        Console.Write(E[i, j] + "\t");
    }
    Console.WriteLine();
}

for (int i = 0; i < M.Length; i++)
{
    for (int j = 0; j < M[i].Length; j++)
    {
        M[i][j] = E[i, j];
    }
}

int max_col = M[0].Length;
for (int i = 0; i < M.Length; i++)
{
    if (max_col < M[i].Length)
    {
        max_col = M[i].Length; 
    }
}

Console.WriteLine();

Console.WriteLine("Содержимое Матрицы M: ");
for (int i = 0; i < M.Length; i++)
{
    Console.Write($"i = {i}: \t");
    if (max_col == M[i].Length)
        for (int j = 0; j < M[i].Length; j++)
        {
        
            M[i][j] = 0;

        Console.Write(M[i][j] + "\t");
        }
    else 
        for (int j = 0; j < M[i].Length; j++)
            Console.Write(M[i][j] + "\t");

    Console.WriteLine();
}   
