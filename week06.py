def load_to_list(filepath: str) -> list[float]:
    with open(filepath, "r") as file:
        temps = [float(line.strip()) for line in file if line.strip()]
        print(temps)

load_to_list("data/temperatures.txt")

def descriptive_statistics(source_data: list[float]) -> None:
    with open(source_data, "r") as file:
        temps = [float(line.strip()) for line in file if line.strip()] #.strip() - filtering out empty spaces.
    num_temps = len(temps)
    ave = sum(temps) / num_temps
    highest = max(temps)
    lowest = min(temps)
    print(f"\nThere are {num_temps} values in the data source.\nThe average value is {ave:.2f}.\nThe highest value is {highest} and the smallest value is {lowest}.")

descriptive_statistics("data/temperatures.txt")

def apply_markup(filepath: str) -> None:
    with open(filepath, "r") as file:
        for line in file:
            words = line.strip().split() # words do not contain spaces, tabs, etc. and are split with spaces
            formatted = []
            for word in words:
                if word.startswith("."):
                    formatted.append(word[1:].upper()) # adding new item to the end of list, and slicing the first character
                elif word.startswith("_"):
                    formatted.append(' '.join(word[1:])) #adding spaces between letters
                else:
                    formatted.append(word) # leave other words alone.
            print(' '.join(formatted))

apply_markup("data/markup.txt")

"""
REFLECTION:
intersection:
the code for my intersection was a lot shorter than the one you wrote.
I made my result be empty, and then used an if statement inside of a loop for elements in foo
stating that if it was in bar and not result (so the list wasn't empty), then the result would
be the empty result + whatever the intersection was. It passed the tests.

alphabetical:
My code involved ascii values. So if the values were not corresponding to a letter, then
the result was false, or if the i-1 ascii was greater than the i ascii the result would be
false too.

letters:
This one also involved ascii values where they had to be in a certain range, the program
would return the result (which was the transformed string) and if was empty, it would
return None.

generate palindrome:
Here, I made a variable reversed_string like in your code "pali", and used a while loop
to count i down from len(string). Then made result = reversed_string + string[i].
I think this one is a lot more similar to your code than the other ones.

is palindrome:
Our code here is also similar, but I again used ascii values to filter out non-letter
characters.

- I think my code works well. All of it passed the tests and I feel comfortable with the
way I did things.



"""


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

