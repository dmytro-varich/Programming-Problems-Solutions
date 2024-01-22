namespace Classes;

public class InternetAdapter: IEmployee
{
    private IStudent student;
    public InternetAdapter(IStudent student)
    {
        this.student = student;
    }

    public string GetName()
    {
        return student.GetName();
    }

    public int GetSalary()
    {
        return student.GetStipend();
    }
    

}