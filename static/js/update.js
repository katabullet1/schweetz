$(window).load(function() {
    $("#contactMSG").click(function(){
     $("#myModal").modal();
  });
    var d = new Date();
    var n = d.getUTCFullYear();
    
    document.getElementById("copyRdate").innerHTML = n;
    
});
