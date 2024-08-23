
jupitor_dictionary = {
    "LOL": "Laughing Out Loud",
    "BRB": "Be Right Back",
    "IDK": "I Don't Know",
    "TY" : "Thank You",
    "RIP": "Rest In Piece"
    
}

answer = input("Enter a text ")
answer_modified = answer.upper()

if answer_modified in jupitor_dictionary:
    message = jupitor_dictionary[answer_modified]
    print(f"{answer_modified} = {message}")

else:
    "Not in dictionary"
