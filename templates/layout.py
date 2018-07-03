{%extends 'layout.html'%}
{%block content%}
<body>
  <div class="container">
  <p>Welcome{{name}} to the {{course}} we shall be contacting on your email {{email}}</p>
  <p>Go back to multiply page <a href="{{url_for("index")}}">Click here</a></p>
</div>
</body>

{%endblock%}
