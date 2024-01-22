using Classes;

// 1
Firm myFirm = new Firm();
IStudent student1 = new Intern("John", 50000);
IEmployee adapter1 = new InternetAdapter(student1);
myFirm.AddPerson(adapter1);

IStudent student2 = new Intern("Alice", 60000);
IEmployee adapter2 = new InternetAdapter(student2);
myFirm.AddPerson(adapter2);

myFirm.SendSalaries();

// 2 
Firm myFirm2 = new Firm();

IEmployee employee1 = new Employee("John", 50000);
IEmployee employee2 = new Employee("Alice", 60000);

myFirm2.AddPerson(employee1);
myFirm2.AddPerson(employee2);

myFirm2.SendSalaries();
