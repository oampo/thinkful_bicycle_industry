from manufacturer import Manufacturer
from bike import Bike
from frames import CarbonFrame, AluminiumFrame, SteelFrame
from wheels import RoadWheel, TimeTrialWheel, MountainBikeWheel
from shop import Shop
from customer import Customer


def main():
    """ The main function """

    # Create two manufacturers and add models of bike
    pinarello = Manufacturer("Pinarello", 0.3)
    pinarello.add_model("TimeAttack", CarbonFrame, TimeTrialWheel)
    pinarello.add_model("RoadWarrior", AluminiumFrame, RoadWheel)
    pinarello.add_model("SanRemo", CarbonFrame, RoadWheel)

    trek = Manufacturer("Trek", 0.3)
    trek.add_model("MountainHawg", SteelFrame, MountainBikeWheel)
    trek.add_model("Rodeo", SteelFrame, RoadWheel)
    trek.add_model("Everest", CarbonFrame, MountainBikeWheel)

    # Create a shop which stocks products from both manufacturers
    bobs_cycles = Shop("Bob's Cycles", 0.2)
    bobs_cycles.add_manufacturer(pinarello)
    bobs_cycles.add_manufacturer(trek)

    # Buy 5 of each bike as stock
    for i in xrange(5):
        bobs_cycles.buy("Pinarello", "TimeAttack")
        bobs_cycles.buy("Pinarello", "RoadWarrior")
        bobs_cycles.buy("Pinarello", "SanRemo")

        bobs_cycles.buy("Trek", "MountainHawg")
        bobs_cycles.buy("Trek", "Rodeo")
        bobs_cycles.buy("Trek", "Everest")

    # Create three customers with different budgets
    alice = Customer("Alice", 200)
    dan = Customer("Dan", 500)
    carol = Customer("Carol", 1000)

    customers = (alice, dan, carol)

    # Print the weight of the bikes sold by Bob's Cycles
    print "Bicycle weights:"
    print ""
    for bike_specification in bobs_cycles.product_range():
        print "{:40} {}kg".format(bike_specification.full_name(),
                                  bike_specification.weight)
    print ""

    # Print the bikes which each customer can afford
    print "Customers:"
    print ""
    for customer in customers:
        print "{} can afford the following bikes:".format(customer.name)
        print ""
        for bike_specification in bobs_cycles.product_range():
            price = bobs_cycles.price(bike_specification.manufacturer_name,
                                      bike_specification.name)
            if price > customer.money:
                continue

            print bike_specification.full_name()
        print ""

    # Print the current stock levels at Bob's Cycles
    print "Inventory of Bob's Cycles: "
    print ""
    for bike_specification in bobs_cycles.product_range():
        stock = bobs_cycles.stock(bike_specification.manufacturer_name,
                                  bike_specification.name)
        print "{:40} {} in stock".format(bike_specification.full_name(), stock)

    # Buy a bike for each customer
    alice.buy(bobs_cycles, "Trek", "MountainHawg")
    dan.buy(bobs_cycles, "Trek", "MountainHawg")
    carol.buy(bobs_cycles, "Pinarello", "SanRemo")
    print ""

    # Print the customer's purchases, and remaining money
    for customer in customers:
        print "{} now owns a {}".format(customer.name,
                                        customer.bike.full_name())
        print "{} has ${:.2f} remaining".format(customer.name, customer.money)
        print ""


    # Print the updates stock levels
    print "Updated inventory of Bob's Cycles: "
    print ""
    for bike_specification in bobs_cycles.product_range():
        stock = bobs_cycles.stock(bike_specification.manufacturer_name,
                                  bike_specification.name)
        print "{:40} {} in stock".format(bike_specification.full_name(), stock)

    print ""

    # Print the amount of profit Bob has made
    print "Profit for Bob's Cycles: ${}".format(bobs_cycles.profit)

if __name__ == "__main__":
    main()
