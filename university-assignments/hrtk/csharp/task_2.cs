using System;
using System.Linq;
using System.Text;
Console.OutputEncoding = System.Text.Encoding.UTF8;

string[] last_name = new string[] { "Андросов", "Диркін", "Дункин", "Петров", "Сидоркін", "Сидоров", "Яблучков" };
bool res;

Console.WriteLine("\t\tВывожу все фамилии");
foreach (string el in last_name) Console.WriteLine(el.ToString());
Console.WriteLine();


do
{
    Console.Write("Введите на какую букву начинается фамилия\n --> ");
    ConsoleKeyInfo x = Console.ReadKey();
    while (!char.IsLetter(x.KeyChar))
    {
        Console.WriteLine();
        Console.Write("Фамилии на такую букву нет\n");
        Console.Write("Введите на какую букву начинается фамилия\n --> ");
        x = Console.ReadKey();
    }

    char first_letter = Convert.ToChar(x.KeyChar);
    res = true;
    Console.WriteLine();


    for (int i = 0; i < last_name.Length; i++)
    {
        if (char.ToUpper(last_name[i].First()) == char.ToUpper(first_letter))
        {
            Console.WriteLine($"\t\tВывожу фамилии после буквы '{char.ToUpper(first_letter)}'");
            for (int k = i; k < last_name.Length; k++)
                Console.WriteLine(last_name[k].ToString());
            res = false;
            break;
        }

    }

    if (res)
    {
        Console.WriteLine("Фамилии на такую букву нет");
    }
} while (res);
