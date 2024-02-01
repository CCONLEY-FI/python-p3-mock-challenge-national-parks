#!/usr/bin/env python3
from datetime import datetime

class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters, inclusive")
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters, inclusive")
        self._name = value

    def trips(self):
        return self._trips

    def national_parks(self):
        return list(set(trip.national_park for trip in self._trips))

    def total_visits_at_park(self, park):
        return sum(1 for trip in self._trips if trip.national_park == park)

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not (isinstance(start_date, str) and isinstance(end_date, str)):
            raise ValueError("Dates must be strings")
        elif len(start_date) < 7 or len(end_date) < 7:
            raise ValueError("Dates must be at least 7 characters long")
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        self.register_trip()

    def register_trip(self):
        self._visitor._trips.append(self)
        self._national_park._trips.append(self)
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Start date must be a string")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise ValueError("End date must be a string")
        self._end_date = value

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park

class NationalPark:
    _all_parks = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string of length 3 or more characters")
        self._name = name
        self._trips = []
        NationalPark._all_parks.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        return self._trips

    def visitors(self):
        return list(set(trip.visitor for trip in self._trips))

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        visitor_count = {}
        for trip in self._trips:
            visitor = trip.visitor
            if visitor in visitor_count:
                visitor_count[visitor] += 1
            else:
                visitor_count[visitor] = 1
        return max(visitor_count, key=visitor_count.get) if visitor_count else None

    @classmethod
    def most_visited(cls):
        if not cls._all_parks:
            return None
        return max(cls._all_parks, key=lambda park: park.total_visits())
    
    


# Ensure to import pytest or set up your testing environment to use these tests.

           
# Exceptions
#define exceptions should be within the class? or outside of the class?
    #answer: outside of the class
    #reason: exceptions are not part of the class, they are part of the module
    #format:
        #describe the error
            #use case: when would this error be raised?
            #use location: where in the code would this error be raised?        
# Visitor
    # Visitor __init__(self, name)
        # Visitor is initialized with a name, as a string
    # Visitor property name
        # Returns the visitor's name
        # Names must be of type str
        # Names must be between 1 and 15 characters, inclusive
        # Should be able to change after the visitor is instantiated
    # Visitor trips()
        # Returns a list of all trips for that visitor
        # Trips must be of type Trip
    # Visitor national_parks()
        # Returns a unique list of all parks that visitor has visited
        # Parks must be of type NationalPark
    # Visitor total_visits_at_park(park)
        # Receives a NationalPark object as argument
        # Returns the total number of times a visitor visited the park passed in as argument
        # Returns 0 if the visitor has never visited the park
        # Trip __init__(self, visitor, national_park, start_date, end_date)
            # Trip is initialized with a Visitor instance, a NationalPark instance, a start_date, and an end_date
        # Trip property start_date
            # Returns the trip's start_date 
            # Start_date must be of type str
            # Start_date length must be greater or equal to 7 characters
            # Is in the format "September 1st"
            # Should be able to change after the trip is instantiated
        # Trip property end_date
            # Returns the trip's end_date
            # End_date must be of type str
            # End_date length must be greater or equal to 7 characters
            # Is in the format "September 1st"
            # Should be able to change after the trip is instantiated
        # Trip property visitor
            # Returns the Visitor object for that trip
            # Must be of type Visitor
        # Trip property national_park
            # Returns the NationalPark object for that trip
            # Must be of type NationalPark
        # Trip property duration
            # Returns the duration of the trip
            # Duration is the number of days between the start_date and the end_date, inclusive
# NationalPark
    # NationalPark __init__(self, name)
            # NationalPark is initialized with a name, as a string
        # NationalPark property name
            # Returns the national_park's name
            # Names must be of type str
            # Names length must be greater or equal to 3 characters
            # Should not be able to change after the national_park is instantiated
            # hint: hasattr()
        # NationalPark trips()
            # Returns a list of all trips at a particular national park
            # Trips must be of type Trip
        # NationalPark visitors()
            # Returns a unique list of all visitors a particular national park has welcomed
            # Visitors must be of type Visitor
        # NationalPark total_visits()
            # Returns the total number of times a park has been visited
            # Returns 0 if the park has no visits
        # NationalPark best_visitor()
            # Returns the Visitor instance that has visited that park the most
            # Returns None if the park has no visitors
    # Bonus: Aggregate and Association Method
        # NationalPark classmethod most_visited()
            # Returns the NationalPark instance with the most visits.
            # Returns None if there are no visits.
            # hint: will need a way to remember all NationalPark objects
            # hint: do you have a method to get the total visits for a particular NationalPark object?
            # Uncomment lines 127-135 in the national_park_test file