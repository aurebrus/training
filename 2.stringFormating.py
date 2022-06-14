name = "Bob"
greeting = "Hello, Bob"
print(greeting)

second_greeting = f"Hello, {name}"
print(second_greeting)

name = "Rolf"
second_greeting = f"Hello, {name}"
print(second_greeting)

#template
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)
with_name = greeting.format("Bob")
print(with_name)

#longer_phrase
phrase = "Hello {}. Today is {}."
formatted = phrase.format("Rolf", "Monday")
print(formatted)

