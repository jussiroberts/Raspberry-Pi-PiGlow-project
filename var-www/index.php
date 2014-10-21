<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"/>
<title> PiGlow Controller </title>

<script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
<script>
$(document).ready(function() {
    $("input[name$='mode']").click(function() {
        var test = $(this).val();

        $("div.desc").hide();
        $("#Mode" + test).show();
    });
});
</script>

<!--Ladataan css tiedostot-->
<link href="styles/normal.css" rel="stylesheet" type="text/css" />
<link href="styles/divs.css" rel="stylesheet" type="text/css" />
</script>

</head>

<body>


<table class="main_table" align="center" border="0" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td valign="top">

<div class="topphoto">
<img src="images/ylakuva.png">
</div>

<div class="logo">
<img src="images/logo.png" title="PiGlow Controller" alt="PiGlow Controller">
</div>

<div class="status"> <!-- The placeholder for the element that shows the current mode of the LED -->
<b>
<?php

 $file = "/tmp/test.txt";
 
 $content = file_get_contents($file);
 

if ($content == 1) {
	echo "Current mode: CPU Load";
} elseif ($content == 2) {
	echo "Current mode: Network Load";
} elseif ($content == 3) {
	echo "Current mode: Binary Clock";
} elseif ($content == 4) {
	echo "Current mode: Lights off";
} 
?>
</b>
</div>


<!-- Linkit -->


<div class="modes_link">
<a href="?p=modes"
onmouseover="document.sub_but.src='images/modes_pressed.png'"
onmouseout="document.sub_but.src='images/modes.png'">
<img border="0" src="images/modes.png" title="Modes" alt="Modes" name="sub_but" />
</a>
</div>

<div class="help_link" align="left">

<a href="?p=help"
onmouseover="document.sub_but1.src='images/help_pressed.png'"
onmouseout="document.sub_but1.src='images/help.png'">
<img border="0" src="images/help.png" title="Help" alt="Help" name="sub_but1" />
</a>
</div>


<div class="content">
<div class="text">



<!-- PHP alkaa -->
<?php

$sivu=($_GET['p']);
switch($sivu)
{

case "modes":
require 'modes.php';
break;

case "help":
require 'help.php';
break;

case "testi":
require 'testi.php';
break;

case "process":
require 'process.php';
break;

default:
require 'modes.php';
break;
}

?>
<!-- PHP loppuu-->

</div>

</div>

</td>
</tr>
</table>



</body>
</html>
