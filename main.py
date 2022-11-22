spareMoney = int(input("Wie viel Geld hast du zur verfügung ? "))
consoleOpen = True
itemList = []
price = 0

while consoleOpen:
    print("Zu erhaltenen Artikel:")
    print("Fanta 2€")
    print("Cola 3€")
    print("Snickers 1€")
    print("Mars 1€")
    print("Orangensaft 2€")
    print("")
    print("Zusätzliche Befehle:")
    print("- show shoppingcart | Um dein Einkaufswagen anzugucken")
    print("- money | Um dein aktuelles Guthaben zu sehen")
    print("- checkout | um zu bezahlen")
    print("")
    inputVal = input("Was möchtest du ? ")
    if inputVal.lower() == "fanta":
        costValue = 2
        if spareMoney >= costValue:
            print("Du hast " + inputVal + " in deinen Einkaufswagen hinzugefügt")
            spareMoney = spareMoney - costValue
            itemList.append(inputVal.lower())
            price = price + costValue
        else:
            print("Du hast zu wenig Geld")
        print("")
    elif inputVal.lower() == "cola":
        costValue = 3
        if spareMoney >= costValue:
            print("Du hast " + inputVal + " in deinen Einkaufswagen hinzugefügt")
            spareMoney = spareMoney - costValue
            itemList.append(inputVal.lower())
            price = price + costValue
        else:
            print("Du hast zu wenig Geld")
        print("")
    elif inputVal.lower() == "snickers":
        costValue = 1
        if spareMoney >= costValue:
            print("Du hast " + inputVal + " in deinen Einkaufswagen hinzugefügt")
            spareMoney = spareMoney - costValue
            itemList.append(inputVal.lower())
            price = price + costValue
        else:
            print("Du hast zu wenig Geld")
        print("")
    elif inputVal.lower() == "mars":
        costValue = 1
        if spareMoney >= costValue:
            print("Du hast " + inputVal + " in deinen Einkaufswagen hinzugefügt")
            spareMoney = spareMoney - costValue
            itemList.append(inputVal.lower())
            price = price + costValue
        else:
            print("Du hast zu wenig Geld")
        print("")
    elif inputVal.lower() == "orangensaft":
        costValue = 2
        if spareMoney >= costValue:
            print("Du hast " + inputVal + " in deinen Einkaufswagen hinzugefügt")
            spareMoney = spareMoney - costValue
            itemList.append(inputVal.lower())
            price = price + costValue
        else:
            print("Du hast zu wenig Geld")
        print("")
    elif inputVal.lower() == "show shoppingcart":
        print("Deine Items in deinem Einkaufswagen")
        print("")
        for i in range(0, len(itemList)):
            print("[x] " + itemList[i])

        print("")

    elif inputVal.lower() == "money":
        print("Dein Guthaben: " + str(spareMoney) + "€")
        print("")

    elif inputVal.lower() == "checkout":
        print("Du hast folgende " + str(len(itemList)) + " Gegenstände: ")
        print("")
        for i in range(0, len(itemList)):
            print("[x] " + itemList[i])
        print("für " + price + "€ gekauft.")
        print("")
        price = 0
        itemList = []

    elif inputVal.lower() == "quit":
        exit()
    else:
        print("Dies ist keine Option")