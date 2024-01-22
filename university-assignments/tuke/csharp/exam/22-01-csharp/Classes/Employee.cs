namespace Classes;

public class Employee: IEmployee
{
    private string Name;
    private int Salary; 

    public Employee(string name, int salary)
    {
        Name = name;
        Salary = salary;
    }

    public int GetSalary()   
    {
        return Salary; 
    } 

    public string GetName()
    {
        return Name;
    }
}