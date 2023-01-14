<!DOCTYPE html>
<html>

<head>
</head>

<body>
    <form action="index.php" method="POST">
        a = <input type="number" name='a'><br>
        b = <input type="mumber" name='b'><br>
        <input type="submit" value="Generuj">
    </form>

    <?php

    $suma = 0;
    $srednia = 0;
    $count = 0;

    if (isset($_POST['a']) && isset($_POST['b'])) {
        $a = $_POST['a'];
        $b = $_POST['b'];

        for ($i = $a; $i <= $b; $i++) {
            $count = $count + 1;
            $suma = $suma + $i;
            echo ($i . ", ");
        }

        $srednia = $suma / $count;
    }

    echo ("<br>");
    echo ($count);
    echo ("<br>");
    echo ("<br>");
    echo ($suma);
    echo ("<br>");
    echo ($srednia);

    $a = 0;
    $b = 0;

    ?>
</body>

</html>