const clientB = document.getElementById('Clients');
const inventoryB = document.getElementById('Inventory');
const palletsB = document.getElementById('Pallets');
const boxesB = document.getElementById('Boxes');
const movementB = document.getElementById('Movement');

let tableUpdate = 'none'
selectedEntry = null

const subTab = document.createElement(`div`);

document.addEventListener('DOMContentLoaded', function () {

    clientB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableUpdate = "client"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select client by ID to update</strong></label><br>
                    <input type="number" placeholder="Client ID" name="ClientID" id="ID" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>

        `

        display.appendChild(subTab);

        const form = document.getElementById('GetForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

    })

    inventoryB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableUpdate = "inventory"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select inventory by ID to update</strong></label><br>
                    <input type="number" placeholder="Inventory ID" name="InventoryID" id="ID" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>

        `

        display.appendChild(subTab);

        const form = document.getElementById('GetForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

    })

    palletsB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableUpdate = "pallets"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select pallet by ID to update</strong></label><br>
                    <input type="number" placeholder="Pallet ID" name="PalletID" id="ID" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>

        `

        display.appendChild(subTab);

        const form = document.getElementById('GetForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

    })

    boxesB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableUpdate = "boxes"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select box by ID to update</strong></label><br>
                    <input type="number" placeholder="Box ID" name="BoxID" id="ID" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>

        `

        display.appendChild(subTab);

        const form = document.getElementById('GetForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

    })

    movementB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableUpdate = "movement"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select pallet movement by ID to update</strong></label><br>
                    <input type="number" placeholder="Pallet Movement ID" name="MovementID" id="ID" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>

        `

        display.appendChild(subTab);

        const form = document.getElementById('GetForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

    })

    function submitForm() {
        console.log('In submitForm...');

        FieldType = null

        switch (tableUpdate) {
            case "client":
                FieldType = 'client_id'
                break;
            case "inventory":
                FieldType = 'inventory_id';
                break;
            case "boxes":
                FieldType = 'box_id';
                break;
            case "pallets":
                FieldType = 'pallet_id';
                break;
            case "movement":
                FieldType = 'movement_id';
                break;
        }
        const SearchParam = document.getElementById('ID').value

        console.log('Field Type:', FieldType);
        console.log('Search Parameter:', SearchParam);


        fetch(`/viewData/${tableUpdate}/${FieldType}/${SearchParam}`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                results = document.getElementById('results');
                results.innerHTML = '';

                data.data.forEach(clientInfo => {
                    console.log(clientInfo)
                    displayResults(clientInfo)
                    selectedEntry = clientInfo;
                })
            })

            .catch(error => {
                console.error(`${tableUpdate} has no ${FieldType} that equals ${SearchParam}:`, error);
            });
    }
});

function displayResults(data) {
    results = document.getElementById('results');
    changeEntry = document.createElement('div')


    row = document.createElement(`div`);
    row.className="entry";
    switch (tableUpdate) {
        case "client":
            row.innerHTML = `ID: ${data.Client_id}, Client Name: ${data.Client}, Client Address: ${data.clientAddress}, Client Contact: ${data.clientContact} <br>`;

            subTab.innerHTML = `
               <form id="UpdateForm" method="POST" >
                <label> <strong>Update client details (leave fields blank that you want unchanged)</strong></label><br>
                
                    <input type="text" placeholder="Client Name" name="Client Name" id="Client Name" > <br>
                    <input type="text" placeholder="Client Address" name="Client Address" id="Client Address" > <br>
                    <input type="text" placeholder="Client Contact" name="Client Contact" id="Client Contact" > <br>
                <button type="submit" class="Submit">Submit</button>
                </form>
               
               `
            updateform = document.getElementById('UpdateForm')

            if (updateform) {
                console.log("Form found, setting up event listener");
                updateform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    updateEntry();
                });
            } else {
                console.error("Form element not found");
            }


            break;
        case "inventory":
            row.innerHTML = `ID: ${data.inventory_id}, Client ID: ${data.client_id}, Description: ${data.description}, Quantity: ${data.quantity}, Box ID: ${data.box_id} <br>`;

            subTab.innerHTML = `
        
                <form id="UpdateForm" method="POST" >
                        <label> <strong>Update new inventory details (leave fields blank that you want unchanged)</strong></label><br>
                        
                            <input type="text" placeholder="Client ID (Foreign Key)" name="clientId" id="clientId" > <br>
                            <input type="text" placeholder="Description" name="Description" id="Description" > <br>
                            <input type="text" placeholder="Quantity" name="Quantity" id="Quantity" > <br>
                            <input type="text" placeholder="Box ID (Foreign Key)" name="Box ID" id="Box ID" > <br>
                            <button type="submit" class="Submit">Submit</button>
                </form>`


            updateform = document.getElementById('UpdateForm')

            if (updateform) {
                console.log("Form found, setting up event listener");
                updateform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    updateEntry();
                });
            } else {
                console.error("Form element not found");
            }

            break;
        case "boxes":
            row.innerHTML = `ID: ${data.box_id}, Box Label: ${data.box_label}, Dimensions: ${data.dimensions}, Weight: ${data.weight}, Pallet ID: ${data.pallet_id} <br>`;

            subTab.innerHTML = `
        
                    <form id="UpdateForm" method="POST" >
                            <label> <strong>Update box details (leave fields blank that you want unchanged)</strong></label><br>
                            
                                <input type="text" placeholder="Box label" name="box label" id="box label" > <br>
                                <input type="text" placeholder="Dimensions (LxHxW)" name="dimensions" id="dimensions" > <br>
                                <input type="text" placeholder="Weight" name= Weight" id="Weight" > <br>
                                <input type="text" placeholder="Pallet Id (Foreign Key)" name="Pallet Id" id="Pallet Id" > <br>
                                <button type="submit" class="Submit">Submit</button>
                    </form>`

            updateform = document.getElementById('UpdateForm')

            if (updateform) {
                console.log("Form found, setting up event listener");
                updateform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    updateEntry();
                });
            } else {
                console.error("Form element not found");
            }
            break;
        case "pallets":
            row.innerHTML = `ID: ${data.pallet_id}, Pallet Label: ${data.pallet_label}, Pallet Quality: ${data.pallet_quality}, Capacity: ${data.capacity} <br>`;

            subTab.innerHTML = `
                <form id="UpdateForm" method="POST" >
                        <label> <strong>Update pallet details (leave fields blank that you want unchanged)</strong></label><br>
                        
                            <input type="text" placeholder="Pallet Label" name="Pallet Label" id="Pallet Label" > <br>
                            <input type="text" placeholder="Pallet Quality" name="Pallet Quality" id="Pallet Quality" > <br>
                            <input type="text" placeholder="Pallet Capacity" name="Pallet Capacity" id="Pallet Capacity" > <br>
                        <button type="submit" class="Submit">Submit</button>
                </form>
        
        `

            updateform = document.getElementById('UpdateForm')

            if (updateform) {
                console.log("Form found, setting up event listener");
                updateform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    updateEntry();
                });
            } else {
                console.error("Form element not found");
            }

            break;
        case "movement":
            row.innerHTML = `ID: ${data.movement_id}, Pallet ID: ${data.pallet_id}, From Zone: ${data.from_zone}, To Zone: ${data.to_zone}, Barcode: ${data.barcode} <br>`;




            subTab.innerHTML = `
                    <form id="UpdateForm" method="POST" >
                            <label> <strong>Update pallet movement details (leave fields blank that you want unchanged)</strong></label><br>
                            
                                <input type="text" placeholder="Pallet ID (Foreign Key)" name="Pallet ID" id="Pallet ID" > <br>
                                <input type="text" placeholder="Starting Zone" name="Starting Zone" id="Starting Zone" > <br>
                                <input type="text" placeholder="Ending Zone" name=" Ending Zone" id="Ending Zone" > <br>
                                <input type="text" placeholder="Barcode" name="Barcode" id="Barcode" > <br>
                                <button type="submit" class="Submit">Submit</button>
                    </form
                    
        `

            updateform = document.getElementById('UpdateForm')

            if (updateform) {
                console.log("Form found, setting up event listener");
                updateform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    updateEntry();
                });
            } else {
                console.error("Form element not found");
            }

            break;

    }
    updateform=document.getElementById("UpdateForm")
    updateform.classList.add("form");
    subTab.append(results)
    results.appendChild(row);
    results.after(changeEntry);


};
function updateEntry() {

    switch (tableUpdate) {
        case "client":
            NewClientName = document.getElementById("Client Name").value;
            NewClientAddress = document.getElementById("Client Address").value;
            newClientContact = document.getElementById("Client Contact").value;

            if (NewClientName == "")
                NewClientName = selectedEntry.Client
            if (NewClientAddress == "")
                NewClientAddress = selectedEntry.clientAddress
            if (newClientContact == "")
                newClientContact = selectedEntry.clientContact

            clientId = selectedEntry.Client_id;
            confirmation = confirm(`Are you sure the information is correct?\n Client Name: ${NewClientName}\n Client Address: ${NewClientAddress}\n Client Contact: ${newClientContact} `)
            if (confirmation) {
                fetch(`/updateData/client`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ NewClientName, NewClientAddress, newClientContact, clientId })
                })
                    .then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully updated.")
                        else
                            alert("Entry not updated.")

                        location.reload();
                    }

                    )
            } else {
                alert("Throwing away input.")

                location.reload();
            }

            break;

        case "inventory":

            NewClientId = document.getElementById("clientId").value;
            NewDescription = document.getElementById("Description").value;
            NewQuantity = document.getElementById("Quantity").value;
            NewBoxId = document.getElementById("Box ID").value;

            if (NewClientId == "")
                NewClientId = selectedEntry.client_id
            if (NewDescription == "")
                NewDescription = selectedEntry.description
            if (NewQuantity == "")
                NewQuantity = selectedEntry.quantity
            if (NewBoxId == "")
                NewBoxId = selectedEntry.box_id

            inventoryId = selectedEntry.inventory_id;

            confirmation = confirm(`Are you sure the information is correct?\n Client Id: ${NewClientId} \n Description: ${NewDescription}\n Quantity: ${NewQuantity} \n Box Id: ${NewBoxId} `)
            if (confirmation) {
                fetch(`/updateData/inventory`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ NewClientId, NewDescription, NewQuantity, NewBoxId, inventoryId })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Updated")
                        else
                            alert("Entry not Updated.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.")
                location.reload();
            }

            break;

        case "pallets":

            newPalletLabel = document.getElementById("Pallet Label").value;
            newPalletQuality = document.getElementById("Pallet Quality").value;
            newPalletCapacity = document.getElementById("Pallet Capacity").value;

            if (newPalletLabel == "")
                newPalletLabel = selectedEntry.pallet_label
            if (newPalletQuality == "")
                newPalletQuality = selectedEntry.pallet_quality
            if (newPalletCapacity == "")
                newPalletCapacity = selectedEntry.capacity
            palletId = selectedEntry.pallet_id;

            confirmation = confirm(`Are you sure the information is correct?\n Pallet Label:${newPalletLabel}\n Pallet Quality: ${newPalletQuality}\n Pallet Capacity: ${newPalletCapacity} `)
            if (confirmation) {

                fetch(`/updateData/pallets`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ newPalletLabel, newPalletQuality, newPalletCapacity, palletId })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Updated")
                        else
                            alert("Entry not Updated.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.")
                location.reload();
            }
            break;

        case "boxes":

            newBoxLabel = document.getElementById('box label').value;
            newDimensions = document.getElementById('dimensions').value;
            newWeight = document.getElementById('Weight').value;
            newPalletId = document.getElementById('Pallet Id').value;

            if (newBoxLabel == "")
                newBoxLabel = selectedEntry.box_label
            if (newDimensions == "")
                newDimensions = selectedEntry.dimensions
            if (newWeight == "")
                newWeight = selectedEntry.weight
            if (newPalletId == "")
                newPalletId = selectedEntry.pallet_id

            boxId = selectedEntry.box_id;

            confirmation = confirm(`Are you sure the information is correct?\n Box Label: ${newBoxLabel} \n Dimensions: ${newDimensions} \n Weight: ${newWeight} \n Pallet ID: ${newPalletId} `)
            if (confirmation) {

                fetch(`/updateData/boxes`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ newBoxLabel, newDimensions, newWeight, newPalletId, boxId })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Updated")
                        else
                            alert("Entry not Updated.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.");
                location.reload();
            }

            break;

        case "movement":

            NewPallet_Id = document.getElementById("Pallet ID").value;
            NewStartZone = document.getElementById("Starting Zone").value;
            NewEndZone = document.getElementById("Ending Zone").value;
            NewBarcode = document.getElementById("Barcode").value;

            if (NewPallet_Id == "")
                NewPallet_Id = selectedEntry.pallet_id
            if (NewStartZone == "")
                NewStartZone = selectedEntry.from_zone
            if (NewEndZone == "")
                NewEndZone = selectedEntry.to_zone
            if (NewBarcode == "")
                NewBarcode = selectedEntry.barcode

            movementId = selectedEntry.movement_id;

            confirmation = confirm(`Are you sure the information is correct?\n Pallet ID: ${NewPallet_Id}\n Starting Zone: ${NewStartZone} \n Ending Zone: ${NewEndZone} \n Barcode: ${NewBarcode}`)
            if (confirmation) {
                fetch(`/updateData/movement`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ NewPallet_Id, NewStartZone, NewEndZone, NewBarcode, movementId })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Updated")
                        else
                            alert("Entry not Updated.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.");
                location.reload();
            }


            break;
    }

}