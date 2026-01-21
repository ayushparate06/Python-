class Employee:
    """Class to store employee information and calculate salary"""
    
    def __init__(self, name, employee_id, department, basic_salary):
        """
        Initialize employee with basic information
        
        Args:
            name (str): Employee name
            employee_id (str): Employee ID
            department (str): Department name
            basic_salary (float): Basic salary in Rs.
        """
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.basic_salary = basic_salary
    
    def calculate_da(self):
        """Calculate Dearness Allowance (92% of Basic Salary)"""
        return self.basic_salary * 0.92
    
    def calculate_hra(self):
        """Calculate House Rent Allowance (58% of Basic Salary)"""
        return self.basic_salary * 0.58
    
    def calculate_ta(self):
        """Calculate Travel Allowance (30% of Basic Salary)"""
        return self.basic_salary * 0.30
    
    def calculate_lic(self):
        """Calculate LIC Deduction (Rs. 500 fixed)"""
        return 500
    
    def calculate_gross_salary(self):
        """Calculate gross salary (Basic + DA + HRA + TA)"""
        return self.basic_salary + self.calculate_da() + self.calculate_hra() + self.calculate_ta()
    
    def calculate_net_salary(self):
        """Calculate net salary (Gross Salary - LIC)"""
        return self.calculate_gross_salary() - self.calculate_lic()
    
    def display_info(self):
        """Display employee information and salary details"""
        print("=" * 50)
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print("=" * 50)
        print(f"Basic Salary: Rs. {self.basic_salary:,.2f}")
        print(f"DA (92%): Rs. {self.calculate_da():,.2f}")
        print(f"HRA (58%): Rs. {self.calculate_hra():,.2f}")
        print(f"TA (30%): Rs. {self.calculate_ta():,.2f}")
        print("-" * 50)
        print(f"Gross Salary: Rs. {self.calculate_gross_salary():,.2f}")
        print(f"LIC Deduction: Rs. {self.calculate_lic():,.2f}")
        print("-" * 50)
        print(f"Net Salary: Rs. {self.calculate_net_salary():,.2f}")
        print("=" * 50)


def main():
    """Main function to demonstrate employee salary calculation"""
    
    # Example 1: Create an employee
    emp1 = Employee("Rahul Kumar", "EMP001", "IT", 50000)
    emp1.display_info()
    
    print("\n")
    
    # Example 2: Create another employee
    emp2 = Employee("Priya Sharma", "EMP002", "HR", 45000)
    emp2.display_info()
    
    print("\n")
    
    # Example 3: Create an employee with custom input
    print("Enter Employee Details:")
    name = input("Name: ")
    emp_id = input("Employee ID: ")
    department = input("Department: ")
    basic_salary = float(input("Basic Salary (Rs.): "))
    
    emp3 = Employee(name, emp_id, department, basic_salary)
    emp3.display_info()


if __name__ == "__main__":
    main()
