var x=0;
function f1(){ //Funkcja odpowiadająca za podmianę pierwszego zdania
    
    if(x==0){
    document.getElementById("txt1").innerHTML = "Twierdzenie mówi: <br> Jeśli trójkąt jest prostokątny, to suma kwadratów długości przyprostokątnych jest równa kwadratowi długości przeciwprostokątnej <------(klikni)"
    document.getElementById('jpg1').src = 'pic1.png'
    x=1}
    else if(x==1){
    document.getElementById("txt1").innerHTML = "Czym jest twierdzenie pitagorasa? <------(klikni)"
    document.getElementById('jpg1').src = ''
    x=0}
}


var y=0
function f2(){ //Funkcja odpowiadająca za podmianę drugiego zdania

    if(y==0){
    document.getElementById("txt2").innerHTML = "Obliczanie długość przeciwprostokątnej poniższego trójkąta prostokątnego <------(klikni)"
    document.getElementById('jpg2').src = 'pic2.png'
    document.getElementById('txt3').innerHTML = 'Wynik to: <br> 4<sup>2</sup>+3<sup>2</sup>=c<sup>2</sup><br>16 + 9 = c<sup>2</sup><br>25 = c<sup>2</sup><br>c = 5 '
    y=1}

    else if(y==1){
    document.getElementById("txt2").innerHTML = "Jak to wygląda w praktyce? <------(klikni)"
    document.getElementById('jpg2').src = ''
    document.getElementById("txt3").innerHTML = "" 
    document.getElementById('txt3').innerHTML = ''
    y=0}
}


function f3(){ //Kalkulator 1
    var a = document.getElementById("a").value
    var b = document.getElementById("b").value
    c = Math.pow(a,2)+Math.pow(b,2)  
    c = Math.sqrt(c)
    document.getElementById("c").value = c
}

function f4(){ //Kalkulator 2
    var a2 = document.getElementById("a2").value
    var b2 = document.getElementById("b2").value
    c2 = Math.pow(a2,2)-Math.pow(b2,2) 
    c2 = Math.abs(c2) 
    c2 = Math.sqrt(c2)
    document.getElementById("c2").value = c2
}

