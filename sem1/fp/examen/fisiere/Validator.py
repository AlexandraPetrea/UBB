class ValidatorException(Exception):
    def __init__(self, messageList=["Validation error!"]):
        self._messageList = messageList
        
    def getMessage(self):
        return self._messageList

    def Verify_name(self,name):
        for i in range(0,len(name)):
            if ((ord(name[i])<65)or((ord(name[i])>90)and(ord(name[i])<97))or(ord(name[i])>122))and ord(name[i])!=32:
                return False
        return True
        
    def __str__(self):
        result = ""
        for message in self.getMessage():
            result += message
            result += "\n"
        return result
