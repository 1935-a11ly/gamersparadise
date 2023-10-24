/* jshint esversion: 8 */
'use strict';
const BASE_URL =  "https://mycallmusa01.pythonanywhere.com/api/games/"

async function quick_suggestion() {
    var plat = document.getElementById("selPlatt").value;
    var fetchedSuggestions= await fetch(`${BASE_URL}/${plat}`)
    .then(response => response.json());
    let suggRow=document.querySelector("#response")
    for (let suggestions in fetchedSuggestions){
        let suggDiv=document.createElement("div");
        suggDiv.setAttribute("class", "mui-container mui--text-center");
        suggDiv.setAttribute("style", "width:57%;margin-top:20px;background-color: #4CAF50; /* Green */border: none;color: white;padding: 15px 32px;text-align: center;font-size: 16px;");
        suggDiv.innerHTML=fetchedSuggestions[suggestions];
        suggRow.appendChild(suggDiv);
        setTimeout(function() {
            suggDiv.style.display = "none";
          }, 8500);
        }}