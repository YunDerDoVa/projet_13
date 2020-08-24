function showScript(id) {
  var text = document.getElementById(id);
  if (text.dataset['display'] == 'none') {
    text.style.height = '100%';
    text.dataset['display'] = 'block';
  }
  else {
    text.style.height = '0';
    text.dataset['display'] = 'none';
  }
}
