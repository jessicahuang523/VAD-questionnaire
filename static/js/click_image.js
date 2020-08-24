var best, worst;

function showBorder(id){
    var name = id.charAt(0);
    var tags = document.getElementsByName(name);
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
    var raID = id.concat("-ra");
    document.getElementById(id).style.borderColor="red";
    document.getElementById(id).style.borderStyle="solid";
    document.getElementById(raID).checked = true;

    if(name == "b"){
        best = document.getElementById(raID).value;
    }
    else if(name == "w"){
        worst = document.getElementById(raID).value;
    }

    val(best, worst);
}

function val(b, w){
    if(b!=undefined && w!=undefined && b!=w){
        console.log(b,w);
        document.getElementsByTagName("button")[0].disabled = false;
    }
    else{
        document.getElementsByTagName("button")[0].disabled = true;
    }
}