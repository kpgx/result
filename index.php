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
<p>Source Code for this page :<a href="https://github.com/kpgx/result" target="_blank">github.com/kpgx/result</a></p>
<?php

$con=mysqli_connect("localhost","root","","result_new");

// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }  
if(isset($_POST['index']) && !empty($_POST['index'])) {	
	$index = htmlspecialchars(stripslashes(trim($_POST["index"])));  	
   echo "<b>".$index."</b><hr>";	
	$result = mysqli_query($con,"SELECT * FROM `old` WHERE `index`=$index");	
	if (@mysqli_num_rows($result)==0){
		echo "Sorry the Index you entered is not in the DB<br>";	
	}	
	else{
		$row = mysqli_fetch_array($result,MYSQLI_ASSOC);		
  		$GPA=$row['GPA'];
  		$GPAClass=$row['GPAClass'];
		$rank=$row['rank'];
		$rankClass=$row['rankClass'];
		$GPV=$row['GPV'];
		$GPVClass=$row['GPVClass'];
		$tCredit=$row['credit'];
		foreach($row as $x=>$x_value){
			if ($x=='index' ||$x=='GPA' ||$x=='rank' ||$x=='GPV' ||$x=='credit'||$x=='GPAClass'||$x=='rankClass'||$x=='GPVClass'){
				continue;
				}
  			echo "Code=" . $x . ", Grade=" . $x_value."<br>";  			
  		}
  		echo "<hr><b>Class GPA = ".$GPAClass."<br>RANK = ".$rankClass."<br>GPV = ".$GPVClass."<br></b>";
  		echo "gradeCredits={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':2.25,'rA':2.25,'rA-':2.25,'rB+':2.25,'rB':2.25,'rB-':2.25,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}<hr>";

  		//echo "<b>GPA = ".$GPA."<br>RANK = ".$rank."<br>GPV = ".$GPV."<br></b>";
  		//echo "gradeCredits={'A+':4,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':4.00,'rA':4.00,'rA-':3.75,'rB+':3.25,'rB':3.00,'rB-':2.75,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}</hr>";

  		echo "subCredits={'ENH1010':0, 'SCS2001':4, 'SCS2010':3, 'ENH1020':0, 'SCS1005':3, 'SCS1004':3, 'SCS1007':3, 'SCS1006':4, 'SCS1001':3, 'SCS2005':3, 'SCS1003':3, 'SCS1002':4, 'SCS2003':3, 'SCS1009':3,'SCS1008':4,'SCS2011':1}<br>";
		echo "<hr>Drop me an email @ kpgxyz@gmail.com if there is a issue with you results displayed here.";
		//echo "gradeCredits={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,<br>'rA+':2.25,'rA':2.25,'rA-':2.25,'rB+':2.25,'rB':2.25,'rB-':2.25,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}</hr>";
  	}
	mysqli_close($con);
}

?>

<div style="text-align: center"><em><p>I hold no responsibility for the accuracy of the data used in this page. Use this website at your own risk -aela</p></em></div>


</body>

</html>