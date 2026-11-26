# 1. IGBO DICTIONARY by Eke Sonia(20 words)
igbo_dict = {
    "buy": "Zụta", 
    "sell": "Ree", 
    "read": "Gụọ", 
    "water": "Mmiri", 
    "food": "Nri",
    "man": "Nwoke", 
    "woman": "Nwanyị", 
    "child": "Nwa", 
    "house": "Ụlọ", 
    "school": "Ụlọ akwụkwọ",
    "book": "Akwụkwọ", 
    "friend": "Enyi", 
    "money": "Ego", 
    "sleep": "Rahụ ụra", 
    "run": "Gbaa ọsọ",
    "see": "Hụ", 
    "love": "Ịhụnanya", 
    "work": "Ọrụ", 
    "god": "Chineke", 
    "good": "Ọma"
}



# 3. IBIBIO DICTIONARY by Edikan Ukpong (20 words)
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




# 4. ETSAKO DICTIONARY by victor onoshioagbe Blessing (20 words)
etsako_dict = {
    "buy": "Dẹ", 
    "sell": "kie", 
    "read": "Zẹ", 
    "water": "Amẹ", 
    "food": "Ema",
    "man": "Ọzawo", 
    "woman": "Ọkpotsot", 
    "child": "Ọmọ", 
    "house": "Owa", 
    "school": "Owowẹna",
    "book": "Ebe", 
    "friend": "Ukuekhia", 
    "money": "Igho", 
    "sleep": "ogwe", 
    "run": "Na",
    "see": "Miẹ", 
    "love": "Uyemi", 
    "work": "akanya", 
    "god": "Ọghẹna", 
    "good": "emeso"
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

