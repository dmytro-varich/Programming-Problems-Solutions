namespace Assignment1
{
    public class Reader
    {
        private string name;
        private int readerId;
        private float readingSpeed;
        private List<Record> reads;

        public int ReaderID
        {
            get { return readerId; }
        }

        public Reader(string name, int readerId, float readingSpeed)
        {
            this.name = name;
            this.readerId = readerId;
            this.readingSpeed = readingSpeed;
            reads = new List<Record>();
        }

        public int GetTotalReadingTime()
        {
            int totalReadingTime = 0;

            foreach (var read in reads)
            {
                if(!read.Returned)
                    totalReadingTime += read.Book.GetReadingTime(readingSpeed, false);
            }

            return totalReadingTime;
        }

        public void AddReading(Record record)
        {
            if (record != null && record.Reader == this)
            {
                reads.Add(record);
            }
        }

        public float ReturnBooks(DateTime date)
        {
            float totalFee = 0.0f;

            foreach (var read in reads)
            {
                totalFee += read.GetFee(date);
                read.Returned = true;
            }

            return totalFee;
        }
    }
}
