using System;
using System.IO;
using System.Runtime.CompilerServices;
using System.Text;

Console.OutputEncoding = System.Text.Encoding.UTF8;

//1 - создаем папку
Directory.CreateDirectory(@"C:\Users\admin\Desktop\VARICH");
Console.WriteLine("Папка создана");

// 1 - вывести список

// 1.1
string path = @"C:\Users\admin\Downloads\Учеба Колледж\Word";

string[] files = Directory.GetFiles(path);

Console.WriteLine("Список: ");
int i = 1;

foreach (string file in files)
{
   Console.WriteLine($"{i}: " + file); ;
   i++;
}

// 1.2.1
string folder = @"C:\Users\admin\Desktop\directoryinfo";
Directory.CreateDirectory(folder);
Console.WriteLine("Папка создана");

// 1.2.2
StreamWriter sw = new StreamWriter(folder + "\\List_Files.txt");
Console.WriteLine("Файл создан");
Console.WriteLine("Файл записан");
int n = 1;
sw.WriteLine("Список: ");

foreach (string file in files)
{
   sw.WriteLine($"{n}: " + file); ;
   n++;
}
sw.Close();

// 2
Console.WriteLine("========TASK 2========");
string path2 = @"C:\Users\admin\Desktop\TASK_2";
Directory.CreateDirectory(path2);
Console.WriteLine("Папка создана");
// 2.1
StreamWriter input = new StreamWriter(path2 + "\\input.txt");
Console.WriteLine("Файл создан");

Console.Write("Введите количество столбцов: ");
int size = Convert.ToInt32(Console.ReadLine());

Random r = new Random();
int[] arr = new int[size];

for (int j = 0; j < size; j++)
{

   arr[j] = r.Next(100);
   Console.WriteLine(arr[j]);
   input.WriteLine(arr[j]);
}
input.Close();

// 2.2
StreamWriter output = new StreamWriter(path2 + "\\output.txt");
Console.WriteLine();
string[] read_numbers = File.ReadAllLines(path2 + "\\input.txt");

int max = Convert.ToInt32(read_numbers.Max());
string convert_max = Convert.ToString(max);

Console.WriteLine("Максимальное число: " + max);

output.WriteLine("Максимальное число: " + max);

int k = 0;
foreach (string s in read_numbers)
{
   if (s == convert_max)
   {
       k++;

   }
   Console.WriteLine(s);
   output.WriteLine(s);

}

Console.WriteLine("Количество максимальных элементов:" + k);
output.WriteLine("Количество максимальных элементов: " + k);

Console.WriteLine("Успешно перезаписалось в файл output");
output.Close();


// 3

// 1
StreamWriter task3 = new StreamWriter(@"C:\Users\admin\Desktop\numbers.txt");

Console.WriteLine("Succses!");

int xn = 0;
while (xn < 500)
{

   xn++;
   if (xn == 500)
   {
       task3.Write(xn + "\n");

       break;
   }
   task3.Write(xn + ", ");


}

// 2
Console.WriteLine("\n");
string[] M = { "red", "green", "black", "white", "blue" };

foreach (string item in M)
{
   task3.WriteLine(item);

}
Console.WriteLine("Succses!");


task3.Close();



// 3
StreamReader sr = new StreamReader(@"C:\Users\admin\Desktop\task_3.txt");

string check_length = sr.ReadToEnd();

Console.WriteLine("Размер длины строк: " + check_length.Length);

sr.Close();
