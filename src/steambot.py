from mechanize import Browser
import os
import ctypes
import winsound

weaponExterior = ["Battle-Scarred", "Well-Worn", "Field-Tested", "Minimal Wear", "Factory New"]
linkParts = ["http://steamcommunity.com/market/listings/730/", "%20%7C%20", "%20%28", "%29", "%20"]
valuableWeapons = ["AK", "AWP", "M4", "Karambit", "Flip Knife", "Gut Knife", "M9 Bayonet"]
br = Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.60 Safari/537.11')]
username = ""
password = ""
msgBox = ctypes.windll.user32.MessageBoxA
clear = lambda: os.system('cls')

def getLinks(weaponName, weaponModel, weaponExterior, linkParts):
    links = [];
    if " " in weaponName:
        weaponNameParts = weaponName.split(" ")
        weaponName = linkParts[4].join(weaponNameParts)
    
    if " " in weaponModel:
        weaponModelParts = weaponModel.split(" ")
        weaponModel = linkParts[4].join(weaponModelParts)
    
    for i in range(len(weaponExterior)):
        if " " in weaponExterior[i]:
            weaponExteriorParts = weaponExterior[i].split(" ")
            weaponExterior[i] = linkParts[4].join(weaponExteriorParts)
        finalLink = ""
        finalLink += linkParts[0] + weaponName + linkParts[1] + weaponModel + linkParts[2] + weaponExterior[i] + linkParts[3]
        links.append(finalLink)
    return links

def checkItemAvailability():
    #Check if there are listing for the item
    return

def getCheapestPrice():
    #If there as listing for the item get cheapest price and compare it to the user input
    return

def main():
    print "Insert complete item name:"
    weaponName = raw_input()
    print "Insert weapon exterior name:"
    weaponModel = raw_input()
    print "Insert maximum price for the weapon:"
    maxPrice = raw_input()
    try:
        maxPrice = float(maxPrice)
    except:
        print "Insert a numeric value"
        return

    links = getLinks(weaponName, weaponModel, weaponExterior, linkParts)

    clear()
    print "Starting search for " + weaponName + " | " + weaponModel
    print "Maximum price is " + str(maxPrice) + "\n"

    for i in range(len(links)):
        hit = 0
        nextLink = links[i]
        response = br.open(nextLink)
        save = open("current.htm", "w")
        page = response.read()
        save.write(page)
        #HTML Parsing
        if hit:
            #Also if price > y
            if weaponName in valuableWeapons:
                print "Add Later"
                #winsound.Play("", winsound.SND_ALIAS) -> Get Valuable weapon sound
            else:
                winsound.PlaySound("../res/warningBeep", winsound.SND_ALIAS) 
            msgBox(None, "Item found!\n"+ weaponName + " | " + weaponModel + " : " + weaponExterior[i] + "\n" + nextLink, "New Hit!", 0)
            
main()