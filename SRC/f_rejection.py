# Function to reject incorrect values entered by console


def rejection (owner, country):
    if owner not in ["Government", "Private"]:
        print ("Please, enter Government or Private")
        return True
    if country not in ["Ghana", "Spain", "Both"]:
        print ("Please, enter Ghana, Spain or Both")
        return True
