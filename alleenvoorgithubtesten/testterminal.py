import os

# Python program to convert a list to string
    
# Function to convert  
def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)


path =r'./'
list_of_files = []
lijstvanos = []
nummer = 0

for root, dirs, files in os.walk(path):
	for fileman in files:
		list_of_files.append(os.path.join(root,fileman))
for name in list_of_files:
    hoi = name.split(".")
    if hoi[-1] == "py":
        myfile = open(name, "r")
        mylist = myfile.readlines()
        for lijn in mylist:
            lijn = lijn.replace("   ", "")
            ding = lijn.split("(")
            if ding[0] == "os.system":
                lijstvanos.append(lijn)
        hoiman = convert_list_to_string(lijstvanos, "HoiditisAbelvanAbelkrijgtallesmeteennieuwevideoenvandaaghebbenweeencoolprogramma")
        hoiman = hoiman.replace("HoiditisAbelvanAbelkrijgtallesmeteennieuwevideoenvandaaghebbenweeencoolprogramma", "\n")
        with open("config/toevoegen.txt") as dingetjeserbij:
            dingetjeserbij = str(dingetjeserbij.read())
            hoiman = "import os\n\n" + dingetjeserbij + hoiman
            print(hoiman)
        myfile.close()

