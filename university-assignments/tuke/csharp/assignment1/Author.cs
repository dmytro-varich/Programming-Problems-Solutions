using System.Text.RegularExpressions;

namespace Assignment1
{
    public class Author
    {
        private string firstName;
        private string lastName;

        public Author(string firstName, string lastName)
        {
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public void SetAuthorName(string firstName, string lastName)
        {
            Regex pattern = new Regex(@"([A-Z])[a-z]+");
            if (pattern.IsMatch(firstName) && pattern.IsMatch(lastName))
            {
                this.firstName = firstName;
                this.lastName = lastName;
            }
        }

        public string GetAuthorName()
        {
            return this.firstName + " " + this.lastName;
        }
    }
}

