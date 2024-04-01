const addPetForm = document.getElementById("add-pet");
const tableBody = document.getElementById("table-body");

addPetForm.addEventListener("submit", addPet);

async function addPet(e) {
  e.preventDefault();
  const petFormData = new FormData(addPetForm);

  const response = await fetch("http://localhost:5500/pets/create", {
    method: "POST",
    body: petFormData,
  });
  const pet = await response.json();
  addTableRow(pet);
  addPetForm.reset();
}

function addTableRow(pet) {
  const newRow = document.createElement("tr");
  newRow.innerHTML = `
  <tr>
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
    </td>
  </tr>`;
  tableBody.appendChild(newRow);
}
