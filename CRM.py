import json
import os

class CRM:
    def __init__(self, filename='customers.json'):
        self.filename = filename
        self.customers = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.customers, file, indent=4)

    def add_customer(self, name, email, phone):
        if name in self.customers:
            print("Customer already exists.")
        else:
            self.customers[name] = {
                'email': email,
                'phone': phone,
                'interactions': []
            }
            self.save_data()
            print(f"Customer '{name}' added successfully.")

    def view_customers(self):
        if not self.customers:
            print("No customers found.")
            return
        for name, details in self.customers.items():
            print(f"Name: {name}, Email: {details['email']}, Phone: {details['phone']}, Interactions: {len(details['interactions'])}")

    def delete_customer(self, name):
        if name in self.customers:
            del self.customers[name]
            self.save_data()
            print(f"Customer '{name}' deleted successfully.")
        else:
            print("Customer not found.")

    def log_interaction(self, name, notes):
        if name in self.customers:
            self.customers[name]['interactions'].append(notes)
            self.save_data()
            print(f"Interaction logged for customer '{name}'.")
        else:
            print("Customer not found.")

    def view_interactions(self, name):
        if name in self.customers:
            interactions = self.customers[name]['interactions']
            if interactions:
                print(f"Interactions for '{name}':")
                for i, note in enumerate(interactions, 1):
                    print(f"{i}. {note}")
            else:
                print(f"No interactions found for '{name}'.")
        else:
            print("Customer not found.")

def main():
    crm = CRM()
    
    while True:
        print("\nCRM Menu:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Log Interaction")
        print("5. View Interactions")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            crm.add_customer(name, email, phone)
        elif choice == '2':
            crm.view_customers()
        elif choice == '3':
            name = input("Enter customer name to delete: ")
            crm.delete_customer(name)
        elif choice == '4':
            name = input("Enter customer name for interaction: ")
            notes = input("Enter interaction notes: ")
            crm.log_interaction(name, notes)
        elif choice == '5':
            name = input("Enter customer name to view interactions: ")
            crm.view_interactions(name)
        elif choice == '6':
            print("Exiting CRM.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()