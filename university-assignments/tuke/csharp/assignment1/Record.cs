namespace Assignment1
{
    public class Record
    {
        private Book book;
        private Reader reader;
        private DateTime borrowed;
        private bool returned;

        public Book Book
        {
            get { return book; }
        }

        public Reader Reader
        {
            get { return reader; }

        }

        public bool Returned
        {
            get { return returned; }
            set { returned = value; }
        }

        public Record(Book book, Reader reader, DateTime borrowed)
        {
            this.book = book;
            this.reader = reader;
            this.borrowed = borrowed;
            returned = false;
        }

        public float GetFee(DateTime date)
        {
            float FINE = 5.0f;
            float EXTRA_FINE = 0.1f;

            if (!returned)
            {
                int total_days = (date - borrowed).Days;
                if (total_days > 30)
                {
                    int after_month = total_days / 30;
                    int after_day = total_days % 30;

                    float fee = after_month * FINE + after_day * EXTRA_FINE;
                    return fee;
                }
            }

            return 0.0f;
        }


    }
}
