const clientB = document.getElementById('Clients');
const inventoryB = document.getElementById('Inventory');
const palletsB = document.getElementById('Pallets');
const boxesB = document.getElementById('Boxes');
const movementB = document.getElementById('Movement');

const subTab = document.createElement(`a`);

tableEnter = "none"


document.addEventListener('DOMContentLoaded', function () {


    clientB.addEventListener('click', (e) => {
        e.preventDefault();
        const display = document.getElementById('interface');

        tableEnter = "client"
        subTab.innerHTML = `
        
        <form id="NewForm" method="POST" >
                <label> <strong>Enter new client details</strong></label><br>
                
                    <input type="text" placeholder="Client Name" name="Client Name" id="Client Name" required> <br>
                    <input type="text" placeholder="Client Address" name="Client Address" id="Client Address" required> <br>
                    <input type="text" placeholder="Client Contact" name="Client Contact" id="Client Contact" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>

        `

        display.appendChild(subTab);

        const form = document.getElementById('NewForm');

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

        tableEnter = "inventory"
        subTab.innerHTML = `
        
        <form id="NewForm" method="POST" >
                <label> <strong>Enter new inventory details</strong></label><br>
                
                    <input type="text" placeholder="Client ID (Foreign Key)" name="Client Name" id="Client Name" required> <br>
                    <input type="text" placeholder="Description" name="Description" id="Description" required> <br>
                    <input type="text" placeholder="Quantity" name="Quantity" id="Quantity" required> <br>
                    <input type="text" placeholder="Box ID (Foreign Key)" name="Box ID" id="Box ID" required> <br>
                    <button type="submit" class="Submit">Submit</button>
        </form>`

        display.appendChild(subTab);

        const form = document.getElementById('NewForm');

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

        tableEnter = "boxes"
        subTab.innerHTML = `
        
        <form id="NewForm" method="POST" >
                <label> <strong>Enter new box details</strong></label><br>
                
                    <input type="text" placeholder="Box label" name="box label" id="box label" required> <br>
                    <input type="text" placeholder="Dimensions (LxHxW)" name="dimensions" id="dimensions" required> <br>
                    <input type="text" placeholder="Weight" name= Weight" id="Weight" required> <br>
                    <input type="text" placeholder="Pallet Id (Foreign Key)" name="Pallet Id" id="Pallet Id" required> <br>
                    <button type="submit" class="Submit">Submit</button>
        </form>`

        display.appendChild(subTab);

        const form = document.getElementById('NewForm');

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

        tableEnter = "pallets"
        subTab.innerHTML = `
        <form id="NewForm" method="POST" >
                <label> <strong>Enter new pallet details</strong></label><br>
                
                    <input type="text" placeholder="Pallet Label" name="Pallet Label" id="Pallet Label" required> <br>
                    <input type="text" placeholder="Pallet Quality" name="Pallet Quality" id="Pallet Quality" required> <br>
                    <input type="text" placeholder="Pallet Capacity" name="Pallet Capacity" id="Pallet Capacity" required> <br>
                <button type="submit" class="Submit">Submit</button>
        </form>
        
        `

        display.appendChild(subTab);

        const form = document.getElementById('NewForm');

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

        tableEnter = "movement"
        subTab.innerHTML = `
        <form id="NewForm" method="POST" >
                <label> <strong>Enter new pallet movement details</strong></label><br>
                
                    <input type="text" placeholder="Pallet ID (Foreign Key)" name="Pallet ID" id="Pallet ID" required> <br>
                    <input type="text" placeholder="Starting Zone" name="Starting Zone" id="Starting Zone" required> <br>
                    <input type="text" placeholder="Ending Zone" name=" Ending Zone" id="Ending Zone" required> <br>
                    <input type="text" placeholder="Barcode" name="Barcode" id="Barcode" required> <br>
                    <button type="submit" class="Submit">Submit</button>
        </form
        
        `

        display.appendChild(subTab);

        const form = document.getElementById('NewForm');
        form.classList.add("form")
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

    




})
function submitForm() {
    console.log('In submitForm...');

    switch (tableEnter) {
        case "client":

            const clientName = document.getElementById("Client Name").value;
            const clientAddress = document.getElementById("Client Address").value;
            const clientContact = document.getElementById("Client Contact").value;

            confirmation = confirm(`Are you sure the information is correct?\n Client Name: ${clientName}\n Client Address: ${clientAddress}\n Client Contact: ${clientContact} `)
            if (confirmation) {
                fetch(`/enterData/client`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ clientName, clientAddress, clientContact })
                })
                    .then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully inserted")
                        else
                            alert("Entry not inserted.")

                        location.reload();
                    }

                    )
            } else {
                alert("Throwing away input.")

                location.reload();
            }
            break;
        case "inventory":

            const clientId = document.getElementById("Client Name").value;
            const description = document.getElementById("Description").value;
            const quantity = document.getElementById("Quantity").value;
            const boxId = document.getElementById("Box ID").value;
            confirmation = confirm(`Are you sure the information is correct?\n Client Id: ${clientId} \n Description: ${description}\n Quantity: ${quantity} \n Box Id: ${boxId} `)
            if (confirmation) {
                fetch(`/enterData/inventory`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ clientId, description, quantity, boxId })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully inserted")
                        else
                            alert("Entry not inserted.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.")
                location.reload();
            }
            break;
        case "boxes":

            const boxLabel = document.getElementById('box label').value;
            const dimensions = document.getElementById('dimensions').value;
            const weight = document.getElementById('Weight').value;
            const palletId = document.getElementById('Pallet Id').value;

            confirmation = confirm(`Are you sure the information is correct?\n Box Label: ${boxLabel} \n Dimensions: ${dimensions} \n Weight: ${weight} \n Pallet ID: ${palletId} `)
            if (confirmation) {

                fetch(`/enterData/boxes`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ boxLabel, dimensions, weight, palletId })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully inserted")
                        else
                            alert("Entry not inserted.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.");
                location.reload();
            }


            break;
        case "pallets":

            const palletLabel = document.getElementById("Pallet Label").value;
            const palletQuality = document.getElementById("Pallet Quality").value;
            const palletCapacity = document.getElementById("Pallet Capacity").value;

            confirmation = confirm(`Are you sure the information is correct?\n Pallet Label:${palletLabel}\n Pallet Quality: ${palletQuality}\n Pallet Capacity: ${palletCapacity} `)
            if (confirmation) {

                fetch(`/enterData/pallets`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ palletLabel, palletQuality, palletCapacity })
                }).then(response => response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully inserted")
                        else
                            alert("Entry not inserted.")

                        location.reload();
                    })

            } else {
                alert("Throwing away input.")

                location.reload();
            }
            break;
        case "movement":

            const pallet_Id = document.getElementById("Pallet ID").value;
            const startZone = document.getElementById("Starting Zone").value;
            const endZone = document.getElementById("Ending Zone").value;
            const barcode = document.getElementById("Barcode").value;
            confirmation = confirm(`Are you sure the information is correct?\n Pallet ID: ${pallet_Id}\n Starting Zone: ${startZone} \n Ending Zone: ${endZone} \n Barcode: ${barcode}`)
            if (confirmation) {
                fetch(`/enterData/movement`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ pallet_Id, startZone, endZone, barcode })
                }).then(Response => Response.json())
                    .then(error => {
                        console.log(error)
                        if (error.error == false)
                            alert("Successfully inserted")
                        else
                            alert("Entry not inserted.")

                        location.reload();
                    })
            } else {
                alert("Throwing away input.");
                location.reload();
            }
            break;

    }

    // .catch(error => {
    //     console.error('Error occurred during account creation:', error);
    // });
};