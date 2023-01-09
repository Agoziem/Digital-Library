
// JavaScript code

document.getElementById("search").addEventListener('click', function (e) {
    e.preventDefault();
    let input = document.getElementById('searchbar').value
    input=input.toLowerCase();
    console.log(input)
    let deptname = document.querySelectorAll("#departmentname");
    let deptcards = document.querySelectorAll("#departmentcard");

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

document.getElementById("search1").addEventListener('click', function (e) {
    e.preventDefault();
    let input = document.getElementById('searchbar1').value
    input=input.toLowerCase();
    console.log(input)
    let deptname = document.querySelectorAll("#departmentname");
    let deptcards = document.querySelectorAll("#departmentcard");

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

    
      
    // for (i = 0; i < x.length; i++) { 
    //     if (!x[i].innerHTML.toLowerCase().includes(input)) {
    //         x[i].style.display="none";
    //     }
    //     else {
    //         x[i].style.display="list-item";                 
    //     }
    // }