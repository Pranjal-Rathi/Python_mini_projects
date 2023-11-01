class Hotel:
    sortParam = 'name'
    def __init__(self):
        self.name = ''
        self.roomAvl = 0
        self.loc = ''
        self.rating = float
        self.pp = 0

    def __lt__(self, other):
        getattr(self, Hotel.sortParam)<getattr(other, Hotel.sortParam)

    # Function to change sort parameter to name
    @classmethod
    def sortByName(cls):
        cls.sortParam='name'

    # Function to change sort parameter to room availability
    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam='roomAvl'

    # Function to change sort parameter to rating
    @classmethod
    def sortByRate(cls):
        cls.sortParam='rating'

    def __repr__(self):
        return "PRHOTELS DATA:\nHotelName:{}\tRoom Available:{}\tLocation:{}\tRating:{}\tPricePer Room:{}".format(self.name, self.roomAvl, self.loc, self.rating, self.pp)

# Create class for user data.

class User_data:
    def __init__(self):
        self.uname=''
        self.uid = 0
        self.cost = 0

    def __repr__(self):
        return  "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname, self.uid, self.cost)

# Print hotel data.
def PrintHotelData(hotels):
    for h in hotels:
        print(h)

# Sort Hotels data by name.
def SortHotelByName(hotels):
    print("SORT BY NAME:")
    Hotel.sortByName()
    hotels.sort()
    PrintHotelData(hotels)
    print()

# Sort Hotels by rating.
def SortHotelByRating(hotels):
    print("SORT BY RATING:")
    Hotel.sortByRate()
    hotels.sort()
    PrintHotelData(hotels)
    print()

# Printt Hotels for any city location.
def PrintHotelByCity(s, hotels):
    print("HOTELS FOR {} LOCATION ARE:".format(s))
    hotelsByLoc = [h for h in hotels if h.location == s]
    PrintHotelData(hotelsByLoc)
    print()

# Sort Hotels data by room available.
def SortHotelByRoomAvailable(hotels):
    print("SORT BY ROOM AVAILABLE:")
    Hotel.sortByRoomAvailable()
    hotels.sort()
    PrintHotelData(hotels)
    print()

# Print the user's data
def PrintUserData(userName, userID, bookingCost, hotels):
    users=[]
    # Access user data.
    for i in range(3):
        u=User_data()
        u.uname = userName[i]
        u.uid = userID[i]
        u.cost = bookingCost[i]
        users.append(u)
    for i in range(len(users)):
        print(users[i],"\tHotel name:"+hotels[i].name)

# Function to solve
# Hotel Management problem
def HotelManagement(userNAme, userId, hotelNAme, bookingCost, rooms, locations, ratings, prices):
    #Initialize arrays that stores hotel data and user data
    hotels=[]
    # Create objects for hotel and user
    # Initialize the data
    for i in range(3):
        h = Hotel()
        h.name = hotelNAme[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]
        hotels.append(h)

    print()

    # Call the various operations
    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelByCity("Mumbai", hotels)
    SortHotelByRoomAvailable(hotels)
    PrintUserData(userName, userId, bookingCost, hotels)

# Driver Code.
if __name__=='__main__':
    # Initialize variables to store hotel data and user data
    userName = ["U1","U2","U3"]
    userId = [2,3,4]
    hotelName = ["H1","H2","H3"]
    bookingCost = [1000, 1200, 1100]
    rooms = [4, 5, 6]
    locations = ["Mumbai","Delhi","Chennai"]
    ratings = [5,4,5]
    prices = [100,200,100]

    # Function to perform operations
    HotelManagement(userName, userId, hotelName, bookingCost, rooms, locations, ratings, prices)