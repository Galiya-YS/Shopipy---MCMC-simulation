from ClassSupermarket import Supermarket 

Supermarket1=Supermarket()


Supermarket1.next_minute()


Supermarket1.add_new_customers()

for i in range(0,10):
    Supermarket1.next_minute()
    
Supermarket1.write_all_cust()
