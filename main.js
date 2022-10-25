var flag1 = document.getElementById('hd1').value;
if (!flag1.localeCompare("reject")) {
document.getElementById('sh1').style.animationPlayState="paused";
document.getElementById('sh1').style.boxShadow = "0px -10px 30px 0px red";
document.getElementById('inval1').style.visibility="visible";
}

$("#contact").click(function(){
if(document.getElementById("maincount").classList.contains('countroom')){
    he = document.createElement("h1");
   pe = document.createElement("p");
   linebreak = document.createElement("br");
    linebreak1 = document.createElement("br");
     linebreak2 = document.createElement("br");
      linebreak3 = document.createElement("br");
   pe.append("Email : allenanand2001@gmail.com ");
   pe.append(linebreak);
   pe.append("Email : 2coffeeboi2@gmail.com ");
   pe.append(linebreak1);
   pe.append("Email : nidhiya2001@gmail.com");
      pe.append(linebreak2);
   pe.append("Email : collinstp23@gmail.com");
   pe.append(linebreak3);
    pe.append("Phone : 32423423");
   he.setAttribute("id","rmcc");
   he.append("CONTACT");
   $("#maincount").append(he);
   $("#maincount").append(pe);


  document.getElementById("maincount").className = "countroom1";
}
else{ $("#rmcc").remove();
      $("p").remove();
      document.getElementById("maincount").className = "countroom";

}


});

$("#news").click(function(){
if(document.getElementById("maincount").classList.contains('countroom')){

     he = document.createElement("h1");
   pe = document.createElement("p");
   linebreak = document.createElement("br");
  linebreak1 = document.createElement("br");
  linebreak2 = document.createElement("br");
    linebreak3 = document.createElement("br");
     linebreak4 = document.createElement("br");
       linebreak5 = document.createElement("br");
   pe.append("---CHANGE LOG : VERSION 1.1---");
   pe.append(linebreak);
   pe.append("---ROOM AVAIL VIEW ON HOME---");
   pe.append(linebreak1);
   pe.append("---CONTACT AND NEWS---");
      pe.append(linebreak2);
       pe.append("---BOOKED ROOMS WONT BE DISPLAYED---");
       pe.append(linebreak3);
        pe.append("---AUTOMATIC REJECTION:ADMIN PANEL---");
        pe.append(linebreak4);
         pe.append("---NEW USER AND ADMIN UI---");
         pe.append(linebreak5);
              pe.append("---EXCEL EXPORT ADDED :ADMIN PANEL---");
   he.setAttribute("id","rmcc");
   he.append("NEWS");
   $("#maincount").append(he);
   $("#maincount").append(pe);



   document.getElementById("maincount").className = "countroom1";


}
else{ $("#rmcc").remove();
      $("p").remove();
      document.getElementById("maincount").className = "countroom";

}


});