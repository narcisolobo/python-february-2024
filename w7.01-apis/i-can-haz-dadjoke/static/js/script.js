const jokeContainer = document.querySelector("#joke-container");
console.log(jokeContainer);

async function getJoke() {
  const response = await fetch("https://icanhazdadjoke.com/", {
    headers: {
      Accept: "application/json",
    },
  });
  const data = await response.json();
  console.log(data);
  jokeContainer.textContent = data.joke;
}

getJoke();
