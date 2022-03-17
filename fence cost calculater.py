
# checks for numbers more than zero
def ask_for_input(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)

        except ValueError:
            print(error)
    
# returns Y when user says yes and N otherwise
def yes_or_no(qury):
    qurys = input(qury)
    if "0" in qurys or "y" in qurys or "yes" in qurys:
        return "Y"
    else:
        return "N"

loop = False

while not loop:
    # get input
    print("")
    width = ask_for_input("what is the width ")
    print("")
    length = ask_for_input("what is the length ")
    print("")
    cost = ask_for_input("what is the cost per meter ")
    print("")

    # calculate the perimenter 
    perimenter = (width * 2 + length * 2)

    # calculate the cost 

    amount_to_pay = (perimenter * cost)

    # gives output
    print("The Perimeter is {}".format(perimenter))
    
    print("The cost is {} per meter".format(amount_to_pay))


    if yes_or_no("do you wish to repeat ") == "Y":
        loop = False
    else:
        loop = True