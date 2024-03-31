Toastify({
  text: "Toast to you!",
  duration: 3000,
  close: true,
  gravity: "top",
  position: "left",
  stopOnFocus: true,
  className: "alert alert-error",
}).showToast();

function createToast(text) {
  Toastify({
    text,
    duration: 3000,
    close: true,
    gravity: "top",
    position: "left",
    stopOnFocus: true,
    className: "alert alert-error",
  });
}
