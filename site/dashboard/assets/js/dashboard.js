const btn_agencia1 = document.getElementById("btn_ag1")
const btn_agencia2 = document.getElementById("btn_ag2")
const btn_agencia3 = document.getElementById("btn_ag3")
const btn_agencia4 = document.getElementById("btn_ag4")

function agencia1() {

    const grafico1 = document.querySelector("#grafico_ag1");
    const grafico2 = document.querySelector("#grafico_ag2");
    const grafico3 = document.querySelector("#grafico_ag3");
    const grafico4 = document.querySelector("#grafico_ag4");

    const grafico_class1 = document.querySelector(".grafico_ag1")[0];
    const grafico_class2 = document.querySelector(".grafico_ag2")[1];
    const grafico_class3 = document.querySelector(".grafico_ag3")[2];
    const grafico_class4 = document.querySelector(".grafico_ag4")[3];

    grafico1.style.display = "block";
    grafico2.style.display = "none";
    grafico3.style.display = "none";
    grafico4.style.display = "none";

    grafico_class1.style.display = "block";
    grafico_class2.style.display = "none";
    grafico_class3.style.display = "none";
    grafico_class4.style.display = "none";

}

function agencia2() {

    const grafico1 = document.querySelector("#grafico_ag1")[0];
    const grafico2 = document.querySelector("#grafico_ag2")[1];
    const grafico3 = document.querySelector("#grafico_ag3")[2];
    const grafico4 = document.querySelector("#grafico_ag4")[3];

    const grafico_class1 = document.querySelector(".grafico_ag1");
    const grafico_class2 = document.querySelector(".grafico_ag2");
    const grafico_class3 = document.querySelector(".grafico_ag3");
    const grafico_class4 = document.querySelector(".grafico_ag4");

    grafico1.style.display = "none";
    grafico2.style.display = "block";
    grafico3.style.display = "none";
    grafico4.style.display = "none";

    grafico_class1.style.display = "none";
    grafico_class2.style.display = "block";
    grafico_class3.style.display = "none";
    grafico_class4.style.display = "none";
}
function agencia3() {

    const grafico1 = document.querySelector("#grafico_ag1");
    const grafico2 = document.querySelector("#grafico_ag2");
    const grafico3 = document.querySelector("#grafico_ag3");
    const grafico4 = document.querySelector("#grafico_ag4");

    const grafico_class1 = document.querySelector(".grafico_ag1");
    const grafico_class2 = document.querySelector(".grafico_ag2");
    const grafico_class3 = document.querySelector(".grafico_ag3");
    const grafico_class4 = document.querySelector(".grafico_ag4");

    grafico1.style.display = "none";
    grafico2.style.display = "none";
    grafico3.style.display = "block";
    grafico4.style.display = "none";

    grafico_class1.style.display = "none";
    grafico_class2.style.display = "none";
    grafico_class3.style.display = "block";
    grafico_class4.style.display = "none";
}

function agencia4() {

    const grafico1 = document.querySelector("#grafico_ag1");
    const grafico2 = document.querySelector("#grafico_ag2");
    const grafico3 = document.querySelector("#grafico_ag3");
    const grafico4 = document.querySelector("#grafico_ag4");
    
    const grafico_class1 = document.querySelector(".grafico_ag1");
    const grafico_class2 = document.querySelector(".grafico_ag2");
    const grafico_class3 = document.querySelector(".grafico_ag3");
    const grafico_class4 = document.querySelector(".grafico_ag4");

    grafico1.style.display = "none";
    grafico2.style.display = "none";
    grafico3.style.display = "none";
    grafico4.style.display = "block";

    grafico_class1.style.display = "none";
    grafico_class2.style.display = "none";
    grafico_class3.style.display = "none";
    grafico_class4.style.display = "block";
}