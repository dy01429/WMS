import pytest;
import src.WarehouseAPItesting as WarehouseAPItesting;



def retrieve_Test():
    arr = ["2","Search","1","1"]
    assert WarehouseAPItesting.Main(arr)== "Id: 1, Client: Jackson, Address: 380 Hame road, Contact: 912-444-9999"
    
    arr = ["2","Search","1","25"]
    assert WarehouseAPItesting.Main(arr) =="Query returned no result or something went wrong"
    
def delete_Test():
    arr = [ "4","1","1","Y"] 
    assert WarehouseAPItesting.Main(arr) == "Delete was unsucessful"
    
    arr = [ "4","3","1","Y"] 
    assert WarehouseAPItesting.Main(arr) == "Successfully deleted"
    
def rollback_Test():
    arr = [ "4","3","1","Y"] 
    assert WarehouseAPItesting.Main(arr) == "Successfully deleted"
    
    arr= [ "2","3","1","1"]
    assert WarehouseAPItesting.Main(arr)== "Query returned no result or something went wrong"
    
