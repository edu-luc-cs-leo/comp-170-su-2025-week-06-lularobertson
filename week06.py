def load_to_list(filepath: str) -> list[float]:
    with open(filepath, "r") as file:
        lines = file.readlines()
    return [float(line.strip()) for line in lines if line.strip()] #write numbers as floats, without \n
        
temps = load_to_list("data/temperatures.txt") #importing the text
print(temps)

def descriptive_statistics(source_data: list[float]) -> None:
    with open(source_data, "r") as file:
        temps = [float(line.strip()) for line in file if line.strip()]
    num_temps = len(temps)
    ave = sum(temps) / num_temps
    highest = max(temps)
    lowest = min(temps)
    print(f"\nThere are {num_temps} values in the data source.\nThe average value is {ave:.2f}.\nThe highest value is {highest} and the smallest value is {lowest}.")

descriptive_statistics("data/temperatures.txt")




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

