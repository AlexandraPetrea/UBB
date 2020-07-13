import cmd
import ui
import tests
import comand


def main():

    undo = []

    category = cmd.buildCategList
    cmdList = cmd.buildHelpList

    try:
        tests.testEverything()
        print("All tests passed")
    except Exception as ex:
        print(ex)
        print(0)

    print("Choose the type of program:")
    print("1.Command based")
    print("2.UI based")
    uType = input("Enter the type of program:")

    while uType not in ['1','2']:
        print("1.Command based")
        print("2.UI based")

    if uType == '1':
        comand.commandBased(category, cmdList, undo)
    else:
        ui.UIBased(category, cmdList, undo)

main() 
