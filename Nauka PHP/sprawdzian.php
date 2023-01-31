<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
</head>
<body>

<?php

function licz($a,$b){

$tab = array();

$lewo = array();
$prawo = array();

$p = 0;
$l = 0;


for($i=0; $i!=$a; $i++){
    $tab[$i] = rand(1,$b);

    if($tab[$i]%2==1){
    $lewo[$l] = $tab[$i];
    $l = $l +1;
    }

    else if($tab[$i]%2==0){
    $prawo[$p] = $tab[$i];
    $p = $p +1;
    }
}

echo "liczby nieparzyste <br>";
for($i=0; $i!=$l; $i++)
echo $lewo[$i]."<br>";

echo "<br><br>";

echo "liczby parzyste <br>";
for($i=0; $i!=$p; $i++)
echo $prawo[$i]."<br>";

}

licz(10,10)

?>



</body>
</html>