function show_info(){
    var modal = document.getElementById("modal");
   modal.setAttribute("style", "display: flex;");
};

function hide_info(){
    var modal = document.getElementById("modal");
   
    modal.setAttribute("style", "display: none;");
    
};


window.onload = function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const showShare = urlParams.get('showShare')
    
    if(showShare == 1){
        show_info()
    }
  };

document.addEventListener(
    "click",
    function(event) {
      // If user either clicks X button OR clicks outside the modal window, then close modal by calling closeModal()
        if ( event.target.matches(".btn_close_modal") ||
            event.target.matches(".modal")
        ) {
        hide_info()
        }
        if (event.target.matches(".share_btn")){
        show_info()
        }
    },
    false
  )