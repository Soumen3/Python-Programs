# Problem3  : Greedy Hostel Owner

# You know that summers are at peak this year and every day is hot and due to this everyone is using coolers and ACs and a lot of electricity is consumed by the people.
# You are living in a hostel and your hostel owner decided to charge extra for electricity consumption. To achieve this he put one separate electricity meter for every room and connected all those meters to central meter.
# But the hostel owner is a bit greedy and wants to manipulate the meters to show a reading that is more than the actual
# consumption of electricity. He also encrypted all the meters with alphabets. The technique he used for encrypting is as follows:
# Every meter has 6 Alphabets i.e. 6 digits.
# Every alphabet is in upper case.
# Allowed alphabets are A, B, C, D, E, F, G, H, I, J.
# A corresponds to 0, B = 1 and similarly C = 2, D = 3, E = 4, F = 5, G = 6, H = 7, I = 8, J = 9
# The interpretation rules change as follows:
# If the alphabet next to J is A, then  J represents 0. Similarly, if the alphabet after I is B, then I counts as 1 (and not 8), the  alphabet after H is C, then H represents 2. The same is true if  D follows G and if E follows F. 
# Note that A, B, C, D and E will always retain their respective values. When J is not followed by A, J will represent 9 and similar rules for I, H, G and F
# You are given central meter reading and encrypted readings of all the meters in the hostel. Your task is to find out whether the
# the owner is Greedy or Innocent. If he is greedy then print the unit difference otherwise print innocent.
# Owner is greedy if and only if
# (units of all meters in the hostel except central meter < central meter units)
# Input Format:
# First line contains an integer N, giving the number of rooms in the hostel.
# The next line contains N strings each of length 6 characters giving the readings of the meters in the rooms
# The next line contains an integer that gives the reading in the central meter

# Output Format:

# First line containing either GREEDY or INNOCENT
# If the first line is GREEDY, the next line should contain the difference (as a decimal number) between the central meter reading
# and the consumption shown in the rooms.

# Constraints:

# Number of rooms <= 100

# Example 1

# Input
# 3
# JAABHF JAACJA JAACDA
# 500
# Output
# GREEDY
# 105
# A B C D E F G H

# Example 2

# Input
# 8
# JAACJA JAABCH JAABHD JAACAF JAJAJJ JAABEJ JAACJJ JAACDI
# 1500
# Output

# INNOCENT

# Explanation

# The readings are,
# 000200, 000127, 000173, 000205, 0000099, 000149, 000299, 000238
# The sum of these readings is 1490 < 1500, the central meter reading. Hence the owner is INNOCENT.


# Solution:

class Solution:

    def convert_readings(self, readings):
        self.converted_readings = []
        for reading in readings:
            converted_reading = ""
            for i in range(len(reading)):
                if reading[i] == "A":
                    converted_reading += "0"
                elif reading[i] == "B":
                    converted_reading += "1"
                elif reading[i] == "C":
                    converted_reading += "2"
                elif reading[i] == "D":
                    converted_reading += "3"
                elif reading[i] == "E":
                    converted_reading += "4"
                elif reading[i] == "F":
                    if i<len(reading)-1 and reading[i+1] == "E":
                        converted_reading += "4"
                    else:
                        converted_reading += "5"
                elif reading[i] == "G":
                    if i<len(reading)-1 and reading[i+1] == "D":
                        converted_reading += "3"
                    else:
                        converted_reading += "6"
                elif reading[i] == "H":
                    if i<len(reading)-1 and reading[i+1] == "C":
                        converted_reading += "2"
                    else:
                        converted_reading += "7"
                elif reading[i] == "I":
                    if i<len(reading)-1 and reading[i+1] == "B":
                        converted_reading += "1"
                    else:
                        converted_reading += "8"
                elif reading[i] == "J":
                    if i<len(reading)-1 and reading[i+1] == "A":
                        converted_reading += "0"
                    else:
                        converted_reading += "9"

            self.converted_readings.append(int(converted_reading))
                
    
    def Justify(self, data):
        self.rooms = data[0]
        self.readings = data[1].split()
        self.central_meter = data[2]

        # Convert the readings to integers
        self.convert_readings(self.readings)
        total_units = sum(self.converted_readings)

        if total_units > self.central_meter:
            return "GREEDY", (total_units-self.central_meter  )

        return "INNOCENT"




if __name__ == "__main__":
    room = 8
    readings = "JAACJA JAABCH JAABHD JAACAF JAJAJJ JAABEJ JAACJJ JAACDI"
    central_meter = 1500
    data = [room, readings, central_meter]
    s = Solution()
    print(s.Justify(data))