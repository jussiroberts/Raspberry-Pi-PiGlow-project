
<div class="subcontent">

Select the information you would like the PiGlow to display:</p>
<?php
   $mode = $_POST['mode'];
   $brightness = $_POST['brightness'];
?>

<div id="myRadioGroup">
<form action="?p=testi" method="POST">
CPU Load<input type="radio" name="mode" value="1">
Network Load<input type="radio" name="mode" value="2"><br>
Binary Clock<input type="radio" name="mode" value="3">
Lights off<input type="radio" name="mode" value="4"><br>

</br>
<div id="Mode3" class="desc" style="display: none;">
Select LED Brightness: (value range 1-255) </br>
<input type="number" name="brightness" min="0" max="255">
</div>

</br>

</div>

</div>
<input type="submit" value="Apply" align="right">


</form>

<?php echo"$mode $brightness";?>

<div class="copyr">
<hr>
An application developed by Jussi Roberts 
</div>