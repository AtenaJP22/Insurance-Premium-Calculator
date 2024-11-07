# Author: Atena Jafari Parsa - 2101183
# Date: 2024-11-02
# Course: Advanced Python Programming - AIN3005
# Homework 1: Insurance Premium Calculator
# Description: This program calculates insurance premiums using object-oriented principles.

from typing import List, Optional # Importing List from typing module for storing past policies and Optional for optional arguments when updating customer information

class Policy:
    # Class variable to track the next policy ID
    policy_id_counter = 1
    
    def __init__(self, base_premium: float):
        self.policy_id = Policy.policy_id_counter  # Assign and increment ID-This ensures all the policies have unique IDs
        Policy.policy_id_counter += 1
        self.base_premium = base_premium

    # Default calculate_premium, meant to be overridden
    def calculate_premium(self, age: int, **kwargs) -> float:
        raise NotImplementedError("This method should be implemented in subclasses.")
    
    
# HealthPolicy class
class HealthPolicy(Policy):
    def __init__(self, base_premium: float, has_medical_conditions: bool):
        super().__init__(base_premium)#super() is used to get base_premium from the parent class
        self.has_medical_conditions = has_medical_conditions

    def calculate_premium(self, age: int, **kwargs) -> float:
        premium = self.base_premium
        # Increase premium based on age and medical conditions
        if age > 60: #Seniors are more likely to have health issues
            premium *= 1.5
        if self.has_medical_conditions:#People with medical conditions need medical care to a higher extent
            premium *= 1.3
        return premium

# AutoPolicy class
class AutoPolicy(Policy):
    def __init__(self, base_premium: float, driving_record: str, vehicle_type: str):
        super().__init__(base_premium)
        self.driving_record = driving_record
        self.vehicle_type = vehicle_type

    def calculate_premium(self, age: int, **kwargs) -> float:
        premium = self.base_premium
        driving_record = self.driving_record
        vehicle_type= self.vehicle_type

        # Age-based adjustment
        if age < 25: #Young drivers are usually more prone to accidents
            premium *= 1.5
        elif age > 60: #Senior drivers are also more likely to get into accidents
            premium *= 1.2
        # Driving record adjustment
        if driving_record == "major":
            premium *= 2.0
        elif driving_record == "minor":
            premium *= 1.3
        # Vehicle type adjustment
        if vehicle_type == "luxury":
            premium *= 1.2
        elif vehicle_type == "motorcycle":
            premium *= 1.5
        elif vehicle_type == "SUV":
            premium *= 1.4
        elif vehicle_type == "truck":
            premium *= 1.6
        elif vehicle_type == "other":
            premium *= 1.3
        return premium

# LifePolicy class
class LifePolicy(Policy):
    def __init__(self, base_premium: float, coverage_amount: float):
        super().__init__(base_premium)
        self.coverage_amount = coverage_amount

    def calculate_premium(self, age: int, **kwargs) -> float:
        premium = self.base_premium + (self.coverage_amount * 0.01)
        if age > 65:#Seniors are more likely to have health issues
            premium *= 1.3
        return premium

# Customer class
class Customer:
    # Class variable to track the next customer ID
    customer_id_counter = 1
    
    def __init__(self, name: str, age: int, address: str):
        self.customer_id = Customer.customer_id_counter  # Assign and increment ID
        Customer.customer_id_counter += 1
        self.name = name
        self.age = age
        self.address = address
        self.past_policies: List[Policy] = []

    def add_policy(self, policy: Policy):
        self.past_policies.append(policy)


    def generate_quote(self, policy: Policy) -> None:
        """Generates and displays a quote for the provided policy."""
        # Calculate the premium for the given policy
        premium = policy.calculate_premium(self.age)  # Assuming 'self.age' is accessible
        print(f"\nEstimated premium for {policy.__class__.__name__} for {self.name}: ${premium:.2f}\n")
        return premium
    
    def view_past_policies(self):
        print(f"\n Viewing the past policies of: {self.name}")
        for policy in self.past_policies:
            print(f"Policy ID: {policy.policy_id}, Type: {policy.__class__.__name__}, Premium: ${policy.calculate_premium(self.age):.2f}")
            
    def remove_policy(self, policy_id: int) -> bool:
        for policy in self.past_policies:
            if policy.policy_id == policy_id:
                self.past_policies.remove(policy)
                print(f"Policy ID {policy_id} has been removed.")
                return True
        print(f"No policy found with ID {policy_id}.")
        return False
    
    def update_customer_info(self, name: Optional[str] = None, age: Optional[int] = None, address: Optional[str] = None):
        """Updates customer information if provided. Ends the method if no fields are provided."""
        if name is None and age is None and address is None:
            print("No chosen field to be updated")
            return
        
        if name:
            self.name = name
        if age:
            self.age = age
        if address:
            self.address = address
        print(f"Customer information updated: {self.name}, Age: {self.age}, Address: {self.address}")
        
    
 #Unit test cases are written in the test_2101183_hw1.py file.
 #The main program is used to create a user-friendly interface for the user to interact with the program through the console. 
 
 # This task was not required in the homework description.
if __name__ == "__main__":
        
    print("\nWelcome to the Insurance Premium Calculator!\n")
        
    while True:
        print("Would you like to 1. add and calculate your insurance premium or 2. view and manage past policies? (1/2)\n")
        user_input = input().upper()
        while user_input not in ["1", "2"]:
            print("Invalid input. Please enter 1 or 2.")
            user_input = input().upper()
        if user_input=="1":
            print("Please enter your name: ")
            name = input()
            while not name.isalpha():
                print("Invalid name. Please enter a valid name.")
                name = input()
            print("Please enter your age: ")
            age = input()
            while not age.isnumeric() or int(age) not in range(4, 120):
                print("Invalid age. Please enter a valid numerical age.")
                age = input()
            age = int(age)
            print("Please enter your address: ")
            address = input()
            customer = Customer(name, age, address)
            print(f"\nHello {name}! What type of policy would you like to calculate the premium for?\n")
            print("1. Health Policy\n")
            print("2. Auto Policy\n")
            print("3. Life Policy\n")
            policy_choice = input()
            while not policy_choice.isnumeric() or int(policy_choice) not in range(1, 4):
                print("Invalid choice. Please enter a number between 1 and 3.")
                policy_choice = input()
            policy_choice = int(policy_choice)
            if policy_choice == 1:
                print("\nDo you have any medical conditions? (Y/N)\n")
                medical_conditions = input()
                while medical_conditions not in ["Y", "N", "y", "n"]:
                    print("Invalid input. Please enter Y or N.")
                    medical_conditions = input()
                medical_conditions = medical_conditions.upper()
                if medical_conditions == "Y":
                    has_medical_conditions = True
                else:
                    has_medical_conditions = False
                policy = HealthPolicy(base_premium=100, has_medical_conditions=has_medical_conditions)
                customer.add_policy(policy)
                customer.generate_quote(policy)
            elif policy_choice == 2:
                print("\nPlease enter your driving record (major/minor/none):\n")
                driving_record = input()
                while driving_record not in ["major", "minor", "none"]:
                    print("Invalid input. Please enter major, minor, or none.")
                    driving_record = input()
                print("\nPlease enter your vehicle type (luxury/motorcycle/SUV/truck/other):\n")
                vehicle_type = input()
                while vehicle_type not in ["luxury", "motorcycle", "SUV", "truck", "other"]:
                    print("Invalid input. Please enter luxury, motorcycle, SUV, truck, or other.")
                    vehicle_type = input()
                policy = AutoPolicy(base_premium=100, driving_record=driving_record, vehicle_type=vehicle_type)
                customer.add_policy(policy)
                customer.generate_quote(policy)
            elif policy_choice == 3:
                print("Please enter the coverage amount(numerical): ")
                coverage_amount = input()
                while not coverage_amount.isnumeric():
                    print("Invalid input. Please enter a valid coverage amount( numerical ).")
                    coverage_amount = input()
                coverage_amount = float(coverage_amount)#After checking if the input is numeric, we convert it to a float to prevent errors
                policy = LifePolicy(base_premium=100, coverage_amount=coverage_amount)
                customer.add_policy(policy)
                customer.generate_quote(policy)
        if user_input=="2":
            print("Please enter your name: ")
            name = input()
            while not name.isalpha():
                print("Invalid name. Please enter a valid name.")
                name = input()
            print("Please enter your age: ")
            age = input()
            while not age.isnumeric() or int(age) not in range(4, 120):
                print("Invalid age. Please enter a numerical valid age.")
                age = input()
            age = int(age)
            print("Please enter your address: ")
            address = input()
            customer = Customer(name, age, address)
            print(f"\nHello {name}! What would you like to do?\n")
            print("1. View past policies\n")
            print("2. Remove a policy\n")
            print("3. Update customer information\n")
            choice = input()
            while not choice.isnumeric() or int(choice) not in range(1, 4):
                print("Invalid choice. Please enter a number between 1 and 3.")
                choice = input()
            choice = int(choice)
            if choice == 1:
                customer.view_past_policies()
            elif choice == 2:
                print("Please enter the ID of the policy you would like to remove: ")
                policy_id = input()
                while not policy_id.isnumeric():
                    print("Invalid ID. Please enter a  numerical valid ID.")
                    policy_id = input()
                policy_id = int(policy_id)
                customer.remove_policy(policy_id)
            elif choice == 3:
                print("Would you like to update your name, age, or address? (name/age/address)\n")
                field = input()
                while field not in ["name", "age", "address"]:
                    print("Invalid choice. Please enter name, age, or address.")
                    field = input()
                if field == "name":
                    print("Please enter your new name: ")
                    new_name = input()
                    while not new_name.isalpha():
                        print("Invalid name. Please enter a valid name.")
                        new_name = input()
                    customer.update_customer_info(name=new_name)
                elif field == "age":
                    print("Please enter your new age: ")
                    new_age = input()
                    while not new_age.isnumeric() or int(new_age) not in range(4, 120):
                        print("Invalid age. Please enter a numerical valid age.")
                        new_age = input()
                    new_age = int(new_age)
                    customer.update_customer_info(age=new_age)
                elif field == "address":
                    print("Please enter your new address: ")
                    new_address = input()
                    customer.update_customer_info(address=new_address)
            else:
                print("Invalid choice. Please try again.")
                
        print("\nWould you like to perform another action? (Y/N)\n")
        repeat = input()
        while repeat not in ["Y", "N", "y", "n"]:
            print("Invalid input. Please enter Y or N.")
            repeat = input()
        repeat = repeat.upper()
        if repeat == "N":
            print("\nThank you for using the Insurance Premium Calculator! Goodbye!\n")
            break
        else:
            continue
       
  