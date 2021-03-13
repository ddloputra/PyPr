from pip._vendor.distlib.compat import raw_input


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

    def show_item(self):
        print(self.items_in_cart)

    def calculate_item(self):
        temp = self.items_in_cart.values()
        print(int(sum(temp)))
        return int(sum(temp))



# test = ShoppingCart("Test")
# test.add_item("test",12)

user = input("Hello, Welcome to personal shopper Aflamart. What is your name?")
my_cart = ShoppingCart(user)

lm = False

while lm == False:
    print("We'll search everything for you {} \n".format(my_cart.customer_name))
    product = input("What you wanna buy for today? \n")
    price = int(input("How much the price? \n"))
    my_cart.add_item(product, price)
    print('\n')
    case = False
    while case == False:
        print('\n\n\n\n\n\n\n\n\n')
        my_cart.show_item()
        print("1. Add more item")
        print("2. Remove item")
        print("3. Checkout!")
        num = input("Select [1,2,3] : ")
        if num == "1":
            case = True
            lm = False
            print('\n\n\n\n\n\n\n\n\n')
        elif num == "2":
            case = False
            lm = False
            remove = input("What item you wanna remove?")
            my_cart.remove_item(remove)
        elif num == "3":
            sureorno = False
            while sureorno == False:
                print("\n\n\n\n\n\n")
                sureorno = input("Are you sure you wanna checkout? [yes | no]:\n\n")
                sureorno = sureorno.lower()
                if sureorno == "yes" or sureorno == "y":
                    my_cart.show_item()
                    print("Your total items :")
                    total = my_cart.calculate_item()
                    money = int(input("How much you wanna pay?"))
                    while total > money:
                        print("\n\n\n\n\n")
                        print("You dont have enough money to buy all the stuff!")
                        print("Try again!")
                        sureorno = False
                        lm = True
                        case = True
                        break
                    else:
                        changes = money - total
                        print("\n\n\n\n\n\n")
                        print("Your changes : {}".format(changes))
                        print("We will search everything for you. \n Thank you ou for trusting us!")
                        case = True
                        lm = True
                        break
                elif sureorno == "no" or sureorno == "n":
                    case = False
                    sureorno = True
                else:
                    print("Check your spellings!")
                    sureorno = False
        else:
            case = False
            print("Please check your spelling!")


