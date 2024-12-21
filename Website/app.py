import json
from flask import Flask, render_template ,request, Response, redirect,jsonify
import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread
import src.FinalFile as dylanPro
import cv2
from pyzbar.pyzbar import decode
import mysql.connector
from datetime import datetime
from ultralytics import YOLO



from pyzbar.pyzbar import decode

from flask_mysqldb import MySQL
from flask import Flask
from enum import Enum
import mysql.connector as work

#db = SQLAlchemy()
try:
    os.mkdir('./static/frames')
except OSError as error:
    pass


app= Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= 'w+XdW6dnK8L_GP5'
# CHANGE to YOUR database name, with a slash added as shown
app.config['MYSQL_DB'] = 'capstone'

mysql=MySQL(app)
#b.init_app(app)



autoCommit= False
askAfterChanges=True

tString= "String"


def sendQuery(cursor,query):
    try:
        cursor.execute(query)
        return True
    except Exception as e:
        print ("An error has occured: {}".format(e))
        return False

def deleteEntryW(query,data):
    print("In special Delete")
    cnx= work.connect(user='test',password='test123',host='25.52.190.77',database='Capstone')
    cursorc = cnx.cursor()
    for key, value in data.items():
        print(f"{key}:{value}")
    print(query)
    try:
            cursorc.execute(query, data)
            print("Changes written to database.")
        
            cnx.commit()
            cursorc.close()
            cnx.close()
            return True
    except work.Error as e:
            print ("An error has occured: {}".format(e))
            cursorc.close()
            cnx.close()
            return False
        

    

def ValidateEntry (query,data,cursor):
        for key, value in data.items():
            print(f"{key}:{value}")
        print(query)
        try:
            cursor.execute(query, data)
            print("Changes written to database.")
            mysql.connection.commit()
            return True
        except Exception as e:
            print ("An error has occured: {}".format(e))
            return False
                 
    # elif uInput=="N":
    #     print("Discarding data")
    # else:
    #     print("Unknown Input")
    
def deleteEntry(query,cursor):
    if sendQuery(cursor,query):
        print("Successfully deleted")
        mysql.connection.commit()
            
    else:
        print("Delete was unsucessful")


#print functions

def printClient(cursor, query):
    sendQuery(cursor,query)
    try:
        for (client_id,client_name,client_address,contact_details) in cursor:
            print("Id: {}, Client: {}, Address: {}, Contact: {}".format(client_id,client_name,client_address,contact_details))
            data =[{
                                'Client_id':client_id,
                                'Client':client_name,
                                'clientAddress':client_address,
                                'clientContact':contact_details
                            }for (client_id,client_name,client_address,contact_details) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")

def printInventory(cursor, query):
    sendQuery(cursor,query)
    try:
        for (inventory_id,client_id,description,quantity,box_id) in cursor:
            print("ID: {}, Client ID: {}, description: {}, quality: {}, box ID: {}".format(inventory_id,client_id,description,quantity,box_id))
            data =[{
                                'inventory_id':inventory_id,
                                'client_id':client_id,
                                'description':description,
                                'quantity':quantity,
                                'box_id':box_id
                            }for (inventory_id,client_id,description,quantity,box_id) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")

def printBoxes(cursor, query):
    sendQuery(cursor,query)
    try:
        for(box_id, box_label, length,width,height, weight, pallet_id) in cursor:
            print("ID: {}, Box_label: {}, Lenght:{},Width:{}, Height:{}, Weight: {}, Pallet_id: {} ".format(box_id, box_label,length,width,height, weight, pallet_id))
            data =[{
                                'box_id':box_id,
                                'box_label':box_label,
                                'length':length,
                                'width':width,
                                'height':height,
                                'weight':weight,
                                'pallet_id':pallet_id
                            }for (box_id, box_label, length,width,height, weight, pallet_id) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")

def printPallets(cursor, query):
    sendQuery(cursor,query)
    try:
        for ( pallet_id,pallet_label, pallet_quality, capacity) in cursor:
            print("ID: {}, Label: {}, Quality: {}, capacity: {}".format(pallet_id,pallet_label, pallet_quality, capacity))
            
            data =[{
                                'pallet_id':pallet_id,
                                'pallet_label':pallet_label,
                                'pallet_quality':pallet_quality,
                                'capacity':capacity
                            }for (pallet_id,pallet_label, pallet_quality, capacity) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")

def printPalletMovements(cursor, query):
    sendQuery(cursor,query)
    try:
        for (movement_id, pallet_id, timestamp, from_zone, to_zone, barcode)in cursor:
            print("ID: {}, Pallet ID: {}, Timestamp: {}, From: {}, To: {}, Barcode: {}".format(movement_id, pallet_id, timestamp, from_zone, to_zone, barcode))
            
        data =[{
            'movement_id':movement_id,
            'pallet_id':pallet_id,
            'from_zone':from_zone,
            'to_zone':to_zone,
            'barcode':barcode}for (movement_id, pallet_id, timestamp, from_zone, to_zone, barcode) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")
        
def printBarcode(cursor, query):
    sendQuery(cursor,query)
    try:
        for (scan_id,barcode_data , scan_time, zone)in cursor:
            print("ID: {}, Barcode Data: {}, Scan Time:{}, Zone: {}".format(scan_id, barcode_data, scan_time, zone))
            
        data =[{
            'scan_id':scan_id,
            'barcode_data':barcode_data,
            'scan_time':scan_time,
            'zone':zone}for (scan_id, barcode_data, scan_time, zone) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")
        
def printStacking(cursor, query):
    sendQuery(cursor,query)
    try:
        for (stack_id, pallet_id, box_id, stack_level)in cursor:
            print("Stack ID: {}, Pallet ID: {}, Box ID: {}, Stack Level: {}".format(stack_id, pallet_id, box_id, stack_level))
            
        data =[{
            'stack_id':stack_id,
            'pallet_id':pallet_id,
            'box_id':box_id,
            'stack_level':stack_level}for (stack_id, pallet_id, box_id, stack_level) in cursor]
        return data
    except:
        print("Query returned no result or something went wrong")


# def record(out):
#     global rec_frame
#     while(rec):
#         time.sleep(0.05)
#         out.write(rec_frame)
        

MAX_BOX_WIDTH = 1300
MAX_BOX_HEIGHT = 1300

# Database connection function
def connect_db():
    return work.connect(user='root',password='w+XdW6dnK8L_GP5',host='localhost',database='capstone')

# YOLO model initialization
Boxes = YOLO(r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\runs\detect\train2\weights\best.pt')

# Mapping zones to video file paths
video_zones = {
    'A': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\96.avi',
    'B': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\97.avi',
    'C': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\34.avi',
    'D': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\33.avi',
}

# Retrieve the last known zone for a barcode
def get_last_zone(barcodedata, cursor):
    query = "SELECT zone FROM barcode_scans WHERE barcode_data = %s ORDER BY scan_time DESC LIMIT 1"
    cursor.execute(query, (barcodedata,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

# Insert a new zone scan for a barcode
def insert_zone_scan(barcodedata, zone, cursor, conn):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO barcode_scans (barcode_data, scan_time, zone) VALUES (%s, %s, %s)"
    cursor.execute(query, (barcodedata, timestamp, zone))
    conn.commit()

# Determine zone from coordinates
def get_zone_from_coordinates(x_center, y_center, frame_width, frame_height):
    half_width = frame_width / 2
    half_height = frame_height / 2
    if x_center < half_width and y_center < half_height:
        return 'A'
    elif x_center >= half_width and y_center < half_height:
        return 'B'
    elif x_center < half_width and y_center >= half_height:
        return 'C'
    else:
        return 'D'

# Draw grid on the frame
def draw_grid(frame):
    height, width, _ = frame.shape
    step_x = width // 2
    step_y = height // 2

    # Draw grid lines
    for x in range(1, 2):
        cv2.line(frame, (x * step_x, 0), (x * step_x, height), (255, 0, 0), 2)
    for y in range(1, 2):
        cv2.line(frame, (0, y * step_y), (width, y * step_y), (255, 0, 0), 2)

    # Add zone labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    zones = ['Zone A', 'Zone B', 'Zone C', 'Zone D']
    for i, label in enumerate(zones):
        col = i % 2
        row = i // 2
        x = col * step_x + 10
        y = (row + 1) * step_y - 10
        cv2.putText(frame, label, (x, y), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    return frame

# Display zone footage with YOLO detections
def display_zone_video(barcodedata, zone, cursor, conn):
    video_path = video_zones.get(zone)
    if not video_path:
        print(f"No video found for Zone {zone}.")
        return

    cap = cv2.VideoCapture(video_path)
    last_zone = zone

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Draw grid on the footage
        frame = draw_grid(frame)

        # YOLO detections
        results = Boxes(frame)
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width_box, height_box = x2 - x1, y2 - y1

            # Enforce maximum box size
            if width_box > MAX_BOX_WIDTH or height_box > MAX_BOX_HEIGHT:
                continue

            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            new_zone = get_zone_from_coordinates(x_center, y_center, frame.shape[1], frame.shape[0])

            # Draw green bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Annotate with barcode data
            cv2.putText(frame, f"Barcode: {barcodedata}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Handle zone change
            if new_zone != last_zone:
                print(f"Object linked to Barcode {barcodedata} moved to new zone: {new_zone}. Updating database...")
                insert_zone_scan(barcodedata, new_zone, cursor, conn)
                last_zone = new_zone

        # After all annotations are done, we consider frame as annotated_frame
        annotated_frame = frame

        # Resize and add the zone name in the center
        resized_frame = cv2.resize(annotated_frame, (1000, 800))
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(f"Zone {zone}", font, 1, 2)[0]
        text_x = (resized_frame.shape[1] - text_size[0]) // 2
        cv2.putText(resized_frame, f"Zone {zone}", (text_x, 50), font, 1, (255, 255, 255), 2)

        cv2.imshow(f"Zone {zone}", resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main function
def dylanMain():
    conn = connect_db()
    cursor = conn.cursor()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Barcode detection
        barcodes = decode(frame)
        for barcode in barcodes:
            barcodedata = barcode.data.decode('utf-8')
            last_zone = get_last_zone(barcodedata, cursor)

            if last_zone:
                print(f"Barcode {barcodedata} found in Zone {last_zone}.")
                # Give user options when barcode is found
                while True:
                    choice = input("Enter '1' to view zone footage or '2' to change barcode zone: ").strip()
                    if choice == '1':
                        # View zone footage
                        display_zone_video(barcodedata, last_zone, cursor, conn)
                        break
                    elif choice == '2':
                        # Change barcode zone
                        while True:
                            new_zone = input("Enter a new a zone (A,B,C,D): ").strip().upper()
                            if new_zone in video_zones:
                                insert_zone_scan(barcodedata, new_zone, cursor, conn)
                                print(f"Assigned Zone {new_zone} to Barcode {barcodedata}.")
                                display_zone_video(barcodedata, new_zone, cursor, conn)
                                break
                            else:
                                print("Invalid input. Please enter a valid zone (A,B,C,D):")
                        break
                    else:
                        print("Invalid choice. Please enter '1' or '2'.")
            else:
                # If barcode not in database, assign a zone
                print(f"Barcode {barcodedata} not found. Please enter a valid zone (A,B,C,D):")
                while True:
                    zone = input("Please give barcode a zone (A,B,C,D): ").strip().upper()
                    if zone in video_zones:
                        insert_zone_scan(barcodedata, zone, cursor, conn)
                        print(f"Assigned Zone {zone} to Barcode {barcodedata}.")
                        display_zone_video(barcodedata, zone, cursor, conn)
                        break
                    else:
                        print("Invalid input. Please give barcode a zone (A,B,C,D): ")

        # Resize the barcode scanner
        resized_frame = cv2.resize(frame, (700, 700))
        cv2.imshow("Barcode Scanner", resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    conn.close()
    cv2.destroyAllWindows()

# Main function
def ffgfg():

    print("checkpoint 0")
    conn = connect_db()
    cursor = conn.cursor()
    cap = cv2.VideoCapture(0)

    print("checkpoint 1")

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        print("checkpoint 2")
        # Barcode detection
        barcodes = decode(frame)
        for barcode in barcodes:
            barcodedata = barcode.data.decode('utf-8')
            last_zone = get_last_zone(barcodedata, cursor)

            if last_zone:
                print(f"Barcode {barcodedata} found in Zone {last_zone}.")
                # Give user options when barcode is found
                while True:
                    choice = input("Enter '1' to view zone footage or '2' to change barcode zone: ").strip()
                    if choice == '1':
                        # View zone footage
                        display_zone_video(barcodedata, last_zone, cursor, conn)
                        break
                    elif choice == '2':
                        # Change barcode zone
                        while True:
                            new_zone = input("Enter a new a zone (A,B,C,D): ").strip().upper()
                            if new_zone in video_zones:
                                insert_zone_scan(barcodedata, new_zone, cursor, conn)
                                print(f"Assigned Zone {new_zone} to Barcode {barcodedata}.")
                                display_zone_video(barcodedata, new_zone, cursor, conn)
                                break
                            else:
                                print("Invalid input. Please enter a valid zone (A,B,C,D):")
                        break
                    else:
                        print("Invalid choice. Please enter '1' or '2'.")
            else:
                # If barcode not in database, assign a zone
                print(f"Barcode {barcodedata} not found. Please enter a valid zone (A,B,C,D):")
                while True:
                    zone = input("Please give barcode a zone (A,B,C,D): ").strip().upper()
                    if zone in video_zones:
                        insert_zone_scan(barcodedata, zone, cursor, conn)
                        print(f"Assigned Zone {zone} to Barcode {barcodedata}.")
                        display_zone_video(barcodedata, zone, cursor, conn)
                        break
                    else:
                        print("Invalid input. Please give barcode a zone (A,B,C,D): ")

        # Resize the barcode scanner
        resized_frame = cv2.resize(frame, (700, 700))
        cv2.imshow("Barcode Scanner", resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    conn.close()
    cv2.destroyAllWindows()



#Web App Starts Here 

@app.route('/startDylan')
def dylanStart():
    dylanMain()
    

# @app.route('/scanner/barcode')
# def scaning():
#     scannedBarcode=scan()

#     data={
#         'barcode':scannedBarcode
#     }
#     return jsonify(data)


# Home Route
@app.route('/')
def index():
    return render_template('home.html')


#Enter Data Routes
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/enterData')
def enterData():
    return render_template('enterData.html')

@app.route('/enterData/client',methods=['POST'])
def enterClientdata():
    try:
        
       #
        
        data =request.get_json()
        query=("INSERT INTO clients (client_name, client_address, contact_details) VALUES (%(clientName)s, %(clientAddress)s, %(clientContact)s)")
        
        print (data)
        cur=mysql.connection.cursor()
        
        ValidateEntry(query,data,cur)
       
        cur.close()
        response = {
                'error': False,
                'message':'Successfully inserted'
                         
            }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    

@app.route('/enterData/inventory',methods=['POST'])
def enterInventoryData():
    try:
        
        cur= mysql.connection.cursor()
        
        data =request.get_json()
        query= ("INSERT INTO inventory (client_id, description, quantity, box_id) VALUES (%(clientId)s, %(description)s, %(quantity)s, %(boxId)s)")
        ValidateEntry(query,data,cur)
        
        mysql.connection.commit()
        cur.close()
        
        response = {
                    'error': False,
                    'message':'Successfully inserted'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
    
@app.route('/enterData/pallets',methods=['POST'])
def enterpalletData():
    try:
       
        cur= mysql.connection.cursor()
        
        data =request.get_json()
        query= ("INSERT INTO pallets (pallet_label, pallet_quality, capacity) VALUES (%(palletLabel)s, %(palletQuality)s, %(palletCapacity)s)")
        
        
        ValidateEntry(query,data,cur)
        
        cur.close()
        response = {
                'error': False,
                'message':'Successfully inserted'
                         
            }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                        
            }
        return jsonify(response)
    
    
@app.route('/enterData/boxes',methods=['POST'])
def enterBoxData():
    try:
        
        cur= mysql.connection.cursor()
        
        data =request.get_json()
        
        query=("INSERT INTO boxes (box_label, dimensions, weight, pallet_id) VALUES(%(boxLabel)s,%(dimensions)s,%(weight)s,%(palletId)s)")
        
        ValidateEntry(query,data,cur)
        
        cur.close()
        response = {
                'error': False,
                'message':'Successfully inserted'
                         
            }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
        
    
@app.route('/enterData/movement',methods=['POST'])
def enterMovementData():
    try:
        
        
        cur= mysql.connection.cursor()
        
        
        data =request.get_json()
        
        query= ("INSERT INTO pallet_movements (pallet_id, from_zone, to_zone, barcode) VALUES (%(pallet_Id)s, %(startZone)s, %(endZone)s, %(barcode)s)")
        
        ValidateEntry(query,data,cur)
        
        cur.close()
        response = {
                'error': False,
                'message':'Successfully inserted'
                         
            }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)



#View Data Routes
@app.route('/viewData')
def viewData():
    return render_template('viewData.html')

@app.route('/viewData/client/<string:field>/<param>',methods=['GET'])
def viewDataClient(field,param):
    try:
        print(type(param))
        if(type(param) is type(tString)):
            param= "'"+param+"'"
        
        print(field)
        print(param)
        
        cur= mysql.connection.cursor()
        
        query=('SELECT * FROM clients WHERE {} = {}'.format(field,param))
        
        print(query)
        
        data =printClient(cur,query)
        
        
        #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
        
        print(data)
        if(data):
            response = {
            'error':False,
            'message': "Items Fetched",
            'data':data
            }
        
            return jsonify(response),200
        else :
            response = {
            'error':True,
            'message': "No Items Fetched",
            
            }
            #return json.dumps(response)
    except Exception as e:
        print("error Retreiving data")
        response = {
            'error': True,
            'message': f'Error Occurred: {e}',
            'data': None         
        }
        
        # Return a JSON response with HTTP status code 500 (Internal Server Error)
        return jsonify(response), 500
    
@app.route('/viewData/inventory/<string:field>/<param>',methods=['GET'])
def viewDataInventory(field,param):
        try:
            
            print(field)
            print(param)
            if(type(param) is type(tString)):
                param= "'"+param+"'"
            cur= mysql.connection.cursor()
            
            query=('SELECT * FROM inventory WHERE {} = {}'.format(field,param))
            
            print(query)
            data =printInventory(cur,query)
            
            
            #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
            
            print(data)
            if(data):
                response = {
                'error':False,
                'message': "Items Fetched",
                'data':data
                }
            
                return jsonify(response),200
            else :
                response = {
                'error':True,
                'message': "No Items Fetched",
                
                }
                #return json.dumps(response)
        except Exception as e:
            print("error Retreiving data")
            response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
            
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500
            
            
@app.route('/viewData/movement/<string:field>/<param>',methods=['GET'])
def viewDataMovement(field,param):
            try:
                
                print(field)
                print(param)
                
                if(type(param) is type(tString)):
                    param= "'"+param+"'"
                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM pallet_movements WHERE {} = {}'.format(field,param))
                
                print(query)
                data =printPalletMovements(cur,query)
                
                
                #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
                
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    #return json.dumps(response)
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': True,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
            
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500
        
        
@app.route('/viewData/pallets/<string:field>/<param>',methods=['GET'])
def viewDataPallets(field,param):
            try:
                
                
                print(field)
                print(param)
                
                if(type(param) is type(tString)):
                    param= "'"+param+"'"
                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM pallets WHERE {} = {}'.format(field,param))
                
                print(query)
                data =printPallets(cur,query)
                
                
                #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
                
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    #return json.dumps(response)
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': True,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
            
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500
        
        
        
@app.route('/viewData/boxes/<string:field>/<param>',methods=['GET'])
def viewDataBoxes(field,param):
            try:
            
                print(field)
                print(param)
                
                if(type(param) is type(tString)):
                    param= "'"+param+"'"
                

                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM boxes WHERE {} = {}'.format(field,param))
                
                print(query)
                data =printBoxes(cur,query)
                
                
                #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
                
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    #return json.dumps(response)
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': True,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
            
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500

@app.route('/viewData/barcode/<string:field>/<param>',methods=['GET'])
def viewDataBarcode(field,param):
            try:
            
                print(field)
                print(param)
                
                if(type(param) is type(tString)):
                    param= "'"+param+"'"
                

                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM barcode_scans WHERE {} = {}'.format(field,param))
                
                print(query)
                data =printBarcode(cur,query)
                
                
                #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
                
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    #return json.dumps(response)
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': True,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
            
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500

@app.route('/viewData/stacking/<string:field>/<param>',methods=['GET'])
def viewDataStacking(field,param):
            try:
            
                print(field)
                print(param)
                
                if(type(param) is type(tString)):
                    param= "'"+param+"'"
                

                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM box_stacking WHERE {} = {}'.format(field,param))
                
                print(query)
                data =printStacking(cur,query)
                
                
                #items=[{'id':client_id,'name':client_name,'address':client_address,'contact':contact_details}for(client_id,client_name,client_address,contact_details) in cur]
                
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    #return json.dumps(response)
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': True,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
            
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500

@app.route('/viewData/viewAll/client',methods=['GET'])
def viewDataClientAll():
    try:
        
        cur= mysql.connection.cursor()
        
        query=('SELECT * FROM clients')
        data =printClient(cur,query)
        
        #results=cur.fetchall()
        
        #print(results)
        cur.close()
        
        #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
        print(data)
        if(data):
            response = {
            'error':False,
            'message': "Items Fetched",
            'data':data
            }
        
            return jsonify(response),200
        else :
            response = {
            'error':True,
            'message': "No Items Fetched",
            
            }
            return jsonify(response),500
    except Exception as e:
        print("error Retreiving data")
        response = {
            'error': False,
            'message': f'Error Occurred: {e}',
            'data': None         
        }
        
        # Return a JSON response with HTTP status code 500 (Internal Server Error)
        return jsonify(response), 500

@app.route('/viewData/viewAll/barcode',methods=['GET'])
def viewDataBarcodeAll():
    try:
        
        cur= mysql.connection.cursor()
        
        query=('SELECT * FROM barcode_scans')
        data =printBarcode(cur,query)
        
        #results=cur.fetchall()
        
        #print(results)
        cur.close()
        
        #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
        print(data)
        if(data):
            response = {
            'error':False,
            'message': "Items Fetched",
            'data':data
            }
        
            return jsonify(response),200
        else :
            response = {
            'error':True,
            'message': "No Items Fetched",
            
            }
            return jsonify(response),500
    except Exception as e:
        print("error Retreiving data")
        response = {
            'error': False,
            'message': f'Error Occurred: {e}',
            'data': None         
        }
        
        # Return a JSON response with HTTP status code 500 (Internal Server Error)
        return jsonify(response), 500
    
@app.route('/viewData/viewAll/stacking',methods=['GET'])
def viewDataStackingAll():
    try:
        
        cur= mysql.connection.cursor()
        
        query=('SELECT * FROM box_stacking')
        data =printStacking(cur,query)
        
        #results=cur.fetchall()
        
        #print(results)
        cur.close()
        
        #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
        print(data)
        if(data):
            response = {
            'error':False,
            'message': "Items Fetched",
            'data':data
            }
        
            return jsonify(response),200
        else :
            response = {
            'error':True,
            'message': "No Items Fetched",
            
            }
            return jsonify(response),500
    except Exception as e:
        print("error Retreiving data")
        response = {
            'error': False,
            'message': f'Error Occurred: {e}',
            'data': None         
        }
        
        # Return a JSON response with HTTP status code 500 (Internal Server Error)
        return jsonify(response), 500
    
@app.route('/viewData/viewAll/inventory',methods=['GET'])
def viewDataInventoryAll():
            try:
                
                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM inventory')
                data =printInventory(cur,query)
                
                #results=cur.fetchall()
                
                #print(results)
                cur.close()
                
                #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    return jsonify(response),500
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': False,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
        
            # Return a JSON response with HTTP status code 500 (Internal Server Error)
            return jsonify(response), 500
    
@app.route('/viewData/viewAll/pallets',methods=['GET'])
def viewDataPalletsAll():
            try:
                
                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM pallets')
                data =printPallets(cur,query)
                
                #results=cur.fetchall()
                
                #print(results)
                cur.close()
                
                #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    return jsonify(response),500
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': False,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
                
                # Return a JSON response with HTTP status code 500 (Internal Server Error)
                return jsonify(response), 500
    
@app.route('/viewData/viewAll/boxes',methods=['GET'])
def viewDataBoxesAll():
            try:
                
                cur= mysql.connection.cursor()
                
                query=('SELECT * FROM boxes')
                data =printBoxes(cur,query)
                
                #results=cur.fetchall()
                
                #print(results)
                cur.close()
                
                #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
                print(data)
                if(data):
                    response = {
                    'error':False,
                    'message': "Items Fetched",
                    'data':data
                    }
                
                    return jsonify(response),200
                else :
                    response = {
                    'error':True,
                    'message': "No Items Fetched",
                    
                    }
                    return jsonify(response),500
            except Exception as e:
                print("error Retreiving data")
                response = {
                    'error': False,
                    'message': f'Error Occurred: {e}',
                    'data': None         
                }
                
                # Return a JSON response with HTTP status code 500 (Internal Server Error)
                return jsonify(response), 500
    
@app.route('/viewData/viewAll/movement',methods=['GET'])
def viewDataMovementAll():
    try:
        
        cur= mysql.connection.cursor()
        
        query=('SELECT * FROM pallet_movements')
        data =printPalletMovements(cur,query)
        
        #results=cur.fetchall()
        
        #print(results)
        cur.close()
        
        #items=[{'id':item[0],'name':item[1],'address':item[2],'contact':item[3]}for item in results]
        print(data)
        if(data):
            response = {
            'error':False,
            'message': "Items Fetched",
            'data':data
            }
            
            return jsonify(response),200
        else :
            response = {
            'error':True,
            'message': "No Items Fetched",
            
            }
            return jsonify(response),500
    except Exception as e:
        print("error Retreiving data")
        response = {
            'error': False,
            'message': f'Error Occurred: {e}',
            'data': None         
        }
        
        # Return a JSON response with HTTP status code 500 (Internal Server Error)
        return jsonify(response), 500


#Update Data Routes
@app.route('/updateData')
def updateData():
    return render_template('updateData.html')

@app.route('/updateData/client',methods=['POST'])
def updateClientdata():
    try:
        data=request.get_json()
        
        print(data)
        
        query=('UPDATE clients SET client_name=%(NewClientName)s, client_address=%(NewClientAddress)s, contact_details=%(newClientContact)s WHERE client_id=%(clientId)s')
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully updated'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully updated'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/updateData/inventory',methods=['POST'])
def updateInventorydata():
    try:
        data=request.get_json()
        
        print(data)
        
        query=('UPDATE inventory SET client_id=%(NewClientId)s, description=%(NewDescription)s, quantity=%(NewQuantity)s ,box_id=%(NewBoxId)s WHERE inventory_id=%(inventoryId)s')
      
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully updated'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully updated'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/updateData/pallets',methods=['POST'])
def updatePalletdata():
    try:
        data=request.get_json()
        
        print(data)
        
        query=('UPDATE pallets SET pallet_label=%(newPalletLabel)s, pallet_quality=%(newPalletQuality)s, capacity=%(newPalletCapacity)s WHERE pallet_id=%(palletId)s')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully updated'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully updated'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/updateData/boxes',methods=['POST'])
def updateBoxdata():
    try:
        data=request.get_json()
        
        print(data)
        
        query=('UPDATE boxes SET box_label=%(newBoxLabel)s, dimensions=%(newDimensions)s, weight=%(newWeight)s,pallet_id= %(newPalletId)s WHERE box_id=%(boxId)s')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully updated'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully updated'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/updateData/movement',methods=['POST'])
def updateMovementdata():
    try:
        data=request.get_json()
        
        print(data)
        
        query=('UPDATE pallet_movements SET pallet_id=%(NewPallet_Id)s, from_zone=%(NewStartZone)s, to_zone=%(NewEndZone)s,barcode=%(NewBarcode)s WHERE movement_id=%(movementId)s')
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully updated'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully updated'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
        
        
#Delete Data Routes
@app.route('/deleteData')
def deletePage():
    return render_template('deleteData.html')

@app.route('/deleteData/client/<field>/<id>',methods=["GET"])
def deleteClient(field,id):
    
    try:
        print(field)
        print (id)
        
        id= ("'"+id+"'")
        data={
            "field":field,
            "id":id
        }
        
        query=('DELETE FROM clients WHERE %(field)s = %(id)s ')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =deleteEntryW(query,data)
        
        if(boolVal):
            query=('SELECT * FROM clients WHERE %(field)s = %(id)s ')
            boolVal =ValidateEntry(query,data,cur)

        
        
        cur.close()
        if(boolVal==False):
            response = {
                    'error': False,
                    'message':'Successfully Deleted'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully Deleted'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
    
@app.route('/deleteData/inventory/<field>/<id>',methods=["GET"])
def deleteInventory(field,id):
    
    
    try:
        print(field)
        print (id)
       
        data={
            "field":field,
            "id":id
        }
        
        query=('DELETE FROM inventory WHERE %(field)s = %(id)s ')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully Deleted'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully Deleted'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/deleteData/boxes/<field>/<id>',methods=["GET"])
def deleteBox(field,id):
    
    
    
    try:
        print(field)
        print (id)
        
        
        data={
            "field":field,
            "id":id
        }
        
        query=('DELETE FROM boxes WHERE %(field)s = %(id)s ')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully Deleted'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully Deleted'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/deleteData/pallets/<field>/<id>',methods=["GET"])
def deletePallet(field ,id):
    
    
    try:
        print(field)
        print (id)
        
        
        data={
            "field":field,
            "id":id
        }
        
        query=('DELETE FROM pallets WHERE %(field)s = %(id)s ')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully Deleted'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully Deleted'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
@app.route('/deleteData/movement/<field>/<id>',methods=["GET"])
def deleteMovement(field,id):
    
    
    try:
        print(field)
        print (id)
        

                
        
        
        data={
            "field":field,
            "id":id
        }
        
        query=('DELETE FROM pallet_movements WHERE %(field)s = %(id)s ')
        
        
        
        cur=mysql.connection.cursor()
        
        boolVal =ValidateEntry(query,data,cur)
        
        
        cur.close()
        if(boolVal):
            response = {
                    'error': False,
                    'message':'Successfully Deleted'
                            
                }
        else:
             response = {
                    'error': True,
                    'message':'unsuccessfully Deleted'
                            
                }
        
        return jsonify(response)
    except Exception as e:
        response = {
                'error': True,
                'message': f'Error Occurred: {e}',
                'data': None         
            }
        return jsonify(response)
    
    
    
@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route('/video_feed')
def video_feed():
    return Response(scan(), mimetype='multipart/x-mixed-replace; boundary=frame')
    

@app.route('/commit')
def commit():
    return render_template('commit.html')

@app.route('/rollback')
def rollback():
    return render_template('rollback.html')

@app.route('/changeSetting')
def changeSetting():
    return render_template('changeSetting.html')

# @app.route('/test')
# def test():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text