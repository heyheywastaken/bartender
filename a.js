var input=document.getElementById('searchinput');
input.addEventListener('keypress',function(event){
    if (event.key=='Enter'){
        event.preventDefault();
        document.getElementById('searchbut').click();
    }
});