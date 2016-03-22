(function() {
  $(document).ready(function(){
    $('#js-search-button').click(function(e) {
      e.preventDefault()
      var query = $('#js-query-input').val()
      $.ajax('/', {
        dataType: 'json',
        method: 'POST',
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({
          "query": query
        }),
        success: function(data, status, jqXHR) {
          displayResults(data)
        },
        error: function(jqXHR, status, error) {
          displayError()
        }
      })
    })
  })

  function displayResults(results) {
    $('.results').empty()
    results['data'].forEach(function(link, i) {
      if (i == 0) {
        $('.results').append('<div class="result"><p>' + link[0] + '</p></div>')
      } else {
        $('.results').append('<div class="result"><p>' + link[0] + ' (' + link[2] + ')' + '</p><p><img src="' + link[1] + '"></img></div>')
      }
      if (i < results['data'].length - 1) {
        $('.results').append('<div class=arrow></div>')
      }
    })
  }

  function displayError() {
    $('.results').empty()
    $('.results').append('<div class="result"><p>No Results Found</p></div>')
  }

}())
