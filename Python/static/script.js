function validateForm() {
    let name = document.getElementById("name").value;
    let address = document.getElementById("address").value;

    if (name.trim() === "" || address.trim() === "") {
        alert("Both fields are required!");
        return false;
    }
    return true;
}

function validateSearch() {
    let name = document.getElementById("searchName").value;

    if (name.trim() === "") {
        alert("Please enter a name to search!");
        return false;
    }
    return true;
}
