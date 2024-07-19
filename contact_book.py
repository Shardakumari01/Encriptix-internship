# project 5- contact book
import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        # Create GUI elements
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = tk.Label(root, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address = tk.Label(root, text="Address:")
        self.label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(root)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_search = tk.Label(root, text="Search by Name or Phone:")
        self.label_search.grid(row=6, column=0, padx=10, pady=5)
        self.entry_search = tk.Entry(root)
        self.entry_search.grid(row=6, column=1, padx=10, pady=5)

        self.button_search = tk.Button(root, text="Search", command=self.search_contact)
        self.button_search.grid(row=7, column=0, columnspan=2, pady=10)

        self.button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.button_update.grid(row=8, column=0, columnspan=2, pady=10)

        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name == "" or phone == "":
            messagebox.showerror("Error", "Name and Phone number are required!")
            return

        if phone in self.contacts:
            messagebox.showerror("Error", "Contact with this phone number already exists!")
            return

        self.contacts[phone] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", "Contact added successfully!")

        # Clear input fields after adding contact
        self.clear_fields()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Message", "No contacts found.")
            return

        contacts_list = ""
        for contact in self.contacts.values():
            contacts_list += f"Name: {contact['Name']}, Phone: {contact['Phone']}\n"
            if contact['Email']:
                contacts_list += f"  Email: {contact['Email']}\n"
            if contact['Address']:
                contacts_list += f"  Address: {contact['Address']}\n"
            contacts_list += "\n"

        messagebox.showinfo("Contacts", contacts_list)

    def search_contact(self):
        search_term = self.entry_search.get()

        if search_term == "":
            messagebox.showerror("Error", "Please enter a name or phone number to search!")
            return

        found_contacts = []
        for contact in self.contacts.values():
            if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                found_contacts.append(contact)

        if not found_contacts:
            messagebox.showinfo("Message", "No matching contacts found.")
        else:
            search_result = ""
            for contact in found_contacts:
                search_result += f"Name: {contact['Name']}, Phone: {contact['Phone']}\n"
                if contact['Email']:
                    search_result += f"  Email: {contact['Email']}\n"
                if contact['Address']:
                    search_result += f"  Address: {contact['Address']}\n"
                search_result += "\n"

            messagebox.showinfo("Search Results", search_result)

    def update_contact(self):
        phone = self.entry_phone.get()

        if phone not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        name = self.entry_name.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        self.contacts[phone]["Name"] = name
        self.contacts[phone]["Email"] = email
        self.contacts[phone]["Address"] = address

        messagebox.showinfo("Success", "Contact updated successfully!")

        # Clear input fields after updating contact
        self.clear_fields()

    def delete_contact(self):
        phone = self.entry_phone.get()

        if phone not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        del self.contacts[phone]
        messagebox.showinfo("Success", "Contact deleted successfully!")

        # Clear input fields after deleting contact
        self.clear_fields()

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_search.delete(0, tk.END)

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
