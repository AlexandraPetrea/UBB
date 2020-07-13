import cmd

def test_getCommand():
    assert cmd.getCommand("add Maria are") == "add"
    assert cmd.getCommand("   remove aici 123") == "remove"
    assert cmd.getCommand("    insert      98 89 89 ale") == "insert"
    assert cmd.getCommand("list   all for whatever") == "list"


def test_getCategoryAndValue():
    assert cmd.getCategoryAndValue("add 10 food ") == ("10", "food", "")
    assert cmd.getCategoryAndValue("insert   15 others asdf") == ("15", "others", "asdf")
    assert cmd.getCategoryAndValue("add 100 transport as") ==("100", "transport", "as")

def test_getDayCategoryAndValue():
    assert cmd.getDayCategoryAndValue(" add 15 10 food") == ("15", "10", "food", "")
    assert cmd.getDayCategoryAndValue("add 100 15 others ad") == ("100", "15", "others", "ad")
    
    
def test_passSpaces():
    assert cmd.passSpaces("    ale", 0, 6) == 4
    assert cmd.passSpaces("ale", 0, 3) == 0
    assert cmd.passSpaces("   ale",0, 8) == 3

def test_getText():
    assert cmd.getText("here ", 0, 5) == (4, "here")

def test_passText():
    assert cmd.passText("ale  ", 0, 5) == 3

def test_getRemainder():
    assert cmd.getRemainder("food is love") == "is love"
    assert cmd.getRemainder("others are there") == "are there"
    assert cmd.getRemainder("food as f as d") == "as f as d"

def test_removeTo():
    assert cmd.removeTo("24 to 31") == ("24", "31", "")
    assert cmd.removeTo("15 to 20 asd") == ("15", "20", "asd")

def test_removeDayOrCategory():
    assert cmd.removeDayOrCategory("remove food") == ("food", "")
    assert cmd.removeDayOrCategory("remove internet a") == ("internet", "a")
    assert cmd.removeDayOrCategory("remove others ads") == ("others", "ads")

    
def testEverything():

    assertionError = None

    try:
        test_getCommand()
    except:
        print("<getCommand> failed some tests.")
        assertionError = True

    try:
        test_getCategoryAndValue()
    except:
        print("<getCategoryAndValue failed some tests.")
        assertionError = True

    try:
        test_getDayCategoryAndValue()
    except:
        print("<getDayCategoryAndValue> failed some tests.")
        assertionError = True

    try:
        test_passSpaces()
    except:
        print("<passSpaces> failed some tests.")
        assertionError = True

    try:
        test_getText()
    except:
        print("<getText> failed some tests.")
        assertionError = True

    try:
        test_passText()
    except:
        print("<passText> failed some tests.")
        assertionError = True

    try:
        test_getRemainder()
    except:
        print("<getRemainder> failed some tests.")
        assertionError = True

    try:
        test_removeTo()
    except:
        print("<removeTo> failed some tests.")
        assertionError = True

    try:
        test_removeDayOrCategory()
    except:
        print("<removeDayOrCategory> failed some tests.")
        assertionError = True

    if assertionError is not None:
        raise(Exception("Some tests failed")) 
    
