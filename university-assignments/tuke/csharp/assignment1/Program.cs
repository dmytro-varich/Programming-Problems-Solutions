using CsvHelper;
using CsvHelper.Configuration;
using System.Globalization;
using System.Text;

namespace Assignment1
{
    public class Program
    {
        // 1. load from file as a list of records (2p)
        static List<Record> LoadRecords(string path)
        {
            List<Record> records = new List<Record>();
            var config = new CsvConfiguration(CultureInfo.InvariantCulture) { Delimiter = ",", HasHeaderRecord = false };
            using (StreamReader sr = new StreamReader(path, Encoding.UTF8))
            {
                using (CsvReader csv = new CsvReader(sr, config))
                {
                    while (csv.Read())
                    {
                        string author = csv.GetField<string>(0);
                        string title = csv.GetField<string>(1);
                        int pages = csv.GetField<int>(2);
                        Book book = new Book(title, pages, author);
                        Reader reader = new Reader("John", csv.GetField<int>(3), 300);
                        Record record = new Record(book, reader, DateTime.ParseExact(csv.GetField<string>(4), "yyyy-MM-dd", CultureInfo.InvariantCulture));
                        reader.AddReading(record);
                        records.Add(record);
                    }
                }
            }

            return records;
        }

        // 2. find title of most commonly borrowed book from records (0.5p)
        static string FindMostReadBook(string path)
        {
            Dictionary<string, int> bookTittleCounts = new Dictionary<string, int>();
            List<string> mostReadBooks = new List<string>();

            List<Record> records = LoadRecords(path);
            foreach(Record record in records)
            {
                if (bookTittleCounts.ContainsKey(record.Book.Title))
                {
                    bookTittleCounts[record.Book.Title]++;
                }
                else
                {
                    bookTittleCounts[record.Book.Title] = 1;
                }
                
            }

            int maxCount = bookTittleCounts.Values.Max();
            mostReadBooks = bookTittleCounts.Where(kv => kv.Value == maxCount).Select(kv => kv.Key).ToList();

            // return string.Join(", ", mostReadBooks);
            return mostReadBooks[0];
        }

        // 3. find most read author (1p)
        static string FindMostReadAuthor(string path)
        {
            List<string> mostAuthorBooks = new List<string>();
            string[] mostReadBooks = FindMostReadBook(path).Split(", ");
            List<Record> records = LoadRecords(path);

            foreach (Record record in records)
            {
                foreach(string bookTitle in mostReadBooks)
                {
                    if (bookTitle == record.Book.Title)
                    {
                        mostAuthorBooks.Add(record.Book.Author.GetAuthorName());
                    }
                }
                
            }

            //return string.Join(", ", mostAuthorBooks.Distinct());
            return mostAuthorBooks[0];
        }

        // 3. find most avid reader (0.5p)
        static int FindMostAvidReader(string path)
        {
            List<Record> records = LoadRecords(path);
            List<int> mostAvidReader = new List<int>();

            foreach (Record record in records)
            {
                mostAvidReader.Add(record.Reader.ReaderID);
            }

            var grouped = mostAvidReader.GroupBy(x => x);
            var mostPopularReaderID = grouped.OrderByDescending(group => group.Count()).First();
            return mostPopularReaderID.Key;
        }

        // 4. calculate income to a given day (1p)
        static float CalculateIncome(string path, DateTime date)
        {
            float total_income = 0.0f;
            int index = 0;
            List<Record> records = LoadRecords(path);
            List<string> date_returns = new List<string>();
            
            var config = new CsvConfiguration(CultureInfo.InvariantCulture) { Delimiter = ",", HasHeaderRecord = false, MissingFieldFound = null };
            using (StreamReader sr = new StreamReader(path, Encoding.UTF8))
            {
                using (CsvReader csv = new CsvReader(sr, config))
                {
                    while (csv.Read())
                    {
                        string? dateString = csv.GetField<string>(5);
                        date_returns.Add(dateString);
                    }
                }
            }

            foreach (Record record in records)
            {
                if (string.IsNullOrEmpty(date_returns[index]))
                {
                    total_income += record.Reader.ReturnBooks(date);
                }
                else
                {
                    total_income += record.Reader.ReturnBooks(DateTime.ParseExact(date_returns[index], "yyyy-MM-dd", CultureInfo.InvariantCulture));
                }
                index++;
            }

            return total_income;
        }

        static void Main(string[] args)
        {
       
        }
    }
}