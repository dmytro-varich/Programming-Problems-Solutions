using System.IO;
using System.Text;

namespace Lab02
{
    internal class Program
    {
        static char[,] LoadSudoku(string problem)
        {
            char[,] result = new char[9, 9];
            problem = problem.Replace('0', '.');

            for (int i = 0; i < 81; i++)
            {
                result[i / 9, i % 9] = problem[i]; 
            }

            return result;
        }

        static void PrintSudoku(char[,] grid)
        {
            string line = new String('-', 22);

            Console.WriteLine();
            Console.Write("     ");
            for (int i = 1; i <= 9; i++)
            { 
                Console.Write(i + " ");
                if (i % 3 == 0)
                {
                    Console.Write(" ");
                }

            }

            Console.WriteLine();
            Console.WriteLine("   " + line);
            for (int i = 0; i < 9; i++)
            {
                Console.Write(" " + (i+1) + " |");
                for (int j = 0; j < 9; j++)
                {
                    Console.Write(" ");
                    Console.Write(grid[i, j]);
                    if (j % 3 == 2)
                    {
                        Console.Write("|");
                    }
                }
                Console.WriteLine();
                if (i % 3 == 2)
                {
                    Console.WriteLine("   " + line);
                }
            }
        }

        static bool IsValid(char[,] grid, int row, int col, char value)
        {

            for (int i = 0; i < 9; i++)
            {
                if (grid[row, i] == value) { return false; } // horizontal
                if (grid[i, col] == value) { return false; } // vertical
                if (grid[row / 3 * 3 + i / 3, col / 3 * 3 + i%3] == value) { return false; } // square
            }

            return true;
        }

        static bool SolveSudoku(char[,] grid)
        {          
            for(int i=0; i< 9; i++)
            {
                for(int j=0; j<9; j++)
                {
                        if (grid[i, j] == '.')
                        {
                            for(char k='1'; k<='9'; k++)
                            {
                                if (IsValid(grid, i, j, k))
                                {
                                    grid[i, j] = k;
                                    if (SolveSudoku(grid)) { return true; }
                                    else { grid[i, j] = '.'; }
                                }
                            }
                            return false;
                        }
                }
            }                                                                           
            return true;
        }

        static private char Menu()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.White;
            Console.BackgroundColor = ConsoleColor.Blue;
            Console.WriteLine();
            Console.WriteLine(" +----------------------------------------------------+ ");
            Console.WriteLine(" |  ---   +    +   +---     +-----+   +    +  +    +  | ");
            Console.WriteLine(" | |      |    |   |   \\    |     |   |   /   |    |  | ");
            Console.WriteLine(" |  ---   |    |   |    \\   |     |   |__/    |    |  | ");
            Console.WriteLine(" |     |  |    |   |     \\  |     |   |  \\    |    |  | ");
            Console.WriteLine(" |  ---    ----    +------  +-----+   |   \\    ----   | ");
            Console.WriteLine(" +____________________________________________________+ ");
            Console.WriteLine("                                                        \n");
            Console.ResetColor();

            Console.WriteLine(" Welcome to Sudoku!\n\n");
            Console.WriteLine(" Options:\n  1. Start Game\n  2. Rules\n  3. Quit\n\n");
            Console.Write(" Please select an option : ");

            Console.ForegroundColor = ConsoleColor.Cyan;
            string option = Console.ReadLine().Trim();
            Console.ResetColor();

            while (option.Length > 1) { Console.Clear(); return Menu(); }
            while (option[0] != '1' && option[0] != '2' && option[0] != '3') { Console.Clear(); return Menu(); }

            if (option[0] == '2') { Rules(); return Menu(); }

            return option[0];
        }

        static private void Rules()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine(" +----------------------------------------------------------------------------------------------------------------------+ ");
            Console.WriteLine(" | RULES FOR PLAYING SUDOKU                                                                                             | \n" +
                " |                                                                                                                      | \n" +
                " | 1. The Sudoku playing field is a 9x9 square, divided into 9 3x3 subgrids.                                            | \n" +
                " | 2. The task is to fill each cell so that there are no repeating numbers from 1 to 9 in each row, column and subgrid. | \n" +
                " | 3. The starting position of the game contains several pre-filled cells.                                              | \n" +
                " | 4. The goal is to fill in the remaining cells based on logical reasoning without breaking Sudoku.                    | \n" +
                " |                                                                                                                      | \n" +
                " | How to enter row, col, val correctly?                                                                                | \n" +
                " | For example: 5 6 1                                                                                                   | \n" +
                " |                                                                                                                      | \n" +
                " | *Row - is the row number (horizontal position) in the grid.                                                          | \n" +
                " | *Сol - is the column number (vertical position) in the grid.                                                         | \n" +
                " | *Val - is the value you want to put in the cell with coordinates (row, col).                                         | \n" +
                " |                                                                                                                      | \n" +
                " | ! Remember: The game isn't over until you win, but you can enter 'S' - if you want to finish the game . Goodluck !   | \n" +                                                         
                " +----------------------------------------------------------------------------------------------------------------------+ \n\n");
            Console.ResetColor();
            Console.WriteLine(" Options:\n  1. Back\n\n");
            Console.Write(" Please select an option: ");

            Console.ForegroundColor = ConsoleColor.Cyan;
            string option = Console.ReadLine().Trim();
            Console.ResetColor();

            while ((option.Length > 1 && option[0] != '1') || (option[0] != '1') || (option.Length > 1)) { Rules(); return; }
            return;

        }

        static private void Game(char[,] grid)
        {
            char[] data;
            int row, col;
            char val;
            bool res = false, looser = false;
            string option;

            while (!res)
            {

                try
                {

                    do
                    {
                        Console.Clear();
                        PrintSudoku(grid);
                        Console.WriteLine("\n\n");
                        Console.Write(" Enter row, column, and value: ");
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        data = Console.ReadLine().Split().Select(char.Parse).ToArray();
                        Console.ResetColor();
                        if (data[0] == 'S') { SolveSudoku(grid); looser = true;  res = true; }
                        row = data[0] - '0'; col = data[1] - '0'; val = data[2];
                        if ((row <= 0 && row >= 9) && (col <= 0 && col >= 9) && (val <= '1' && val >= '9'))
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine(" Invalid input :/");
                            Thread.Sleep(1000);
                            Console.ResetColor();
                        }

                    } while ((row <= 1 && row >= 9) && (col <= 1 && col >= 9) && (val < '1' && val > '9') && (grid[row - 1, col - 1] != '.'));

                    if (IsValid(grid, row - 1, col - 1, val))
                    {
                        grid[row - 1, col - 1] = val;

                        char[,] check_grid = new char[9, 9];
                        Array.Copy(grid, check_grid, 9);

                        if (SolveSudoku(check_grid))
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                            Console.WriteLine(" It's Correct!");
                            Thread.Sleep(2000);
                            Console.ResetColor();
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Yellow;
                            Console.WriteLine($" Oops! This position {row}x{col} -> '{val}' is invalid.");
                            Thread.Sleep(2000);
                            Console.ResetColor();
                        }
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine($" Oops! This position {row}x{col} -> '{val}' is invalid.");
                        Thread.Sleep(2000);
                        Console.ResetColor();
                    }

                    char[] end_game_grid = grid.Cast<char>().ToArray();
                    int count = end_game_grid.Count(x => x == '.');
                    if (count == 0) { res = true; }

                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine(" Invalid input :(");
                    Thread.Sleep(1000);
                    Console.ResetColor();
                    Console.Clear();
                    PrintSudoku(grid);
                    Console.WriteLine("\n\n");
                    Console.Write(" Enter row, column, and value: ");
                }

            }

            do
            {
                Console.Clear();
                if (!looser)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    PrintSudoku(grid);
                    Console.WriteLine("\n YOU WON!\n\n");
                }
                else if (looser)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    PrintSudoku(grid);
                    Console.WriteLine("\n YOU LOOSER!\n\n");
                }
                Console.ResetColor();

                Console.WriteLine(" Options:\n  1. Back\n\n");
                Console.Write(" Please select an option : ");

                Console.ForegroundColor = ConsoleColor.Cyan;
                option = Console.ReadLine().Trim();
                Console.ResetColor();

            } while ((option.Length > 1 && option[0] != '1') || (option[0] != '1') || (option.Length > 1));

            return;
        }

        static void Main(string[] args)
        {
            char option;
            string path = "C:\\Users\\admin\\Desktop\\TUKE\\2 kurz\\C#\\Sudoku\\sudokus.txt";
            string[] sudoku = File.ReadAllLines(path);
            do
            {
                Random random = new Random();
                int randomIndex = random.Next(0, sudoku.Length);
                string randomGrid = sudoku[randomIndex];

                char[,] grid = LoadSudoku(randomGrid);

                option = Menu();

                if (option == '1') { Console.Clear(); Game(grid);}
                
            } while (option != '3');

            Console.Clear(); 
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("GoodBye! T_T");
            Thread.Sleep(5000);
            Console.ResetColor();
            Environment.Exit(0); 

        }
    }
}
