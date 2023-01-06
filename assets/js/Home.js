var tabButtons = document.querySelectorAll(".tabContainer .buttonContainer a")
var tabPanels = document.querySelectorAll(".tabContainer .tabPanel")

function showPanel(panelIndex){
    tabButtons.forEach(function(node){
        node.classList.remove('active')
    });
    tabButtons[panelIndex].classList.add('active')
    
    tabPanels.forEach(function(node){
        node.style.display='none'
    })

    tabPanels[panelIndex].style.display="block";

}

showPanel(0);