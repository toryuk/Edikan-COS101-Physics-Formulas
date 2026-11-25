# 3. IBIBIO DICTIONARY (20 words)
ibibio_dict = {
    "buy": "de",
    "sell": "nyam",
    "read": "wete",
    "water": "mmong",
    "food": "udia",
    "man": "owo",
    "woman": "owan",
    "child": "eyen",
    "house": "ndo",
    "school": "sukul",
    "book": "nwed",
    "friend": "mbufo",
    "money": "ini",
    "sleep": "tongo",
    "run": "wot",
    "see": "kini",
    "love": "ima",
    "work": "usung",
    "god": "Abasi",
    "good": "emem"
}






# 5. IDOMA DICTIONARY (20 words)
idoma_dict = {
    "buy": "kpa", 
    "sell": "kpa", 
    "read": "ka", 
    "water": "ama", 
    "food": "onogwu",
    "man": "omo", 
    "woman": "oya", 
    "child": "owa", 
    "house": "ogwu", 
    "school": "skul",
    "book": "ibuku", 
    "friend": "ochi", 
    "money": "ego", 
    "sleep": "li", 
    "run": "gba",
    "see": "na", 
    "love": "ayima", 
    "work": "iho", 
    "god": "Owoicho", 
    "good": "yo"
}





while True:
    print("\n=========================")
    print("   NIGERIAN LANGUAGE DICTIONARY")
    print("===========================")
    print("1. Igbo")
    print("2. Yoruba")
    print("3. Ibibio")
    print("4. Etsako")
    print("5. Idoma")
    print("0. Exit")

    choice = input("\nSelect a language (1-5) or 0 to exit: ")

    if choice == "0":
        print("Closing dictionary. Goodbye!")
        break

    word = input("Enter an English word: ").lower()

    if choice == "1":
        if word in igbo_dict:
            print(f"Translation: {igbo_dict[word]}")
        else:
            print(f"Sorry, '{word}' is not in the Igbo dictionary.")

    elif choice == "2":
        if word in yoruba_dict:
            print(f"Translation: {yoruba_dict[word]}")
        else:
            print(f"Sorry, '{word}' is not in the Yoruba dictionary.")

    elif choice == "3":
        if word in ibibio_dict:
            print(f"Translation: {ibibio_dict[word]}")
        else:
            print(f"Sorry, '{word}' is not in the Ibibio dictionary.")

    elif choice == "4":
        if word in etsako_dict:
            print(f"Translation: {etsako_dict[word]}")
        else:
            print(f"Sorry, '{word}' is not in the Etsako dictionary.")

    elif choice == "5":
        if word in idoma_dict:
            print(f"Translation: {idoma_dict[word]}")
        else:
            print(f"Sorry, '{word}' is not in the Idoma dictionary.")

    else:
        print("Invalid choice! Please select a number from 1 to 5.")

