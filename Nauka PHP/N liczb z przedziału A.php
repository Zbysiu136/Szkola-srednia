<!doctype html>

<head>
</head>

<body>
    <style>
        #all {
            width: 400px;
            text-align: center;

        }

        #left {
            width: 200px;
        }
    </style>
    <div id="all">
        <form action="index.php" method="POST">
            a = <input type="number" name='a'><br>
            n = <input type="mumber" name='n'><br>
            <input type="submit" value="Generuj">
        </form>
        <div id="left">
            <?php

            $suma = 0;
            $średnia = 0;



            if (isset($_POST['a']) && isset($_POST['n'])) {
                if (empty($_POST['a']) || empty($_POST['n']))
                    echo "Nie podano liczb!";
                else {
                    $a = $_POST['a'];
                    $n = $_POST['n'];


                    echo $n . " - liczb z przedziału (0, " . $a . ") <br>";
                    for ($i = 1; $i <= $n; $i++) {
                        $x = rand(0, $a);
                        $suma = $suma + $x;
                        echo $x . ", ";
                    }
                    echo "<br><br>Suma:" . $suma . "<br>";
                    echo "Średnia:" . $suma / $n . "<br>";
                }
            }
            ?>

        </div>