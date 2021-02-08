template = """
<html>
  <ul>
  {% for item in todos %}
    <li> {{ item }} </li>
  {% endfor %}
  </ul>
</html>
"""