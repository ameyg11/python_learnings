#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "kutta" : "dog",
    "billi" : "cat", 
    "popat" : "parrot"
}

word = input("Enter a word you want meaning of : ")

print(words[word])