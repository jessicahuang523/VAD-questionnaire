function showBorder(id){
    orgID = id.slice(0, -2);
    tags = document.getElementsByName(orgID);
    for (t=0; t<tags.length; t++){
        tag = tags[t]
        if(tag.style.borderColor == "red"){
            tag.style.borderColor=null;
        }
        if(tag.style.borderStyle == "solid"){
            tag.style.borderStyle=null;
        }
        if(tag.checked == true){
            tag.checked == false;
        }
    }
    raID = id.concat("-ra");
    document.getElementById(id).style.borderColor="red";
    document.getElementById(id).style.borderStyle="solid";
    document.getElementById(raID).checked = true;
}

function validate(dim){
    var best, worst;
    bName = dim + "-b";
    wName = dim + "-w";
    bList = document.getElementsByName(bName);
    wList = document.getElementsByName(wName);
    for (b=0; b<bList.length; b++){
        if(bList[b].checked == true){
            best = bList[b];
            break;
        }
    }
    for (w=0; w<wList.length; w++){
        if(wList[w].checked == true){
            worst = wList[w];
            break;
        }
    }
    if(best==null || worst==null){
        alert("You have to answer both questions!");
    }
    if(best.value == worst.value){
        alert("Please choose two different GIFs!");
    }
}