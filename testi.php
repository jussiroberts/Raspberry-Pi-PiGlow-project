
<meta http-equiv="refresh" content="1; url=?p=modes" />

<?php


$mode = $_POST['mode'];
$brightness = $_POST['brightness'];

$file = "/tmp/test.txt";
 
file_put_contents ($file, $mode);

echo nl2br("Success! \n");


if ($mode == 1) {
	exec ('sudo python /home/pi/piglow/cpuloadz.py > /dev/null 2>/dev/null &');
	echo "cpuloadz.py started! ";
} elseif ($mode == 2) {
	exec ('sudo python /home/pi/piglow/testi.py'); //exec networkload.py will be implemented here at a later stage.
	echo "testi.py started!";
} elseif ($mode == 3) {
	exec ("sudo python /home/pi/piglow/binaryclockzor.py $brightness > /dev/null 2>/dev/null &");
	echo "binaryclockzor.py started!";
} elseif ($mode == 4) {
	exec ('sudo python /home/pi/piglow/lightsoff.py > /dev/null 2>/dev/null &');
	echo "lightsoff.py started!";
} 

echo nl2br("\n Redirecting ....");
?>
