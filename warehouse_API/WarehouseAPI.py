import mysql.connector
from mysql.connector import errorcode
from enum import Enum

#Initalization

#Must input provide credentials to access the database, varies on database
cnx= mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='warehouse')


cursor = cnx.cursor()
exit=False
autoCommit= False
askAfterChanges=False

#Control Functions
def sendQuery(cursor,query):
    try:
        cursor.execute(query)
        return True
    except mysql.connector.Error as e:
        print ("An error has occured: {}".format(e))
        return False

    

def ValidateEntry (query,data):
    for key, value in data.items():
        print(f"{key}:{value}")
    uInput= input ("Is Everything correct? (Y/N) : ")
    if uInput =="Y":
        try:
            cursor.execute(query, data)
            print("Changes written to database.")
            if(askAfterChanges):
                commitToDatabase()
        except mysql.connector.Error as e:
            print ("An error has occured: {}".format(e))
            return
                 
    elif uInput=="N":
        print("Discarding data")
    else:
        print("Unknown Input")
    
def deleteEntry(query):
    if sendQuery(cursor,query):
        print("Successfully deleted")
        if(askAfterChanges):
            commitToDatabase()
    else:
        print("Delete was unsucessful")

def commitToDatabase():
    uInput= input("Commit all changes? (Y/N): ")
    if uInput== "Y":
        print("Commiting")
        cnx.commit()
    elif uInput=="N":
        print("No commit was sent.")
        return
    else:
        print("Unknown Input")
        
#Data INSERT, UPDATE, and DROP Functions

#For all functions 
#updateEntry is 0, 1, or 2; 0 if adding new entry and 1 if updating an entry and 2 if dropping an Entry
#data is a dictionary, needs to be passed in for updating an entry, otherwise can be uninitalized
#key is the Primary Key for the entry, can be 0 if adding an entry, but required to update or drop an Entry

class Command(Enum):
    INSERT=0
    UPDATE=1
    DELETE=2
    

def clientEntry(updateEntry,data,key):
    if(updateEntry==Command.INSERT):
        client = input('Enter Client Name: ')
        clientAd= input('Enter Client Address: ')
        clientContact = input('Enter Client Contact: ')
        query= ("INSERT INTO clients (client_name, client_address, contact_details) VALUES (%(Client)s, %(clientAddress)s, %(clientContact)s)")
        data ={
                            'Client':client,
                            'clientAddress':clientAd,
                            'clientContact':clientContact
                        }
        
    elif(updateEntry==Command.UPDATE):
        print("Updating entry. Any field you wish to leave unchanged, leave the input blank and press enter." )
        uInput= input('Enter Client Name: ')
        if uInput:
            data.update({'Client':uInput})
        uInput= input ('Enter Client Address:  ')
        if uInput:
            data.update({'clientAddress':uInput})
        uInput =input('Enter Client Contact: ')
        if uInput:
            data.update({'clientContact':uInput})
        query= ("UPDATE clients SET client_name=%(Client)s, client_address=%(clientAddress)s, contact_details=%(clientContact)s WHERE client_id="+ key )
        
    elif(updateEntry==Command.DELETE):
        query="SELECT * FROM clients WHERE client_id="+key
        printClient(cursor,query)
        uInput=input("Are you sure you want to delete this entry? (Y/N)")
        if uInput=='Y':
            query= "DELETE FROM clients WHERE client_id="+key
            deleteEntry(query)
        elif uInput=='N':
            print("Discarding DELETE query")
                
    return query,data
        

def inventoryEntry(updateEntry,data,key):
    if(updateEntry==Command.INSERT):
        client_id=input('Enter Client ID (Foreign Key): ')
        description=input('Enter Description: ')
        quantity= input('Enter quantity: ')
        box_id= input('Enter Box ID (Foreign Key): ')
        query= ("INSERT INTO inventory (client_id, description, quantity, box_id) VALUES (%(client_id)s, %(description)s, %(quantity)s, %(box_id)s)")
        data ={
                            'client_id':client_id,
                            'description':description,
                            'quantity':quantity,
                            'box_id':box_id
                        }
        
    elif (updateEntry==Command.UPDATE):
        print("Updating entry. Any field you wish to leave unchanged, leave the input blank and press enter." )
        uInput= input('Enter Client ID (Foreign Key): ')
        if uInput:
            data.update({'client_id':uInput})
        uInput= input ('Enter Description: ')
        if uInput:
            data.update({'description':uInput})
        uInput=input('Enter quantity: ')
        if uInput:
            data.update({'quantity':uInput})
        uInput =input('Enter Box ID (Foreign Key): ')
        if uInput:
            data.update({'box_id':uInput})
        query= ("UPDATE inventory SET client_id=%(client_id)s, description=%(description)s, quantity=%(quantity)s, box_id:=%(box_id)s WHERE inventory_id="+ key )
        
    elif(updateEntry==Command.DELETE):
        query="SELECT * FROM inventory WHERE inventory_id="+key
        printClient(cursor,query)
        uInput=input("Are you sure you want to delete this entry? (Y/N)")
        if uInput=='Y':
            query= "DELETE FROM inventory WHERE inventory_id="+key
            deleteEntry(query)
        elif uInput=='N':
            print("Discarding DELETE query")
        
    return query, data

def boxInfoEntry(updateEntry,data,key):
    if(updateEntry==Command.INSERT):
        box_label=input('Enter box label: ')
        dimensions= input('Enter dimensions (LxHxW): ')
        weight= input('Enter Weight: ')
        pallet_id =input('Enter Pallet Id (Foreign Key): ')
        query=("INSERT INTO boxes (box_label, dimensions, weight, pallet_id) VALUES(%(box_label)s,%(dimensions)s,%(weight)s,%(pallet_id)s)")
        data ={
                            'box_label':box_label,
                            'dimensions':dimensions,
                            'weight':weight,
                            'pallet_id':pallet_id
                        }
        
    elif (updateEntry==Command.UPDATE):
        print("Updating entry. Any field you wish to leave unchanged, leave the input blank and press enter." )
        uInput= input('Enter box label: ')
        if uInput:
            data.update({'box_label':uInput})
        uInput= input ('Enter dimensions (LxHxW): ')
        if uInput:
            data.update({'dimensions':uInput})
        uInput=input('Enter Weight: ')
        if uInput:
            data.update({'weight':uInput})
        uInput =input('Enter Pallet Id (Foreign Key): ')
        if uInput:
            data.update({'pallet_id':uInput})
        query= ("UPDATE boxes SET box_label=%(box_label)s, dimensions=%(dimensions)s, weight=%(weight)s, pallet_id:=%(pallet_id)s WHERE box_id="+ key )
        
    elif(updateEntry==Command.DELETE):
        query="SELECT * FROM boxes WHERE box_id="+key
        printClient(cursor,query)
        uInput=input("Are you sure you want to delete this entry? (Y/N)")
        if uInput=='Y':
            query= "DELETE FROM boxes WHERE box_id="+key
            deleteEntry(query)
        elif uInput=='N':
            print("Discarding DELETE query")
    
    return query, data

def palletInfoEntry(updateEntry,data,key):
    if(updateEntry==Command.INSERT):
        pallet_label=input('Enter pallet Label: ')
        pallet_quality= input('Enter pallet Quality: ')
        capacity= input('Enter pallet capacity: ')
        query= ("INSERT INTO pallets (pallet_label, pallet_quality, capacity) VALUES (%(pallet_label)s, %(pallet_quality)s, %(capacity)s)")
        data ={
                            'pallet_label':pallet_label,
                            'pallet_quality':pallet_quality,
                            'capacity':capacity
                        }
        
    elif (updateEntry==Command.UPDATE):
        print("Updating entry. Any field you wish to leave unchanged, leave the input blank and press enter." )
        uInput= input('Enter pallet Label: ')
        if uInput:
            data.update({'pallet_label':uInput})
        uInput= input ('Enter pallet Quality:  ')
        if uInput:
            data.update({'pallet_quality':uInput})
        uInput =input('Enter pallet capacity: ')
        if uInput:
            data.update({'capacity':uInput})
        query= ("UPDATE clipalletsents SET pallet_label=%(pallet_label)s, pallet_quality=%(pallet_quality)s, capacity=%(capacity)s WHERE pallet_id="+ key )
        
    elif(updateEntry==Command.DELETE):
        query="SELECT * FROM pallets WHERE pallet_id="+key
        printClient(cursor,query)
        uInput=input("Are you sure you want to delete this entry? (Y/N)")
        if uInput=='Y':
            query= "DELETE FROM palleta WHERE pallet_id="+key
            deleteEntry(query)
        elif uInput=='N':
            print("Discarding DELETE query")
        
    return query, data
        
    
def palletMovementEntry(updateEntry,data,key):
    if(updateEntry==Command.INSERT):
        pallet_id= input('Enter Pallet ID (Foregin Key): ')
        from_zone= input ('Enter starting zone: ')
        to_zone =input('enter end zone: ')
        barcode= input ('Enter barcode: ')
        query= ("INSERT INTO pallet_movements (pallet_id, from_zone, to_zone, barcode) VALUES (%(pallet_id)s, %(from_zone)s, %(to_zone)s, %(barcode)s)")
        data ={
                'pallet_id':pallet_id,
                'from_zone':from_zone,
                'to_zone':to_zone,
                'barcode':barcode
                        }
        
    elif(updateEntry==Command.UPDATE):
        print("Updating entry. Any field you wish to leave unchanged, leave the input blank and press enter." )
        uInput= input('Enter Pallet ID (Foregin Key): ')
        if uInput:
            data.pallet_id=uInput
        uInput= input ('Enter starting zone: ')
        if uInput:
            data.from_zone=uInput
        uInput =input('enter end zone: ')
        if uInput:
            data.to_zone=uInput
        uInput= input ('Enter barcode: ')
        if uInput:
            data.update({'barcode':uInput})
        query= ("UPDATE pallet_movements SET pallet_id=%(pallet_id)s, from_zone=%(from_zone)s, to_zone=%(to_zone)s, barcode=%(barcode)s WHERE movement_id="+ key )
        
    elif(updateEntry==Command.DELETE):
        query="SELECT * FROM pallet_movements WHERE movement_id="+key
        printClient(cursor,query)
        uInput=input("Are you sure you want to delete this entry? (Y/N)")
        if uInput=='Y':
            query= "DELETE FROM pallet_movements WHERE movement_id="+key
            deleteEntry(query)
        elif uInput=='N':
            print("Discarding DELETE query")
        
    return query,data

#print functions

def printClient(cursor, query):
    sendQuery(cursor,query)
    try:
        for (client_id,client_name,client_address,contact_details) in cursor:
            print("Id: {}, Client: {}, Address: {}, Contact: {}".format(client_id,client_name,client_address,contact_details))
        data ={
                                'Client':client_name,
                                'clientAddress':client_address,
                                'clientContact':contact_details
                            }
        return data
    except:
        print("Query returned no result or something went wrong")

def printInventory(cursor, query):
    sendQuery(cursor,query)
    try:
        for (inventory_id,client_id,description,quantity,box_id) in cursor:
            print("ID: {}, Client ID: {}, description: {}, quality: {}, box ID: {}".format(inventory_id,client_id,description,quantity,box_id))
        data ={
                                'client_id':client_id,
                                'description':description,
                                'quantity':quantity,
                                'box_id':box_id
                            }
        return data
    except:
        print("Query returned no result or something went wrong")

def printBoxes(cursor, query):
    sendQuery(cursor,query)
    try:
        for(box_id, box_label, dimensions, weight, pallet_id) in cursor:
            print("ID: {}, Box_label: {}, Dimensions: {}, Weight: {}, Pallet_id: {} ".format(box_id, box_label, dimensions, weight, pallet_id))
        data ={
                                'box_label':box_label,
                                'dimensions':dimensions,
                                'weight':weight,
                                'pallet_id':pallet_id
                            }
        return data
    except:
        print("Query returned no result or something went wrong")

def printPallets(cursor, query):
    sendQuery(cursor,query)
    try:
        for ( pallet_id,pallet_label, pallet_quality, capacity) in cursor:
            print("ID: {}, Label: {}, Quality: {}, capacity: {}".format(pallet_id,pallet_label, pallet_quality, capacity))
            
        data ={
                                'pallet_label':pallet_label,
                                'pallet_quality':pallet_quality,
                                'capacity':capacity
                            }
        return data
    except:
        print("Query returned no result or something went wrong")

def printPalletMovements(cursor, query):
    sendQuery(cursor,query)
    try:
        for (movement_id, pallet_id, timestamp, from_zone, to_zone, barcode)in cursor:
            print("ID: {}, Pallet ID: {}, Timestamp: {}, From: {}, To: {}, Barcode: {}".format(movement_id, pallet_id, timestamp, from_zone, to_zone, barcode))
            
            data ={
                                'pallet_id':pallet_id,
                                'from_zone':from_zone,
                                'to_zone':to_zone,
                                'barcode':barcode
                                }
            return data
    except:
        print("Query returned no result or something went wrong")
#Main Loop starts here vvv

while exit==False:
        userin = input('\n Do you want to enter data (1), view data(2), Update data(3), delete data (4) make commit(5), rollback changes(6), change commit settings(7), or exit(8)? ')
        match userin:
            #Data Insert
            case '1':
                
                tableSelect = input ('Avaliable Tables: Client Info (1), Inventory (2), Boxes Info (3), Pallet Info (4), Pallet Movement (5) ')
                query =""
                data ={}
                match tableSelect:
                    case '1':
                        query, data = clientEntry(Command.INSERT,data,0)
                        
                    case '2':
                        query, data =  inventoryEntry(Command.INSERT,data,0)
                        
                        
                    case '3':
                        query, data = boxInfoEntry(Command.INSERT,data,0)
                        
                        
                    case '4':
                        query, data = palletInfoEntry(Command.INSERT,data,0)
                        
                        
                    case '5':
                        query, data = palletMovementEntry(Command.INSERT,data,0)
                        
                    case _:
                        print("Unknown Input, no changes made")
                        
                ValidateEntry(query, data)
                
            #Data Search
            case '2':
                uInput= input ("View all entries in a table or search by key? (All/Search): ")
                if (uInput=="All"):
                    tableSelect= input ('Avaliable Tables: Client Info (1), Inventory (2), Boxes Info (3), Pallet Info (4), Pallet Movement (5),')
                    match tableSelect:
                        
                                case '1':
                                    query ="SELECT * FROM clients"
                                    printClient(cursor, query)
                                        
                                case '2':
                                    query = "SELECT * FROM inventory"
                                    printInventory(cursor, query)
                                        
                                case '3': 
                                    query = "SELECT * FROM boxes"
                                    printBoxes(cursor, query)
                                        
                                case '4':
                                    query = "SELECT * FROM pallets"
                                    printPallets(cursor, query)
                                        
                                case '5':
                                    query = "SELECT * FROM pallet_movements"
                                    printPalletMovements(cursor, query)
                                case _:
                                    print("Unknown Input, no changes made")
                elif(uInput=="Search"):
                    tableSelect= input ('Avaliable Tables: Client Info (1), Inventory (2), Boxes Info (3), Pallet Info (4), Pallet Movement (5) ')
                    match tableSelect:
                        
                                case '1':
                                    fieldSelect=input( "Available fields: Client ID (1), client name (2), client address (3), contact_details (4)")
                                    
                                    match fieldSelect:
                                    
                                        case "1":
                                            searchParam= input("Input desired client ID: ")
                                            query= "SELECT * FROM clients WHERE client_id="+searchParam
                                        case "2":
                                            searchParam= input("Input desired client name: ")
                                            query= "SELECT * FROM clients WHERE client_name="+searchParam
                                        case "3":
                                            searchParam= input("Input desired client address: ")
                                            query= "SELECT * FROM clients WHERE client_address="+searchParam
                                        case "4":
                                            searchParam= input("Input desired client contact: ")
                                            query= "SELECT * FROM clients WHERE contact_details="+searchParam
                                        
                                    printClient(cursor, query)
                                        
                                case '2':
                                    fieldSelect=input( "Available fields: Invetory ID (1), client ID (2), description (3), quantity (4), box id (5)")
                                    
                                    match fieldSelect:
                                    
                                        case "1":
                                            searchParam= input("Input desired Inventory ID: ")
                                            query= "SELECT * FROM inventory WHERE inventory_id="+searchParam
                                        case "2":
                                            searchParam= input("Input desired client ID: ")
                                            query= "SELECT * FROM inventory WHERE client_id="+searchParam
                                        case "3":
                                            searchParam= input("Input desired description: ")
                                            query= "SELECT * FROM inventory WHERE description="+searchParam
                                        case "4":
                                            searchParam= input("Input desired quantity: ")
                                            query= "SELECT * FROM inventory WHERE quantity="+searchParam
                                        case "5":
                                            searchParam= input("Input desired box ID: ")
                                            query= "SELECT * FROM inventory WHERE box_id="+searchParam
                                    printInventory(cursor, query)
                                        
                                case '3': 
                                    fieldSelect=input( "Available fields: Box ID (1), box label (2), dimensions (3), weight (4), pallet_id (5)")
                                    
                                    match fieldSelect:
                                    
                                        case "1":
                                            searchParam= input("Input desired box ID: ")
                                            query= "SELECT * FROM boxes WHERE box_id="+searchParam
                                        case "2":
                                            searchParam= input("Input desired box label: ")
                                            query= "SELECT * FROM boxes WHERE box_label="+searchParam
                                        case "3":
                                            searchParam= input("Input desired dimensions: ")
                                            query= "SELECT * FROM boxes WHERE dimensions="+searchParam
                                        case "4":
                                            searchParam= input("Input desired weight: ")
                                            query= "SELECT * FROM boxes WHERE weight="+searchParam
                                        case "5":
                                            searchParam= input("Input desired pallet id: ")
                                            query= "SELECT * FROM boxes WHERE pallet_id="+searchParam
                                    printBoxes(cursor, query)
                                        
                                case '4':
                                    fieldSelect=input( "Available fields: pallet ID (1), pallet label (2), pallet quality (3), capacity (4)")
                                    
                                    match fieldSelect:
                                    
                                        case "1":
                                            searchParam= input("Input desired pallet ID: ")
                                            query= "SELECT * FROM pallets WHERE pallet_id="+searchParam
                                        case "2":
                                            searchParam= input("Input desired client name: ")
                                            query= "SELECT * FROM pallets WHERE pallet_label="+searchParam
                                        case "3":
                                            searchParam= input("Input desired client address: ")
                                            query= "SELECT * FROM pallets WHERE pallet_quality="+searchParam
                                        case "4":
                                            searchParam= input("Input desired client contact: ")
                                            query= "SELECT * FROM pallets WHERE capacity="+searchParam
                                    printPallets(cursor, query)
                                        
                                case '5':
                                    fieldSelect=input( "Available fields: movement ID (1), pallet id (2), from zone (3), to zone (4), barcode (5)")
                                    
                                    match fieldSelect:
                                    
                                        case "1":
                                            searchParam= input("Input desired movement ID: ")
                                            query= "SELECT * FROM pallet_movements WHERE movement_id="+searchParam
                                        case "2":
                                            searchParam= input("Input desired client name: ")
                                            query= "SELECT * FROM pallet_movements WHERE pallet_id="+searchParam
                                        case "3":
                                            searchParam= input("Input desired from zone: ")
                                            query= "SELECT * FROM pallet_movements WHERE from_zone="+searchParam
                                        case "4":
                                            searchParam= input("Input desired to zone: ")
                                            query= "SELECT * FROM pallet_movements WHERE to_zone="+searchParam
                                        case "5":
                                            searchParam= input("Input desired barcode: ")
                                            query= "SELECT * FROM pallet_movements WHERE barcode="+searchParam
                                    printPalletMovements(cursor, query)
                                case _:
                                    print("Unknown Input, no changes made")
                else:
                    print("Unknown Input, returning to root menu")
            
            #Data Update
            case '3':
                print("update")   
                tableSelect= input ('Avaliable Tables: Client Info (1), Inventory (2), Boxes Info (3), Pallet Info (4), Pallet Movement (5) ')
                match tableSelect:
                            case '1':
                                query ="SELECT * FROM clients"
                                printClient(cursor,query)
                                key=input("Select the entry you want to update by the ID key: ")
                                query = "SELECT * FROM clients WHERE client_id = {}".format(key)
                                data =printClient(cursor,query)
                                query,data = clientEntry(Command.UPDATE,data,key)
                                    
                            case '2':
                                query = "SELECT * FROM inventory"
                                printInventory(cursor,query)
                                key=input("Select the entry you want to update by the ID key: ")
                                query = "SELECT * FROM inventory WHERE inventory_id = {}".format(key)
                                data= printInventory(cursor,query)
                                query,data = inventoryEntry(Command.UPDATE,data,key)
                                
                            case '3': 
                                query = "SELECT * FROM boxes"
                                printBoxes(cursor,query)
                                key=input("Select the entry you want to update by the ID key: ")
                                query = "SELECT * FROM boxes WHERE box_id = {}".format(key)
                                data =printBoxes(cursor,query)
                                query,data = boxInfoEntry(Command.UPDATE,data,key)
                                    
                            case '4':
                                query = "SELECT * FROM pallets"
                                printPallets(cursor,query)
                                key=input("Select the entry you want to update by the ID key: ")
                                query = "SELECT * FROM pallet WHERE pallet_id = {}".format(key)
                                data =printPallets(cursor,query)
                                query,data = palletInfoEntry(Command.UPDATE,data,key)
                                
                                    
                            case '5':
                                query = "SELECT * FROM pallet_movements"
                                printPalletMovements(cursor,query)
                                key=input("Select the entry you want to update by the ID key: ")
                                query = "SELECT * FROM pallet_movements WHERE movement_id = {}".format(key)
                                data=printPalletMovements(cursor,query)
                                query,data =palletMovementEntry(Command.UPDATE,data,key)
                                
                            case _:
                                print("Unknown Input, no changes made")
                ValidateEntry(query, data) 
            
            
            case '4':
                tableSelect = input (' Avaliable Tables: Client Info (1), Inventory (2), Boxes Info (3), Pallet Info (4), Pallet Movement (5) ')
                data={
                        
                    }
                match tableSelect:
                    
                    
                    case "1":
                        deletionKey= input ("Input the primary key for the entry you wish to delete: ")
                        clientEntry(Command.DELETE,data,deletionKey)
                    case "2":
                        deletionKey= input ("Input the primary key for the entry you wish to delete: ")
                        inventoryEntry(Command.DELETE,data,deletionKey)
                    case "3":
                        deletionKey= input ("Input the primary key for the entry you wish to delete: ")
                        boxInfoEntry(Command.DELETE,data,deletionKey)
                    case "4":
                        deletionKey= input ("Input the primary key for the entry you wish to delete: ")
                        palletInfoEntry(Command.DELETE,data,deletionKey)
                    case "5":
                        deletionKey= input ("Input the primary key for the entry you wish to delete: ")  
                        palletMovementEntry(Command.DELETE,data,deletionKey)      
                    
                        
                
            
            #Manual Commit              
            case '5':
                commitToDatabase()
            
            #Rollback 
            case '6':
                    uInput=input("Rollback all unsaved changes? (Y/N): ")
                    if uInput=="Y":
                        try:
                            cnx.rollback()
                            print("Rollback sent to server")
                        except mysql.connector.Error as e:
                            print("Something went wrong: {}".format(e))
                            
                    elif uInput=="N":
                        print("All changes have been kept")
                    else:
                        print("Unknown input, No changes made")
            
            #Commit Ask Option
            case '7':
                uInput=input("Do you want to be asked to commit after each update and creation? (Y/N): ")
                if(input=="Y"):
                    askAfterChanges=True
                    print("System will ask after each change if you want to commit.")
                elif(input=="N"):
                    askAfterChanges=False
                    print("System will not ask to commit after each change.")
                else:
                    print("Unknown Input, No changes made")
            
            #Exit program
            case '8':
                exit=True
                
            #For any other input
            case _:
                print("Unknown Input")
                        



cursor.close()
cnx.close()