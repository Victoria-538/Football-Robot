<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Calling a Python Script</title>
</head>
<body>
  <center>
    <h1>Calling a Python Script</h1>
    <form method="get" action="buttontest.php">
      <input type="submit" style="font-size: 14 pt" value="OFF" name="off">
      <input type="submit" style="font-size: 14 pt" value="ON" name="on">
    </form>
  </center>
  <?php
    if(isset($_GET['off']))
    {
      shell_exec("./logparameters.py off");
    }
    else if(isset($_GET['on']))
    {
     shell_exec("./logparameters.py on");
    }
  ?>
</body>
</html>


