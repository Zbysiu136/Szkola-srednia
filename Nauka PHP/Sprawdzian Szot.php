<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta lang="pl">
    </head>
    <body>
        
<?php
//1
$n = rand(10,100);

//2
$tab = array();
$lewo = array();
$prawo = array();

$l = 0;
$p = 0;
for($i=0; $i!=$n; $i++){
    $tab[$i] = rand(1,100);
    
    if($tab[$i]<=50){
    $lewo[$l] = $tab[$i];
    $l = $l + 1;
    }
    
    else if($tab[$i]>=51){
    $prawo[$p] = $tab[$i];
    $p = $p + 1;
    }
}

echo "Ilość liczb ".$n;
echo "<br><br>";

echo "liczby mniejszeod 50: <br>";
for ($j=0; $j!=$l; $j++)
echo $lewo[$j]."<br>";
echo "<br><br>";

echo "liczby większe od 50: <br>";
for ($j=0; $j!=$p; $j++)
echo $prawo[$j]."<br>";

?>
   
</body>
</html>