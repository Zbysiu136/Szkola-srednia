<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <title>Mój kalendarz</title>

    <link rel="stylesheet" href="styl5.css">
</head>

<body>

    <?php
    $pol = mysqli_connect('localhost', 'root', '', 'egzamin5');

    if (isset($_POST['a'])) {
        $a = $_POST['a'];
        mysqli_query($pol, "UPDATE `zadania` SET wpis = '" . $a . "' WHERE dataZadania = '2020-07-13'");
        //Bo kwerenda aktualuzuje dane, gdyby aktualizacja danych była po ich wyświetleniu działała by dopiero po własnoręcznym odświerzeniu
    }
    mysqli_close($pol);
    ?>


    <div id="baner1">
        <img src="logo1.png" alt="Mój kalendarz">
    </div>
    <div id="baner2">
        <h1>KALENDARZ</h1>
        <?php

        $pol = mysqli_connect('localhost', 'root', '', 'egzamin5');
        $zap = mysqli_query($pol, "SELECT miesiac, rok FROM zadania WHERE dataZadania = '2020-07-01'");

        while ($odp = mysqli_fetch_row($zap)) {
            echo "<h3>miesiąć: " . $odp[0] . ", rok:" . $odp[1];
        }

        mysqli_close($pol);

        ?>

    </div>

    <div id="main">

        <?php


        $pol = mysqli_connect('localhost', 'root', '', 'egzamin5');
        $zap = mysqli_query($pol, "SELECT dataZadania, wpis FROM zadania WHERE miesiac = 'lipiec'");

        while ($odp = mysqli_fetch_row($zap)) {
            echo "<div class='blok'><h5>" . $odp[0] . "</h5><p>" . $odp[1] . "</p></div>";
        }


        mysqli_close($pol);
        ?>
    </div>

    <div id="stopka">
        <form action="kalendarz.php" method="post">
            dodaj wpis: <input type="text" name="a">
            <input type="submit" value="DODAJ">
        </form>


        <p>Stronę wykonał: xyz</p>
    </div>
</body>

</html>