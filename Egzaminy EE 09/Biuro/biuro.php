<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <title>Wycieczki krajoznawcze</title>

    <link rel="stylesheet" href="styl4.css">
</head>

<body>
    <div id="baner">
        <h1>WITAMY W BIURZE PODRÓŻY</h1>
    </div>


    <div id="dane">
        <h3>ARCHIWUM WYCIECZEK</h3>
        <?php
        $pol = mysqli_connect('localhost', 'root', '', 'egzamin4');

        $zap = mysqli_query($pol, "SELECT id, cel, cena FROM wycieczki WHERE dostepna = 0");

        while ($odp = mysqli_fetch_row($zap)) {

            echo $odp[0] . ". " . $odp[1] . ", cena: " . $odp[2] . "<br>";
        }



        mysqli_close($pol);
        ?>
    </div>

    <div id="lewy">
        <h3>NAJTANIEJ</h3>

        <table>
            <tr>
                <td>Włodzy</td>
                <td>od 1200zł</td>
            </tr>
            <tr>
                <td>Francja</td>
                <td>od 1200zł</td>
            </tr>
            <tr>
                <td>Hiszpania</td>
                <td>od 1400zł</td>
            </tr>
        </table>
    </div>
    <div id="srodek">
        <h3>TU BYLIŚMY</h3>

        <?php
        $pol = mysqli_connect('localhost', 'root', '', 'egzamin4');

        $zap = mysqli_query($pol, "SELECT nazwaPliku, podpis FROM zdjecia ORDER BY podpis ASC");

        $row = 0;
        while ($odp = mysqli_fetch_row($zap)) {

            echo "<img src='" . $odp[0] . "' alt='" . $odp[1] . "'>";
        }


        mysqli_close($pol)
        ?>

    </div>
    <div id="prawy">
        <h1>SKONTAKUJ SIĘ</h1>
        <a href="mailto:wycieczki@wycieczki.pl">napisz do nas</a>
        <p>telefon: 555666777</p>
    </div>

    <div id="stopka">
        <p>Stronę wykonał: xyz</p>
    </div>




</body>

</html>