import pandas as pd
import matplotlib.pyplot as plt

from utils import getPossibleCombinations, checkMonotonicFunction,valueToColor
# headers
columns = ["act:0,0 inh:0,0",
            "act:1,0 inh:0,0",
            "act:1,1 inh:0,0",
            "act:0,0 inh:1,0",
            "act:1,0 inh:1,0",
            "act:1,1 inh:1,0",
            "act:0,0 inh:1,1",
            "act:1,0 inh:1,1",
            "act:1,1 inh:1,1"]

# Generate all possible Boolean functions
allFunctions = getPossibleCombinations(9)

# Filter functions that are monotonic
monoFunctions = []
for f in allFunctions:
    if checkMonotonicFunction(f):
        monoFunctions.append(f)
        print(f)



# init DataFrame from all calculated monotonic functions
df = pd.DataFrame(monoFunctions, columns=columns)


# save table to image
def saveTableAsImage(df, filename):
    # init plot
    fig, ax = plt.subplots()  # Adjust the size of the image
    ax.axis('off')  # Turn off the axis

    # give red and white colors
    table_data = []
    for row in df.values:
        colored_row = []
        for value in row:
            colored_row.append(valueToColor(value))
        table_data.append(colored_row)

    # create table
    ax.table(cellText=df.values,
             cellColours=table_data,
             colLabels=df.columns,
             cellLoc='center',
             loc='center',
             edges='closed')

    # save file
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

# save table to image png file
saveTableAsImage(df, 'monotonic_functions_table.png')