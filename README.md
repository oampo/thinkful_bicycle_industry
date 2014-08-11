# Thinkful Bicycle Project - An Example Solution

A brief guide to the classes:

## BikeSpecification

The specification of a bike, describing what components will be used to construct a bike.  This will be used to create instances of the `Bike` class.  Notice how we store two *type* variables.  These should be class types rather than class instances.  They will only be instantiated when we construct a bike from the specification.

## Bike

A class represing an actual bike which a shop can hold in stock, or a person can own.  It is constructed from a `BikeSpecification` object.  Notice how we instatiate the wheels and frame by instantiating the the type variables from the specification.

## Frame, Wheel, \*Frame, \*Wheel

Frames representing the different frame and wheel types.  Notice how the variables here are class rather than instance variables (i.e. we don't use self).  This means that we consider the variables to belong to *all* instances of the frame or wheel type, not just to a single instance.

## Manufacturer

A manufacturer of bikes.  The manufacturer stores a dictionary containing the model specifications.  The specifications are created and added to the dictionary in the `add_model` method.  When a bike needs to be sold (in the `sell` method, the manufacturer creates a new `Bike` instance from the corresponding specification.

## Shop

A shop selling bikes.  Stores a dictionary of manufactures which it sources parts from, and an inventory of bikes held in stock.  When the shop buys a bike it receives a `Bike` object from the manufacturer's `sell` method, and adds it to the inventory.  When it sells a bike it removes the `Bike` object from the inventory by popping it from the list of stock for that particular bike, and returns it to the customer.

## Customer

A customer.  The can buy a bike from a shop using their money, which then reduces.  Go commerce!
