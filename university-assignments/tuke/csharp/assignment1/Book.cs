namespace Assignment1
{
    public class Book
    {
        private string title;
        private int length;
        private Author author;

        public string Title
        {
            get { return title; }
        }

        public Author Author
        {
            get { return author; }
        }

        public Book(string title, int length, string authorName)
        {
            this.title = title;
            this.length = length;
            string[] strlist = authorName.Split(' ', 2);
            Author author = new Author(strlist[0], strlist[1]);
            this.author = author;
        }

        public int GetReadingTime(float minutesPerPage, bool inHours)
        {
            float reading_time = minutesPerPage * this.length;

            if (inHours)
            {
                return (int)Math.Ceiling(reading_time / 60.0f); // time in hours
            }

            return (int)Math.Ceiling(reading_time); // time in minutes
        }

       
    }
}
