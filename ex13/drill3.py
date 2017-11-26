from sys import argv
script, name = argv

print("Hello ", name)
print("How are you doing today?")
print("\nHappy")
print("Ok")
print("Sad\n")
response = input()

if response == "Happy":
    print("I'm happy you are happy")
elif response == "Ok":
    print("Thats ok!")
elif response == "Sad":
    print("Thats too bad")
else:
    print("Invalid response, exiting")
