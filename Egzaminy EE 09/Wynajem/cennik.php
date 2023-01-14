<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <title>Pokoje</title>

    <link rel="stylesheet" href="styl.css">
</head>

<body>
    <div id="baner1">
        <h2>WYNAJEM POKOI</h2>
    </div>

    <div id="menu1"><a href="index.html">POKOJE</a></div>
    <div id="menu2"><a href="cennik.php">CENNIK</a></div>
    <div id="menu3"><a href="kalkulator.html">KALKULATOR</a></div>

    <div id=" baner2"></div>


    <div id="lewy"></div>

    <div id="srodkowy">
        <h1>Cennik</h1>

        <?php

        $pol = mysqli_connect('localhost', 'root', '', 'wynajem');
        $zap = mysqli_query($pol, 'select * from pokoje');


        echo "<table border='1px'>";

        for ($i = 0; $i != 3; $i++) {
            $odp = mysqli_fetch_row($zap);
            echo "<tr>";

            echo "<td>" . $odp[0] . "</td>";
            echo "<td>" . $odp[1] . "</td>";
            echo "<td>" . $odp[2] . "</td>";
            echo "</tr>";
        }

        echo "</table>";


        mysqli_close($pol);

        ?>


    </div>
    <div id="prawy"></div>

    <div id="stopka">
        <p>Stronę opracował: xyz</p>
    </div>

</body>

</html>