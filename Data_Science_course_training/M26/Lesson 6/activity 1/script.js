function appendToScreen(value) {
  var screen = document.getElementById('screen');
  screen.value += value;
  document.getElementById('expression').innerText = screen.value;
}

function clearScreen() {
  document.getElementById('screen').value = '';
  document.getElementById('expression').innerText = '';
}

function deleteLast() {
  var screen = document.getElementById('screen');
  screen.value = screen.value.slice(0, -1);
  document.getElementById('expression').innerText = screen.value;
}

function calculate() {
  var screen = document.getElementById('screen');
  try {
    var result = eval(screen.value);
    document.getElementById('expression').innerText = screen.value + ' =';
    screen.value = result;
  } catch (e) {
    screen.value = 'Error';
    document.getElementById('expression').innerText = '';
  }
}
