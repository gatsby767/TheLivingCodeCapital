// certification.js - small enhancements: debounce search and auto-submit on filter
(function(){
  var q = document.getElementById('q');
  var cert = document.getElementById('cert');
  var form = document.getElementById('searchForm');
  if (!form) return;

  // debounce helper
  function debounce(fn, wait){
    var t; return function(){
      var args = arguments; clearTimeout(t);
      t = setTimeout(function(){ fn.apply(null, args); }, wait);
    };
  }

  if (q){
    q.addEventListener('input', debounce(function(){
      // only submit if more than 2 chars or empty
      var v = q.value.trim();
      if (v.length === 0 || v.length > 2) form.submit();
    }, 450));
  }

  if (cert){
    cert.addEventListener('change', function(){ form.submit(); });
  }
})();
