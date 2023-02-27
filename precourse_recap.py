current_chocolate = "malteasers"
number_of_malteasers_in_a_packet = 40
number_of_malteasers_eaten = 25
chocolate_remaining = number_of_malteasers_in_a_packet - number_of_malteasers_eaten

def chocolate_left():
    print(f"My favourite chocolate is currently " + current_chocolate + " I have " + str(chocolate_remaining) + " left in my packet!")

chocolate_left()