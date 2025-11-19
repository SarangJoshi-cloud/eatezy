import tkinter as tk
from tkinter import ttk

# --- Main Window ---
root = tk.Tk()
root.title('Eatezy Dashboard')
root.geometry('900x600')

# --- Pages ---
class ReservationsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='Upcoming Reservations', font=('Arial', 16, 'bold')).pack(pady=10)
        for i in range(5):
            frame = tk.Frame(self, borderwidth=1, relief='solid', pady=5, padx=5)
            frame.pack(fill='x', padx=10, pady=5)
            tk.Label(frame, text=f'Customer #{i+1}').pack(side='left')
            tk.Label(frame, text='Table for 2 • 7:00 PM').pack(side='left', padx=20)
            tk.Button(frame, text='Confirm').pack(side='right')

class OrdersPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='Pre-Orders', font=('Arial', 16, 'bold')).pack(pady=10)
        for i in range(5):
            frame = tk.Frame(self, borderwidth=1, relief='solid', pady=5, padx=5)
            frame.pack(fill='x', padx=10, pady=5)
            tk.Label(frame, text=f'Order #{i+101}').pack(side='left')
            tk.Label(frame, text='3 items • ₹650').pack(side='left', padx=20)
            tk.Button(frame, text='Mark Ready').pack(side='right')

class MenuPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='Menu Items', font=('Arial', 16, 'bold')).pack(pady=10)
        tk.Button(self, text='Add New Dish').pack(pady=5)
        for i in range(5):
            frame = tk.Frame(self, borderwidth=1, relief='solid', pady=5, padx=5)
            frame.pack(fill='x', padx=10, pady=5)
            tk.Label(frame, text=f'Dish {i+1}').pack(side='left')
            tk.Label(frame, text='₹250 • Available').pack(side='left', padx=20)
            tk.Button(frame, text='Edit').pack(side='right')

class AnalyticsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='Restaurant Analytics', font=('Arial', 16, 'bold')).pack(pady=10)
        tk.Label(self, text='Total Bookings: 120 this month').pack(pady=5)
        tk.Label(self, text='Total Revenue: ₹1,45,000').pack(pady=5)
        tk.Label(self, text='Average Customer Rating: 4.6★').pack(pady=5)

# --- Navigation ---
pages = {}
def show_page(page_name):
    for page in pages.values():
        page.pack_forget()
    pages[page_name].pack(fill='both', expand=True)

nav_frame = tk.Frame(root, width=200, bg='#eee')
nav_frame.pack(side='left', fill='y')

btns = [('Reservations', ReservationsPage), ('Orders', OrdersPage), ('Menu', MenuPage), ('Analytics', AnalyticsPage)]
for name, cls in btns:
    pages[name] = cls(root)
    tk.Button(nav_frame, text=name, command=lambda n=name: show_page(n)).pack(fill='x', pady=5, padx=5)

# Show default page
show_page('Reservations')

root.mainloop()
