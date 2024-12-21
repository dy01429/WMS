const clientB = document.getElementById('Clients');
const inventoryB = document.getElementById('Inventory');
const palletsB = document.getElementById('Pallets');
const boxesB = document.getElementById('Boxes');
const movementB = document.getElementById('Movement');


let tableDelete = 'none'
selectedEntry = null

const subTab = document.createElement(`a`);

document.addEventListener('DOMContentLoaded', function () {

    clientB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableDelete = "client"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select client by ID to delete</strong></label><br>
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

        tableDelete = "inventory"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select inventory by ID to delete</strong></label><br>
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

        tableDelete = "pallets"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select pallet by ID to delete</strong></label><br>
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

        tableDelete = "boxes"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select box by ID to delete</strong></label><br>
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

        tableDelete = "movement"
        subTab.innerHTML = `
        
        <form id="GetForm" method="GET" >
                <label> <strong>Select pallet movement by ID to delete</strong></label><br>
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

        switch (tableDelete) {
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


        fetch(`/viewData/${tableDelete}/${FieldType}/${SearchParam}`)
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
                console.error(`${tableDelete} has no ${FieldType} that equals ${SearchParam}:`, error);
                alert("No entry exists for that id");
                location.reload();
            });
    }
});
function displayResults(data) {
    results = document.getElementById('results');
    


    row = document.createElement(`div`);
    row.className="entry";
    switch (tableDelete) {
        case "client":
            row.innerHTML = `ID: ${data.Client_id}, Client Name: ${data.Client}, Client Address: ${data.clientAddress}, Client Contact: ${data.clientContact} <br>`;


            subTab.innerHTML = `
            <form id="DeleteForm">
                <label> <strong>Delete client details? </strong></label><br>
                    <fieldset>
                        <input type="radio" id="deleteConfirm" name="deleteDecide" value="Delete" /> <label for="deleteConfirm">Delete</label><br>
                        <input type="radio" id="deleteDeny" name="deleteDecide" value="Cancel"/>  <label for="deleteDeny">Cancel</label><br>
                    </fieldset>
                    <button type="submit" class="Submit">Submit</button>
            </form>
             `


            deleteform = document.getElementById('DeleteForm')

            

            if (deleteform) {
                console.log("Form found, setting up event listener");
                deleteform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    deleteEntry();
                });
            } else {
                console.error("Form element not found");
            }




            break;
        case "inventory":
            row.innerHTML = `ID: ${data.inventory_id}, Client ID: ${data.client_id}, Description: ${data.description}, Quantity: ${data.quantity}, Box ID: ${data.box_id} <br>`;



            subTab.innerHTML = `
            <form id="DeleteForm">
                <label> <strong>Delete invetory details? </strong></label><br>
                    <fieldset>
                        <input type="radio" id="deleteConfirm" name="deleteDecide" value="Delete" /> <label for="deleteConfirm">Delete</label><br>
                        <input type="radio" id="deleteDeny" name="deleteDecide" value="Cancel"/>  <label for="deleteDeny">Cancel</label><br>
                    </fieldset>
                    <button type="submit" class="Submit">Submit</button>
            </form>
             `


            deleteform = document.getElementById('DeleteForm')

            if (deleteform) {
                console.log("Form found, setting up event listener");
                deleteform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    deleteEntry();
                });
            } else {
                console.error("Form element not found");
            }


            break;
        case "boxes":
            row.innerHTML = `ID: ${data.box_id}, Box Label: ${data.box_label}, Dimensions: ${data.dimensions}, Weight: ${data.weight}, Pallet ID: ${data.pallet_id} <br>`;


            subTab.innerHTML = `
            <form id="DeleteForm">
                <label> <strong>Delete box details? </strong></label><br>
                    <fieldset>
                        <input type="radio" id="deleteConfirm" name="deleteDecide" value="Delete" /> <label for="deleteConfirm">Delete</label><br>
                        <input type="radio" id="deleteDeny" name="deleteDecide" value="Cancel"/>  <label for="deleteDeny">Cancel</label><br>
                    </fieldset>
                    <button type="submit" class="Submit">Submit</button>
            </form>
             `


            deleteform = document.getElementById('DeleteForm')

            if (deleteform) {
                console.log("Form found, setting up event listener");
                deleteform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    deleteEntry();
                });
            } else {
                console.error("Form element not found");
            }



            break;
        case "pallets":
            row.innerHTML = `ID: ${data.pallet_id}, Pallet Label: ${data.pallet_label}, Pallet Quality: ${data.pallet_quality}, Capacity: ${data.capacity} <br>`;

            subTab.innerHTML = `
            <form id="DeleteForm">
                <label> <strong>Delete pallet details? </strong></label><br>
                    <fieldset>
                        <input type="radio" id="deleteConfirm" name="deleteDecide" value="Delete" /> <label for="deleteConfirm">Delete</label><br>
                        <input type="radio" id="deleteDeny" name="deleteDecide" value="Cancel"/>  <label for="deleteDeny">Cancel</label><br>
                    </fieldset>
                    <button type="submit" class="Submit">Submit</button>
            </form>
             `


            deleteform = document.getElementById('DeleteForm')

            if (deleteform) {
                console.log("Form found, setting up event listener");
                deleteform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    deleteEntry();
                });
            } else {
                console.error("Form element not found");
            }


            break;
        case "movement":
            row.innerHTML = `ID: ${data.movement_id}, Pallet ID: ${data.pallet_id}, From Zone: ${data.from_zone}, To Zone: ${data.to_zone}, Barcode: ${data.barcode} <br>`;

            subTab.innerHTML = `
            <form id="DeleteForm">
                <label> <strong>Delete pallet movement details? </strong></label><br>
                    <fieldset>
                        <input type="radio" id="deleteConfirm" name="deleteDecide" value="Delete" /> <label for="deleteConfirm">Delete</label><br>
                        <input type="radio" id="deleteDeny" name="deleteDecide" value="Cancel"/>  <label for="deleteDeny">Cancel</label><br>
                    </fieldset>
                    <button type="submit" class="Submit">Submit</button>
            </form>
             `


            deleteform = document.getElementById('DeleteForm')

            if (deleteform) {
                console.log("Form found, setting up event listener");
                deleteform.addEventListener('submit', function (event) {
                    event.preventDefault(); // Prevent the default form submission
                    deleteEntry();
                });
            } else {
                console.error("Form element not found");
            }


            break;

    }
    deleteform = document.getElementById('DeleteForm')
    deleteform.classList.add("form")
    subTab.append(results);
    results.appendChild(row);
    // results.after(changeEntry);
}

function deleteEntry() {
    switch (tableDelete) {
        case "client":

            var ele = document.getElementsByName('deleteDecide');

            for (i = 0; i < ele.length; i++) {
                if (ele[i].id == "deleteConfirm" && ele[i].checked) {
                    confirmation = confirm("Are you Sure you want to Delete? \n This action cannot be undone.")
                    break;
                } else {
                    location.reload();
                }
            }
            clientId = selectedEntry.Client_id
            if (confirmation) {
                fetch(`/deleteData/${tableDelete}/${FieldType}/${clientId}`)
                    .then(response => response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Deleted")
                        else
                            alert("Entry not Deleted.\n Entry does not exist or has pre-existing dependencies.")

                        location.reload();
                    })
            }
            else
                location.reload();

            break;

        case "inventory":

            var ele = document.getElementsByName('deleteDecide');

            for (i = 0; i < ele.length; i++) {
                if (ele[i].id == "deleteConfirm" && ele[i].checked) {
                    confirmation = confirm("Are you Sure you want to Delete? \n This action cannot be undone.")
                    break;
                } else {
                    location.reload();
                }
            }
            inventoryID = selectedEntry.inventory_id
            if (confirmation) {
                fetch(`/deleteData/${tableDelete}/${FieldType}/${inventoryID}`)
                    .then(response => response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Deleted")
                        else
                            alert("Entry not Deleted.\n Entry does not exist or has pre-existing dependencies.")

                        location.reload();
                    })
            }
            else
                location.reload();


            break;

        case "pallets":

            var ele = document.getElementsByName('deleteDecide');

            for (i = 0; i < ele.length; i++) {
                if (ele[i].id == "deleteConfirm" && ele[i].checked) {
                    confirmation = confirm("Are you Sure you want to Delete? \n This action cannot be undone.")
                    break;
                } else {
                    location.reload();
                }
            }
            palletId = selectedEntry.pallet_id
            if (confirmation) {
                fetch(`/deleteData/${tableDelete}/${FieldType}/${palletId}`)
                    .then(response => response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Deleted")
                        else
                            alert("Entry not Deleted.\n Entry does not exist or has pre-existing dependencies.")

                        location.reload();
                    })
            }
            else
                location.reload();


            break;

        case "boxes":

            var ele = document.getElementsByName('deleteDecide');

            for (i = 0; i < ele.length; i++) {
                if (ele[i].id == "deleteConfirm" && ele[i].checked) {
                    confirmation = confirm("Are you Sure you want to Delete? \n This action cannot be undone.")
                    break;
                } else {
                    location.reload()
                }
            }
            boxId = selectedEntry.box_id
            if (confirmation) {
                fetch(`/deleteData/${tableDelete}/${FieldType}/${boxId}`)
                    .then(response => response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Deleted")
                        else
                            alert("Entry not Deleted.\n Entry does not exist or has pre-existing dependencies.")

                        location.reload();
                    })
            }
            else
                location.reload();


            break;

        case "movement":

            var ele = document.getElementsByName('deleteDecide');

            for (i = 0; i < ele.length; i++) {
                if (ele[i].id == "deleteConfirm" && ele[i].checked) {
                    confirmation = confirm("Are you Sure you want to Delete? \n This action cannot be undone.")
                    break;
                } else {
                    location.reload();
                }
            }
            movementID = selectedEntry.movement_id
            if (confirmation) {
                fetch(`/deleteData/${tableDelete}/${FieldType}/${movementID}`)
                    .then(response => response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully Deleted")
                        else
                            alert("Entry not Deleted.\n Entry does not exist or has pre-existing dependencies.")

                        location.reload();
                    })
            }
            else
                location.reload();


            break;
    }
}