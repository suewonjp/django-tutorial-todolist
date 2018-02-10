$(document).ready(function() {

  // Prevent form submission with accidental Enter key hit
  function checkEnter(e) {
    e = e || event;
    var txtArea = /textarea/i.test((e.target || e.srcElement).tagName);
    return txtArea || (e.keyCode || e.which || e.charCode || 0) !== 13;
  }
  $(document).find('form').on('keypress', checkEnter)

  $('#new-category-name').on('change', function() {
    const submit = $('#add-category-form input[type="submit"]').attr('disabled', true)
    const name = $(this).val()
    if (!name)
      return
    if ($('.existing-categories').find(`.category-${name}`).length) {
      // Category name duplicated
      $('.warning-box').show()
    }
    else {
      // Ready to submit a new category
      $('.warning-box').hide()
      submit.attr('disabled', false)
    }
  })

})

