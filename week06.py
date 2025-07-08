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




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

