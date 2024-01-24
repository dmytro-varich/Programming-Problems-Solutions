using System;


public class Sphere
{
    private int radius;
    private int mass;

    public Sphere(int radius, int mass)
    {
        this.radius = radius;
        this.mass = mass;
    }

    public int GetRadius()
    {
        return radius; 
    }

    public int GetMass()
    {
        return mass; 
    }

    public double GetVolume()
    {
        double x = ((4 * Math.PI * Math.Pow(radius, 3)) / 3);
        return Math.Round(x, 5);
    }

    public double GetSurfaceArea()
    {
        double x = (4 * Math.PI * Math.Pow(radius, 2));
        return Math.Round(x, 5);
    }
  
    public double GetDensity()
    {
        return Math.Round(GetMass() / GetVolume(), 5); 
    }
  
}
