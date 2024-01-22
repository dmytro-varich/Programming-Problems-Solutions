namespace Classes;

public class Intern: IStudent
{
    private string Name;
    private int Scholarship; 

    public Intern(string name, int scholarship)
    {
        Name = name;
        Scholarship = scholarship;
    }

    public string GetName()
    {
        return Name;
    }

    public int GetStipend()   
    {
        return Scholarship; 
    } 

}