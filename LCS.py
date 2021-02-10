# -----------------------------------------------------------------------------------------------
# Author: Subhashis Suara
# Algorithm: Longest Common Subsequence
# Definations:
#   X - First Sequence
#   Y - Second Sequence
#   C[i][j] - Length of LCS between X[i - 1] and Y[j - 1] (i & j start from 1 to m, n inclusive)
#   B[i][j] - Direction for C[i][j] Element. Can be D - Diagonal, H - Horizontal, V - Vertical
# -----------------------------------------------------------------------------------------------

import sys

# Change the print length for LCS result in terminal
# Enter 0 if you don't want to print in terminal
# Enter -1 if you don't want to limit the print length
LCSPrintLength = 50

# Don't Change
LCSValue = ""

def LCS(X, Y):
    m = len(X)
    n = len(Y)
    B = [[0 for i in range(n + 1)] for j in range(m + 1)]
    C = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (X[i - 1] == Y[j - 1]): # Adjusted for 0 based Indexing
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = 'D'
            elif (C[i - 1][j] > C[i][j - 1]):
                C[i][j] = C[i - 1][j]
                B[i][j] = 'V'
            else:
                C[i][j] = C[i][j - 1]
                B[i][j] = 'H'
    
    return B, C

def printLCS(X, B, i, j):
    if (i == 0 or j == 0):
        return
    if (B[i][j] == 'D'):
        printLCS(X, B, i - 1, j - 1)
        # print(X[i - 1], end = "")
        global LCSValue
        LCSValue += X[i - 1]
    elif (B[i][j] == 'V'):
        printLCS(X, B, i - 1, j)
    else:
        printLCS(X, B, i, j - 1)

if __name__ == "__main__":
    # Initialization to bound X & Y values in case of empty txt files
    X = ""
    Y = ""

    # Making sure user understands the required files
    print("\nBefore proceeding, please ensure the following:")
    print("- You have a X.txt file, containing the 1st sequence, in the same path as this program.")
    print("- You have a Y.txt file, containing the 2nd sequence, in the same path as this program.")
    print("- If you have any file called LCS.txt in the same path as this program,")
    print("  ensure the data is backed up as the file will be overwrittern.")
    print("  If the file doesn't exist, it will be created automatically & contain the result.")
    input("\nPress any key to continue...\n")

    try:
        with open('X.txt', 'r') as XFile:
            # Remove Endline & Trailing White Spaces
            X = XFile.read().replace('\n', '').strip()
            # Remove All White Spaces
            X = ''.join(X.split())
            if (X == ""):
                print("Error: X.txt file is empty! Please enter the relevent 1st sequence in X.txt & try again.\n")
                sys.exit()
    except FileNotFoundError as fileNotFoundError:
            print("Error: File X.txt not found! Please create the file and try again.\n")
            sys.exit()
    except Exception as error:
            print(f"Error: {error}\n")
            sys.exit()

    try:
        with open('Y.txt', 'r') as YFile:
            # Remove Endline & Trailing White Spaces
            Y = YFile.read().replace('\n', '').strip()
            # Remove All White Spaces
            Y = ''.join(Y.split())
            if (Y == ""):
                print("Error: Y.txt file is empty! Please enter the relevent 2nd sequence in Y.txt & try again.\n")
                sys.exit()
    except FileNotFoundError as fileNotFoundError:
            print("Error: File Y.txt not found! Please create the file and try again.\n")
            sys.exit()
    except Exception as error:
            print(f"Error: {error}\n")
            sys.exit()

    m = len(X)
    n = len(Y)
    B, C =  LCS(X, Y)
    printLCS(X, B, m, n)
    if (len(LCSValue) > 0):
        if (LCSPrintLength != 0):
            if (len(LCSValue) > LCSPrintLength and LCSPrintLength > 0):
                print(f"LCS for given X & Y sequences: {LCSValue[:LCSPrintLength]}... {len(LCSValue) - LCSPrintLength} more characters. \n")
            else:
                print(f"LCS for given X & Y sequences: {LCSValue}\n")
                
        print("The result has been saved to LCS.txt file in the same path as this program. Have a great day!\n")

        try:
            with open('LCS.txt', 'w+') as LCSFile:
                LCSFile.write(LCSValue)
        except Exception as error:
                print(f"Error: {error}\n")
                sys.exit()
    else:
        print("No LCS found from X & Y sequences.\n")