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


document.getElementById("search2").addEventListener('click', function (e) {
    e.preventDefault();
    let input = document.getElementById('searchbar2').value
    input=input.toLowerCase();
    console.log(input)
    let deptname = document.querySelectorAll("#departmentname1");
    let deptcards = document.querySelectorAll("#departmentcard1");

    deptname.forEach((element,index) => {
        if(element.innerText.toLowerCase().includes(input)){
            deptcards[index].classList.add("d-block")    
        } else {
            deptcards[index].classList.remove("d-block")  
            deptcards[index].classList.add("d-none")  
        }
    })

}
)