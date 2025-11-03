class MenuItem:


    
    def __init__(self, name, price, category, available = True):
        self.name = name
        self.price = price
        self.catagory = category
        self.is_avail = available
       

    def get_info(self):
        return f"The catagory is {self.catagory}, you choose {self.name} and the price is: {self.price}"
        
    def is_available(self):
        return self.is_avail

    def set_available(self, staus):
        if staus == "available":
            self.is_avail = True
        else:
            self.is_avail = False

    
class Menu:

    def __init__(self):
        self.items = []
        
    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)


    def get_item_by_name(self, item_name):
        return [item for item in self.items if item.name == item_name] 
    

    def get_item_by_catagory(self, catagory_name):
        return [item for item in self.items if item.catagory == catagory_name] 
    

    def displya_menu(self):
        print([item for item in self.items if item.is_avail == True] 
    )


    def get_len_menu(self):
        return len(self.items)

    

class Costomer:
    
    def __init__(self, name, satisfaction = 50):
        self.name = name
        self.satisfaction = satisfaction
    

    def increase_satisfaction(self, amount):
        if sum(self.satisfaction, amount) <= 100:
            self.satisfaction += amount
        else:
            print("The max satisfaction is 100")

    
    def decrease_satisfaction(self, amount):
        if self.satisfaction - amount >= 0 :
            self.satisfaction -= amount
        else:
            print("The minimum satisfaction is 0")
            
    
    def is_happy(self):
        return self.satisfaction >= 70
    

    def display(self):
        print(f"The name is {self.name}, and he was {self.satisfaction} satisfied")



class Order:

    def __init__(self, costomer: Costomer, order_number):
        self.costomer = costomer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self, item: MenuItem):
        self.items.append(item)
        self.total_price += item.price
    

    def remove_item(self, item_name: MenuItem):
        for item in self.items:
            if item.name == item_name.name:
                self.items.remove(item)
                self.total_price -= item_name.price


    def get_total_price(self):
        return self.total_price


    def set_status(self, new_status):
        self.status = new_status


    def display_order(self):
        print(f"costumer name {self.costomer.name}, order number {self.order_number}, he order {self.items}, the total price is {self.total_price}, the status is {self.status}")


    def is_complited(self):
        return self.status == "deliverd"



class Staff:

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.energy = 100
        self.role = role

    def work(self):
        self.energy -= 10
        print(f"the energy decrease to {self.energy}")

    def rest(self):
        if (self.energy + 20) < 100:
            self.energy += 20
        else:
            self.energy = 100
    
    def is_tierd(self):
        return self.energy <= 30
    
    def display(self):
        return f"His name is {self.name}, His salary is {self.salary}, His role is {self.role}, He has {self.energy} energy left"


class Chef(Staff):

    def __init__(self, name, salary, role, specialty):
        super().__init__(name, salary, role)


    def cook_order(self, order: Order):
        order.set_status("cooking")
        super().work()
        order.set_status("ready")
    
    def work(self):
        self.energy -= 15
        print("cooking is harder")

    
class Waiter(Staff):

    def __init__(self, name, salary, role):
        super().__init__(name, salary, role)
        self.tips = 0

    def take_order(self, costumer: Costomer, menu: Menu):
        order = Order(costumer, 1)
        choose = input("Enter your choice")
        for item in menu:
            if item.name == choose:
                order.add_item(item)

        return order.display_order()



    def serve_order(self, order: Order):
        order.set_status("deliverd")
        return Costomer.is_happy()
    

    def receive_tip(self, amount):
        self.tips += amount


    def get_total_earnings(self):
        return sum(self.tips, self.salary)
    

class Restaurant:
    
    def __init__(self, name):
        self.name = name
        self.menu = Menu
        self.staff = [Staff]
        self.orders = [Order]
        self.money = 1000

    def hire_staff(self, staff: Staff):
        self.staff.append(staff)

    def fire_staff(self, name):
        for staff_name in self.staff:
            if staff_name.name == name:
                self.staff.remove(staff_name)

    
    def create_order(self, costomer: Costomer):
        order = Order(costomer, 1)
        for item in self.menu:
            choose = input("Enter your choice")
            if item.name == choose:
                order.add_item(item)
        self.orders.append(order)

    
    def process_order(self, order: Order):
        pass

    def complete_order(self, order: Order):
        self.money += order.get_total_price()
        for item in self.orders:
            if item.order_number == order.order_number:
                self.orders.remove(item)

    def pay_salaries(self):
        for person in self.staff:
            if isinstance(person, Chef):
                self.money -= Chef.salary
            else:
                self.money -= Waiter.salary











    

    