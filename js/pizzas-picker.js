/* cookies utils */
function setCookie(sName, sValue) {
    var today = new Date(), expires = new Date();
    expires.setTime(today.getTime() + 7200000); // 1 cookie dure 2 heures
    document.cookie = sName + "=" + JSON.stringify(sValue) + ";expires=" + expires.toGMTString();
}


function getCookie(sName) {
    var oRegex = new RegExp("(?:; )?" + sName + "=([^;]*);?");

    if (oRegex.test(document.cookie)) {
        return JSON.parse(RegExp["$1"]);
    } else {
        return null;
    }
}

/* command utils */
function loadCommand(){
    var existing = getCookie('command');
    return (existing!==null) ? existing : {};
}

let command = loadCommand();
function saveCommand(){
    setCookie('command', command);
}

function commandSize(){
    let size = 0;
    for(pizza in command){
        size += command[pizza];
    }
    return size;
}

/* pizza utils */
function addPizza(pizza){
    if(command[pizza]===undefined){
        command[pizza] = 1;
    }else{
        command[pizza]++;
    }
}

function delPizza(pizza){
    if(command[pizza]!==undefined){
        command[pizza]--;
        if(command[pizza]==0){
            delete command[pizza];
        }
    }
}

function addtocart(elt){
    var pizza = elt.parentNode.parentNode.querySelector('[pizza-name]').innerHTML.trim();
    addPizza(pizza);
    saveCommand();
    updateCommandDisplay();
}

function delfromcart(elt){
    console.log('deleting item')
}

/* display utils */
let command_container = document.getElementById('command');

function createRow(pizza, quantity){
    let row = document.createElement('tr');

    let td1 = document.createElement('td');
    let td2 = document.createElement('td');
    let td3 = document.createElement('td');
    let td4 = document.createElement('td');

    td1.innerHTML = pizza;
    td2.innerHTML = 'x'+quantity;
    td3.innerHTML = '<a onclick="decrementfromcart(this)"><i class="fa fa-minus text-warning"></i></a>';
    td4.innerHTML = '<a onclick="delfromcart(this)"><i class="fa fa-times text-danger"></i></a>';

    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);

    command_container.appendChild(row);
}

function updateCommandDisplay(){
    document.getElementById('list-count').innerHTML = commandSize();
    command_container.innerHTML = "";
    for(pizza in command){
        createRow(pizza, command[pizza]);
    }
}

// main
updateCommandDisplay();