using System.Security.Cryptography;
using System;
using System.Text;
Console.OutputEncoding = Encoding.Unicode;
Console.OutputEncoding = System.Text.Encoding.UTF8;

//the first task 
Console.Write("Введите свое ФИО: ");//1
string? str = Console.ReadLine();

Console.WriteLine("ФИО: " + str);

int l = str.Length;
Console.WriteLine("Длина строки: " + l); //2.1

// ?!
string[] st = str.Split(' '); //Фамилию берем 
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
Console.WriteLine("Ваша фамилия - " + st1);
Console.WriteLine("Вторая буква вашей фамилии: " + st1[1]);
Console.WriteLine("Количество букв совпадающих со второй буквой фамилии: " + (count - 1));

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
Console.WriteLine();

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

Console.WriteLine("Студент групи КІ-419: " + stb + ' ' + stb1);

//the second task
Console.Write("Введите свою фамилию: ");
string? str = Console.ReadLine();
Console.WriteLine("Ваша фамилия: " + str);

int count = 0;
foreach (char item in str)
{
   if ('a' == item)
   {
       count++;
   }
}
Console.WriteLine($"Количество букв - a в фамилии: {count}");


// the third task

Console.Write("Введите что-то в строку S: "); //1
string? s = Console.ReadLine();

// s1
Console.Write("Введите что-то в строку S1: "); //1
string? s1 = Console.ReadLine();

// s2
Console.Write("Введите что-то в строку S2: "); //1
string? s2 = Console.ReadLine();

s = s.Replace(s1, s2);

Console.WriteLine(s);
