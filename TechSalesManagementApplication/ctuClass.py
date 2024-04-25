class ctuStock:
    def __init__(self, shopName, shopLocation, customers, sales, returns):
        self.__shopName = shopName
        self.__shopLocation = shopLocation
        self.__customers = customers
        self.__sales = sales
        self.__returns = returns

    def get_shop_name(self):
        return self.__shopName

    def set_shop_name(self, new_name):
        self.__shopName = new_name
        return True

    def get_shop_location(self):
        return self.__shopLocation

    def set_shop_location(self, new_location):
        self.__shopLocation = new_location
        return True

    def get_number_of_customers(self):
        return self.__customers

    def get_current_sales(self):
        return self.__sales

    def get_returns(self):
        return self.__returns
