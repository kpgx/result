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

$subjects=array(
"SCS1002"=>"Introduction to Programming",
"ENH1010"=>"Language Skills",
"SCS1003"=>"Computer Systems",
"SCS1004"=>"PC Application Laboratory",
"SCS1005"=>"Systems Analysis and Design",
"SCS1009"=>"Introduction to Probability and Statistics",
"SCS1001"=>"Mathematics for Computing",
"ENH1020"=>"Life Skills",
"SCS1006"=>"Introduction to Data structures and Algorithms",
"SCS1007"=>"Software Engineering",
"SCS1008"=>"Database Management Systems",
"SCS2001"=>"Operating Systems",
"SCS2002"=>"Rapid Application Development",
"SCS2003"=>"Object Oriented Systems Development",
"SCS2005"=>"Internet Programming",
"SCS2006"=>"Analogue and Digital Electronics",
"SCS2004"=>"Introduction to Programming Languages",
"SCS2007"=>"System Programming",
"SCS2008"=>"Numerical Computing",
"SCS2009"=>"Advanced Data Structures and Algorithms",
"SCS2010"=>"Statistical Inference for Computing",
"SCS2011"=>"Analogue and Digital Electronics II",
"ICT1001"=>"Introduction to Software Development",
"ICT1002"=>"Systems Analysis and Design",
"ICT1003"=>"Business Information Systems",
"ICT1004"=>"PC Application Laboratory",
"ICT1005"=>"Fundamentals of Management",
"ICT1006"=>"Mathematics I",
"ICT1007"=>"Communication Skills",
"ICT1008"=>"Fundamentals of Economics",
"ICT1009"=>"Fundamentals of Sociology",
"ICT1010"=> "Communication Technologies",
"ICT1011"=>"Database Management Systems",
"ICT1012"=>"Computer Systems",
"ICT1013"=>"Guest Lecture Series",
"ICT1014"=>"Mathematics II",
"ICT1015"=>"Fundamentals of Accountancy",
"ICT1016"=>"Fundamentals of Psychology",
"ICT2001"=>"Software Engineering",
"ICT2002"=>"Group Project",
"ICT2003"=>"Internet Application Development",
"ICT2004"=>"Multimedia Technologies",
"ICT2005"=>"Business Statistics & Operational Research",
"ICT2006"=>"Marketing",
"ICT2007"=>"Industrial Visits",
"ICT2008"=>"Business Process Re-Engineering",
"ICT2009"=>"IT Project Management",
"ICT2010"=>"Information Systems Security and Audit",
"ICT2011"=>"Digital Fine Arts",
"ICT2012"=>"Software Development Project",
"ICT2013"=>"e-Business Technologies and Applications",
"ICT2014"=>"Special Topics in Computer Science"
);
$con=mysqli_connect("host","user","pass","db");


// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }  
if(isset($_POST['index']) && !empty($_POST['index'])) {	
	$index = htmlspecialchars(stripslashes(trim($_POST["index"])));  	
   echo "<b>".$index."</b><hr>";	
	$result = mysqli_query($con,"SELECT * FROM `ict` WHERE `index`=$index");	
	if (@mysqli_num_rows($result)==0){
		$result = mysqli_query($con,"SELECT * FROM `cs` WHERE `index`=$index");	
		}
	if (@mysqli_num_rows($result)==0){
		echo "Sorry the Index you entered is not in the DB<br>";	
		}	
	else{
		$row = mysqli_fetch_array($result,MYSQLI_ASSOC);
		ksort($row);		
  		$GPA=$row['GPA'];
  		$GPAClass=$row['GPAClass'];
		$rank=$row['rank'];
		$rankClass=$row['rankClass'];
		$GPV=$row['GPV'];
		$GPVClass=$row['GPVClass'];
		$tCredit=$row['credit'];
		foreach($row as $x=>$x_value){
			if ($x=='index' ||$x=='GPA' ||$x=='rank' ||$x=='GPV' ||$x=='credit'||$x=='GPAClass'||$x=='rankClass'||$x=='GPVClass'||$x_value==''){
				continue;
				}
  			echo "[".$x."] ".$subjects[$x] . " => <b>" . $x_value."</b><br>";  			
  		}
  		echo "<hr><b>Class GPA = ".$GPAClass."<br>RANK = ".$rankClass."<br>GPV = ".$GPVClass."<br>Total credits = ".$tCredit."<br></b>";
  		echo "gradeCredits={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':2,'rA':2,'rA-':2,'rB+':2,'rB':2,'rB-':2,'rC+':2,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}<hr>";

  		//echo "<b>GPA = ".$GPA."<br>RANK = ".$rank."<br>GPV = ".$GPV."<br></b>";
  		//echo "gradeCredits={'A+':4,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':4.00,'rA':4.00,'rA-':3.75,'rB+':3.25,'rB':3.00,'rB-':2.75,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}</hr>";
		echo "subCredits={'ENH1010':0, 'SCS2001':4, 'SCS2010':3, 'ENH1020':0, 'SCS1005':3, 'SCS1004':3, 'SCS1007':3, 'SCS1006':4, 'SCS1001':3, 'SCS2005':3, 'SCS1003':3, 'SCS1002':4, 'SCS2003':3, 'SCS1009':3,'SCS1008':4,'SCS2011':1,'SCS2006':2,'ICT1013':2, 'ICT1012':2, 'ICT1011':3, 'ICT1010':3, 'ICT1015':1, 'ICT1014':1, 'ICT2005':2, 'ICT2006':1, 'ICT2001':3, 'ICT2003':3, 'ICT2002':3, 'ICT2009':2, 'ICT2008':2, 'ICT1001':3, 'ICT1002':3, 'ICT1003':2, 'ICT1004':2, 'ICT1005':2, 'ICT1006':1, 'ICT1007':1, 'ICT1008':1, 'ICT1009':1}<hr>";
  		echo "Drop me an email @ kpgxyz@gmail.com if there is a issue with you results displayed here.";
		//echo "gradeCredits={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,<br>'rA+':2.25,'rA':2.25,'rA-':2.25,'rB+':2.25,'rB':2.25,'rB-':2.25,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}</hr>";
  	}
	mysqli_close($con);
}

?>

<div style="text-align: center"><em><p>I hold no responsibility for the accuracy of the data used in this page. Use this website at your own risk -aela</p></em></div>


</body>

</html>