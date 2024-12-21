const clientB = document.getElementById('Clients');
const inventoryB = document.getElementById('Inventory');
const palletsB = document.getElementById('Pallets');
const boxesB = document.getElementById('Boxes');
const movementB = document.getElementById('Movement');
const barcodeB=document.getElementById('Barcodes');
const stackingB= document.getElementById('Stacking');

let tableSearch = 'none'

const subTab = document.createElement(`a`);

even=false;


document.addEventListener('DOMContentLoaded', function () {


    clientB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "client"

        const display = document.getElementById('searchInterface');

        results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="client_id">Client ID</option>
                    <option value="client_name">Client Name</option>
                    <option value="client_address">Client Address</option>
                    <option value="contact_details">Client Contact</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )

    inventoryB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "inventory"

        const display = document.getElementById('searchInterface');
        results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="inventory_id">Inventory ID</option>
                    <option value="Description">Description</option>
                    <option value="quantity">Quantity</option>
                    <option value="box_id">Box ID</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )

    palletsB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "pallets"

        const display = document.getElementById('searchInterface');

         results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="pallet_id">Pallet ID</option>
                    <option value="pallet_label">Pallet Label</option>
                    <option value="pallet_quality">Quality</option>
                    <option value="Capacity">Capacity</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )

    boxesB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "boxes"

        const display = document.getElementById('searchInterface');

        results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="box_id">Box ID</option>
                    <option value="box_label">Box Label</option>
                    <option value="Length">Length</option>
                    <option value="Width">Width</option>
                    <option value="Height">Height</option>
                    <option value="Weight">Weight</option>
                    <option value="pallet_id">Pallet ID</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )

    movementB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "movement"

        const display = document.getElementById('searchInterface');

        results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="movement_id">Movement ID</option>
                    <option value="client_name">Client Name</option>
                    <option value="from_zone">From Zone</option>
                    <option value="to_zone">To Zone</option>
                    <option value="barcode">Barcode</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');
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

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )

    barcodeB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "barcode"

        const display = document.getElementById('searchInterface');

        results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="scan_id">Scan ID</option>
                    <option value="barcode_data">Barcode Data</option>
                    <option value="scan_time">Scan Time</option>
                    <option value="pallet_id> Pallet ID</option>
                    <option value="zone_id">Zone ID</option>
                    <option value="zone">Zone</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )

    stackingB.addEventListener('click', (e) => {
        e.preventDefault();

        tableSearch = "stacking"

        const display = document.getElementById('searchInterface');

        results= document.getElementById('results');

        if(results)
            results.innerHTML='';

        subTab.innerHTML = `
        <button type="button" id= 'View All'> View All</button>
        <form id="SearchForm" method="GET" >
                <label for="FieldType"> <strong>Search by Field</strong></label>
                <select id="FieldType" name="FieldType">
                    <option value="stack_id">Stack ID</option>
                    <option value="pallet_id">Pallet ID</option>
                    <option value="box_id">Box ID</option>
                    <option value="stack_level">Stack Level</option>
                </select>

                <input type="text" placeholder="Search" name="SearchParam" id="SearchParam" required>
                <button type="submit" class="Search">Search</button>
        </form>
        `

        display.appendChild(subTab);

        const form = document.getElementById('SearchForm');

        if (form) {
            console.log("Form found, setting up event listener");
            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the default form submission
                submitForm();
            });
        } else {
            console.error("Form element not found");
        }

        const getAll = document.getElementById('View All')

        if (getAll) {
            getAll.addEventListener("click", function (event) {
                event.preventDefault
                getAllData()
            })
        }


    }
    )
}
)

function submitForm() {
    console.log('In submitForm...');

    const FieldType = document.getElementById('FieldType').value
    const SearchParam = document.getElementById('SearchParam').value

    console.log('Field Type:', FieldType);
    console.log('Search Parameter:', SearchParam);


    fetch(`/viewData/${tableSearch}/${FieldType}/${SearchParam}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            results = document.getElementById('results');
            results.innerHTML = '';

            data.data.forEach(clientInfo => {
                console.log(clientInfo)
                displayResults(clientInfo)
            })
        })

        .catch(error => {
            console.error('Error Retreiving Entry:', error);
            alert("Entry not found with specific input.")
            location.reload()
        });
};

function getAllData() {
    even=false;
    fetch(`/viewData/viewAll/${tableSearch}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            results = document.getElementById('results');
            results.innerHTML = '';

            data.data.forEach(clientInfo => {
                console.log(clientInfo)
                displayResults(clientInfo)
            })
        })

        .catch(error => {
            console.error('Error occurred during account creation:', error);
        });
};

function displayResults(data) {
    results = document.getElementById('results');
    


    row = document.createElement(`div`);

    row.className= "entry";

    if(even){
        row.style.backgroundColor= "white";
        even=false;
    }else{
        even=true;
    }

   // row.setAttribute("style",'margin-bottom: 5px')

    switch (tableSearch) {
        case "client":
            row.innerHTML = `ID: ${data.Client_id}, Client Name: ${data.Client}, Client Address: ${data.clientAddress}, Client Contact: ${data.clientContact} <br>`;
            break;
        case "inventory":
            row.innerHTML = `ID: ${data.inventory_id}, Client ID: ${data.client_id}, Description: ${data.description}, Quantity: ${data.quantity}, Box ID: ${data.box_id} <br>`;
            break;
        case "boxes":
            row.innerHTML = `ID: ${data.box_id}, Box Label: ${data.box_label}, Length: ${data.length}, Width: ${data.width}, Height: ${data.height} Weight: ${data.weight}, Pallet ID: ${data.pallet_id} <br>`;
            break;
        case "pallets":
            row.innerHTML = `ID: ${data.pallet_id}, Pallet Label: ${data.pallet_label}, Pallet Quality: ${data.pallet_quality}, Capacity: ${data.capacity} <br>`;
            break;
        case "movement":
            row.innerHTML = `ID: ${data.movement_id}, Pallet ID: ${data.pallet_id}, From Zone: ${data.from_zone}, To Zone: ${data.to_zone}, Barcode: ${data.barcode} <br>`;
            break;
        case "barcode":
            row.innerHTML = `ID: ${data.scan_id}, Barcode Data: ${data.barcode_data}, Scan Time: ${data.scan_time}, Pallet ID: ${data.pallet_id}, Zone ID: ${data.zone_id}, Zone: ${data.zone} <br>`;
            break;
        case "stacking":
            row.innerHTML = `ID: ${data.stack_id}, Pallet ID: ${data.pallet_id}, Box ID: ${data.box_id}, Stack Level: ${data.stack_level} <br>`

    }

    results.appendChild(row);


};


