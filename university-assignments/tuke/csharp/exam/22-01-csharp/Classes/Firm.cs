using System.IO.Pipes;

namespace Classes;

public class Firm
{
     private List<IEmployee> employees;

    public Firm()
    {
        employees = new List<IEmployee>();
    }

    public void AddPerson(IEmployee person)
    {
        employees.Add(person);
    }

    public void SendSalaries()
    {
        foreach (var employee in employees)
        {
            Console.WriteLine($"{employee.GetName()}: {employee.GetSalary()}");
        }
    }
}