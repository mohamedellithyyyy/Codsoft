import tkinter as tk
from tkinter import messagebox

# Dummy data to simulate contacts
contacts = [
    {"name": "John Doe", "phone": "123-456-7890", "email": "john@example.com", "address": "123 Main St"},
    {"name": "Jane Smith", "phone": "987-654-3210", "email": "jane@example.com", "address": "456 Elm St"}
]

def add_contact():
    # Function to add a new contact
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added successfully")

def view_contacts():
    # Function to display all contacts
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    # Function to search for a contact
    query = entry_search.get()
    found_contacts = [contact for contact in contacts if query in contact["name"] or query in contact["phone"]]
    contact_list.delete(0, tk.END)
    for contact in found_contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    # Function to delete a contact
    selected_index = contact_list.curselection()
    if selected_index:
        contacts.pop(selected_index[0])
        messagebox.showinfo("Success", "Contact deleted successfully")
        view_contacts()

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Labels and Entry fields for adding a contact
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1)

# Buttons for actions
button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.grid(row=4, column=0, columnspan=2, pady=10)

button_view = tk.Button(root, text="View Contacts", command=view_contacts)
button_view.grid(row=5, column=0, columnspan=2, pady=10)

label_search = tk.Label(root, text="Search:")
label_search.grid(row=6, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=6, column=1)

button_search = tk.Button(root, text="Search", command=search_contact)
button_search.grid(row=7, column=0, columnspan=2, pady=10)

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.grid(row=8, column=0, columnspan=2, pady=10)

# Listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.grid(row=9, column=0, columnspan=2)

root.mainloop()
