<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <title>Forum o psach</title>

    <link rel="stylesheet" href="styl.css">
</head>

<body>
    <?php

    if (isset($_POST['a'])) {
        $a = $_POST['a'];
        $pol = mysqli_connect('localhost', 'root', '', 'forumpsy');
        $zap = mysqli_query($pol, "INSERT INTO `odpowiedzi`(`Pytania_id`, `konta_id`, `odpowiedz`) VALUES ('1','5','" . $a . "')");
        mysqli_close($pol);
    }




    ?>

    <div id="baner">
        <h1>Forum miłośników psów</h1>
    </div>

    <div id="lewy">
        <img src="Avatar.png" alt="Użytkownik forum">

        <?php
        $pol = mysqli_connect('localhost', 'root', '', 'forumpsy');
        $zap = mysqli_query($pol, "SELECT konta.nick, konta.postow, pytania.pytanie FROM konta INNER JOIN pytania ON konta.id = pytania.konta_id WHERE konta.id = 1");
        while ($odp = mysqli_fetch_row($zap)) {
            echo "<h4>Użytkownik: " . $odp[0] . "</h4><p>" . $odp[1] . " postów na forum</p><p>" . $odp[2];
        }

        mysqli_close($pol)

        ?>

        <video src="video.mp4" loop id="video"></video>
    </div>
    <div id="prawy">
        <form action="index.php" method="post" id="form">
            <textarea rows="4" cols="40" name="a"></textarea><br>
            <input type="submit" value="Dodaj odpowiedź" id="button">
        </form>
        <h2>Odpowiedzi na pytanie</h2>

        <?php
        $pol = mysqli_connect('localhost', 'root', '', 'forumpsy');
        $zap = mysqli_query($pol, "SELECT konta.nick, konta.postow, pytania.pytanie FROM konta INNER JOIN pytania ON konta.id = pytania.konta_id;");
        echo "<ol>";
        while ($odp = mysqli_fetch_row($zap)) {

            echo "<li>" . $odp[2] . " " . $odp[0] . "</li><hr>";
        }
        echo "</ol>";
        mysqli_close($pol);



        ?>
    </div>

    <div id="stopka">
        Autor: xyz <a href="http://mojestrony.pl/" target="_blank" rel="noopener noreferrer">Zobacz nasze relacje</a>
    </div>
</body>

</html>