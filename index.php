<!DOCTYPE html>
<html>
<head>
<title>UCSC semester exam results</title>
</head>
<body>
<div style="text-align: center"><form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
index: <input type="text" name="index"><br>
<input type="submit">
</form></div>
<?php

$host=""
$user=""
$password=""
$db=""

$con=mysqli_connect($host,$user,$password,$db);

if (mysqli_connect_errno()){
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }  
if(isset($_POST['index']) && !empty($_POST['index'])){	
	$index = htmlspecialchars(stripslashes(trim($_POST["index"])));  	
   echo "<b>".$index."</b><hr>";	
	$result = mysqli_query($con,"SELECT * FROM `current` WHERE `index`=$index");	
	if (@mysqli_num_rows($result)==0){
		echo "Sorry the Index you entered is not in the DB<br>";	
		}	
	else{
		$row = mysqli_fetch_array($result,MYSQLI_ASSOC);		
  		$GPA=$row['GPA'];
		$rank=$row['rank'];
		$GPV=$row['GPV'];
		$tCredit=$row['credit'];
		foreach($row as $x=>$x_value){
			if ($x=='index' ||$x=='GPA' ||$x=='rank' ||$x=='GPV' ||$x=='credit'){
				continue;
				}
  			echo "Code=" . $x . ", Grade=" . $x_value."<br>";  			
  			}
  		echo "<hr><b>RANK = ".$rank."<br>GPA = ".$GPA."<br>GPV = ".$GPV."<br>Total credits = ".$tCredit."<br><hr></b>";
  		echo "<b>subCredits={'ENH1010':0, 'SCS2001':4, 'SCS2010':3, 'ENH1020':0, 'SCS1005':3, 'SCS1004':3, 'SCS1007':3, 'SCS1006':4, 'SCS1001':3, 'SCS2005':3, 'SCS1003':3, 'SCS1002':4, 'SCS2003':3, 'SCS1009':3,'SCS1008':4,'SCS2011':1}
<br>gradeCredits={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,<br>'rA+':2.25,'rA':2.25,'rA-':2.25,'rB+':2.25,'rB':2.25,'rB-':2.25,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}</b>";
  		}
	mysqli_close($con);
	}

?>

<div style="position:absolute;width:700px;bottom:0px;right:25%;left:50%;margin-left:-350px;"><em><p>I hold no responsibility for the accuracy of the data used in this page. Use this website at your own risk -aela</p></em></div>

</body>

</html>