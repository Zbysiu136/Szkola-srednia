<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <title>Kwiaty</title>

    <link rel="stylesheet" href="styl.css">
</head>

<body>
    <div id="header">
        <h1>Moje kwiaty</h1>
    </div>

    <div id="lewy">
        <h3>Kwiaty dla Ciebie!</h3>
        <a href="https://www.swiatkwiatow.pl/">Rozpoznaj kwiaty</a><br>
        <a href="znajdz.php">Znajdź kwiaciarnię</a><br>
        <img src="gozdzik.png" alt="Goździk" id="img">
    </div>
    <div id="prawy">
        <img src="gerbera.png" alt="gerbera">
        <img src="gozdzik.png" alt="gozdzik">
        <img src="roza.png" alt="róża">

        <p>Podaj miejscowość, w której poszukujesz kwiaciarni: </p>
        <form action="znajdz.php" method="POST">
            <input type="text" name="a">
            <input type="submit" value="SPRAWDŹ">

        </form>
        <div id="wynik"></div>
        <?php

        if (isset($_POST['a'])) {
            $a = $_POST['a'];

            $pol = mysqli_connect('localhost', 'root', '', 'kwiaciarnia');
            $zap = mysqli_query($pol, "SELECT `nazwa`, `ulica` FROM kwiaciarnie WHERE `miasto` = '$a' ");

            $odp = mysqli_fetch_row($zap);

            echo $odp[0];
            echo " ";
            echo $odp[1];
        }




        ?>
    </div>
    <div id="foter">
        <h3>Stronę opracował: xyz</h3>
    </div>

</body>

</html>