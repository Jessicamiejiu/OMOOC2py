!DOCTYPE html>
<html>
  <head>

    <title>Diary Web Application</title>

  </head>
  
  <body>
  
    <form action="/diary" method="post">
    Input: <input type="text" name="newdiary" />
    <input value="Submit" type="submit" />
    </form><br>
    <textarea rows="20" cols="50">{{diarylog}}</textarea>
  
  </body>
</html>
