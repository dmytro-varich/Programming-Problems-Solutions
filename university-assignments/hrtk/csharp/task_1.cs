//Начальные значения
double h = 0.1, a = 0.4, b = 1.0, y;

Console.WriteLine("|      x     |   y  |"); //заголовок таблицы

//Цикл while
while (a <= b)
{


   y = 1 + Math.Pow(Math.Log(a), 2);  //Лог. выр.
   Console.WriteLine("| {0:f2} | 1.0 | {1:f2} |", a, y); //Вывод
   a += h;  //Шаг цикла 0.1
}


//Изначальные данные
double a = 1.5, b = 1.2, y;

Console.WriteLine("|       x      |   y   |"); //заголовок таблицы

//Цикл for
for (double x = -0.75; x >= -1.5; x -= 0.05)
{
   y = 1.2 * Math.Pow((a - b), 3) * Math.Exp(x * x) + x; //Лог. выр.
   Console.WriteLine("| {0:f2} | -1.5 | {1:f2} |", x, y); //Вывод 
}


//Изначальные значения
double a = 1.7, b = 6.2, xn = 9.2, xk = 0.4, dx = -0.8, y = 0, sum = 1;

Console.WriteLine("|      x     |   y   |"); //заголовок таблицы

//Цикл for
for (double k = 4; k <= 8; sum *= k++)

   //Цикл while
   while (xn >= xk)
   {
       //Условный оператор (а < x < b)
       if ((a < xn) && (xn < b)) y = Math.Pow(a + Math.Pow(Math.Log(xn), 2), 0.33);

       //Условный оператор (x > b)
       if (xn > b) y = Math.Pow(Math.Sin(a - xn), 2) + Math.Pow(Math.Abs(a - b), 0.25);

       //Условный оператор (x < 1.2)
       if (xn < 1.2) y = sum * (10 + Math.Sin(xn) / (k - xn));

       Console.WriteLine("| {0:f2} | 0,4 | {1:f2}  |", xn, y); //Вывод    

       xn += dx; //Шаг 
   }
