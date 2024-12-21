result= document.getElementById("barcodeScan")
//scanB=document.getElementById("startScanButton")
dylanB=document.getElementById("startDylan")

document.addEventListener('DOMContentLoaded', function () {
    /*scanB.addEventListener('click', (e) => {
        e.preventDefault();

        fetch(`/viewData/${tableSearch}/${FieldType}/${SearchParam}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            results.innerHTML = data.barcode;

            alert("Barcode Detected!")
        })

        .catch(error => {
            console.error('Error Retreiving Entry:', error);
            alert("Entry not found with specific input.")
            location.reload()
        });


    })

   */
   dylanB.addEventListener('click', (e) => {
        fetch('/startDylan')
    })
})