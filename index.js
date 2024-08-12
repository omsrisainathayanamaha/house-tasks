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
            /*should send me the following data:
            Total Service Hours - Cleaning (lifetime)
            Total Service Hours - Kitchen (this week)
            Service Hours - Cleaning (this week)
            Service Hours - Kitchen (this week)
            Service Hours - Cleaning Required (this week)
            Service Hours - Kitchen Required (this week)
            Task List - Cleaning (each has a name, time required, and date string)
            Task List - Kitchen (each has a name, time required, and date string)
            
            */
        }
    }
    xhr.send(data);
}