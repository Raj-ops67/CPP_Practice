#include <iostream>
using namespace std;
class Person{
    protected:
    string name;
    int age;
    public:
    void getPersonDetails(){
        cout<<" Enter Name: ";
        cin>>name;
        cout<<"Enter age : ";
        cin>>age;
    }
    void displayPersonDetails(){
         cout<<"--student detail--"<<endl;
        cout<<"Name= "<<name<<endl;
        cout<<"Age= "<<age<<endl;
    }
};
class Student: public Person{
private :
int rollNo;
float marks;
public:
void getStudentDetails(){
getPersonDetails();
cout<<"Enter Roll No: ";
cin>>rollNo;
cout<<"Enter Marks: ";
cin>>marks;
}
void displayStudentDetails(){
    displayPersonDetails();
    cout<<"Roll Number: "<<rollNo<<endl;
    cout<<"Marks: "<<marks<<endl;
}
};
int main(){
    Student s;
    s.getStudentDetails();
    s.displayStudentDetails();
    return 0;
}