// Grab the form and the table body
const petForm = document.getElementById("add-pet");
const tableBody = document.getElementById("table-body");

// add a submit event listener on the form
petForm.addEventListener("submit", async function (event) {
  // prevent submission of the form
  event.preventDefault();
  console.log("form has been intercepted");

  // create a FormData object out of the user input
  const petFormData = new FormData(petForm);

  // make a fetch post request
  const response = await fetch("http://localhost:5500/pets/create", {
    method: "POST",
    body: petFormData,
  });

  // turn the JSON body of the response into JavaScript object
  const pet = await response.json();

  // call the createTableRow function to create a table row
  const tableRow = createTableRow(pet);
  // append the row to the tableBody
  tableBody.appendChild(tableRow);
  // blank out the form
  petForm.reset();
});

function createTableRow(pet) {
  // create a table row HTML element object
  const tableRow = document.createElement("tr");
  // create a template literal with dynamic placeholders
  const tableData = `
  <td class="align-middle">
    <a href="/pets/${pet.id}">${pet.name}</a>
  </td>
  <td class="align-middle">${pet.type}</td>
  <td class="align-middle">
    ${pet.is_derpy ? "Yes" : "No"}
  </td>
  <td class="d-flex gap-2">
    <a
      href="/pets/${pet.id}/edit"
      class="btn btn-sm btn-primary"
    >
      Edit
    </a>
    <form action="/pets/${pet.id}/delete" method="post">
      <button type="submit" class="btn btn-sm btn-danger">
        Delete
      </button>
    </form>
  </td>`;
  // set the tableRow innerHTML to the template literal
  tableRow.innerHTML = tableData;
  // return the tableRow
  return tableRow;
}
