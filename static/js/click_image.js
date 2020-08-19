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