import os 

#Function to search the dxf file into a certain directory
def Path_Finder(search_name):

    #where the search will happen
    chiffre = search_name[0:4]

    #creating the searching directory 
    search_dir = r"\\ctbn33\AVOR\__Desenhos_Windchill" + "/" + chiffre

    #all the files in the directory
    dir_files = os.listdir(search_dir)
    match_files = []

    #Search for the files that match
    for i in range(len(dir_files)):
        if dir_files[i].endswith(".dxf") and dir_files[i].startswith(search_name[0:14]):
            match_files.append(dir_files[i])
    
    #On the matchfiles get the latest version, if multiple match files exist. 
    if len(match_files) > 1:
        try:
            version = 0
            index = 0

            for i in range(len(match_files)):
                n_version = int(match_files[i][-6:-4])
                if n_version >= version:
                    index = i
                    version = n_version
            
            latest_version_dir = search_dir + "/" + match_files[index]
        except:
            latest_version_dir = search_dir + "/" + match_files[0]
    
    else:
        latest_version_dir = search_dir + "/" + match_files[0]
    
    return(latest_version_dir)

Path_Finder("MSBA-10008-010")