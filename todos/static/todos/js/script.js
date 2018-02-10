$(document).ready(function() {

  // Prevent form submission with accidental Enter key hit
  function checkEnter(e) {
    e = e || event;
    var txtArea = /textarea/i.test((e.target || e.srcElement).tagName);
    return txtArea || (e.keyCode || e.which || e.charCode || 0) !== 13;
  }
  $(document).find('form').on('keypress', checkEnter)

})

