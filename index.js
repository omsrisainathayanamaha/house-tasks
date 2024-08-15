/*
XMLHttpRequest template
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    var data = {"identifier": MY_IDENTIFIER, "player": player, "option": option}
    xhr.onreadystatechange = function ()
*/
const SHOWN = "display:block;";
const HIDDEN = "display:none;";
function profileServer()
{
    var name = document.getElementById('name').value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    var data = {"username":name};
    xhr.onreadystatechange = function()
    {
        if(xhr.readyState == 4 && xhr.status == 200)
        {
            /*should send me the all the Person data plus the list of unfinished tasks
            */
           var response = xhr.responseText;
        }
    }
    xhr.send(data);
}