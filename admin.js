
 $(document).ready(function(){
var refreshIntervalId = null; var value;

function djform(){
document.getElementById("id_adminname").style.visibility = "hidden";
document.getElementById("id_roomnum").style.visibility = "hidden";
document.getElementById("id_reso").style.visibility = "hidden";
document.getElementById("btni").style.visibility = "hidden";
}
djform();

$("#insro").click(function(){
                $("#listreq").empty();
                $("#maincont").empty();
                    for (var i = 1; i < 9999; i++)
             {clearInterval(refreshIntervalId);}
              alert("stopped");

document.getElementById("id_adminname").style.visibility = "visible";
document.getElementById("id_roomnum").style.visibility = "visible";
document.getElementById("id_reso").style.visibility = "visible";
document.getElementById("btni").style.visibility = "visible";

});
$(document).on('click', 'button', function(e){

   let dec = this.id;
   let first = dec.charAt(0);
   let second = dec.replaceAll('a', '').replaceAll('r', '');
   alert(second);
   let number;
   for(let i=1;i<=value-1;i++)
   {
      if(i==parseInt(second)){
         number=i;
         break;
      }
   }
   if(first == "a"){
    let name = $("#"+number).text();

     $.ajax({
              type: "GET",
              url: "/acc", //url of site no need to enter full site
              dataType: "json",

              contentType: 'application/json',
                data :{  'name' : name,

                      },
                success: function(response){
                   alert(response.res);
                }




     });


   }
   else {  let name = $("#"+number).text();
            $.ajax({
              type: "GET",
              url: "/rej", //url of site no need to enter full site
              dataType: "json",

              contentType: 'application/json',
                data :{  'name' : name,

                      },
                success: function(response){
                   alert(response.res);
                }




     });



   }

});


$("#rq1").click(function(){
  djform();
  refreshIntervalId = setInterval(function(){
 $.ajax({
            type: "GET",
            url: "/rq1", //url of site no need to enter full site
           dataType: "json",

            contentType: 'application/json',

            success: function (response) {
                $("#listreq").empty();
                $("#maincont").empty();

                 value= 1;
                for(var key in response.rqs){
               //  var temp= "<li>"+response.rqs[key].name+"</li>";
                 var temp =response.rqs[key].name;
                 var li = document.createElement("li");
                 var bttn = document.createElement("button");
                 var bttn1 = document.createElement("button");
                 var div = document.createElement("div");
                 var div1 = document.createElement("div");
                 var div2 = document.createElement("div");
                 var he = document.createElement("h1");
                 he.append(response.rqs[key].rm);
                 div2.append(he);
                 div2.setAttribute("class","reqroom");
                 div.setAttribute("class","round1");
                 div.setAttribute("id","da"+value);
                 bttn.setAttribute("id","a" + value)
                 bttn.textContent="🗸"
                 div1.setAttribute("class","round2");
                 div1.setAttribute("id","dr"+value);
                 bttn1.setAttribute("id","r" + value)

                 bttn1.textContent="✖"
                 div.append(bttn);
                 div1.append(bttn1);


                 li.setAttribute('id',value);
                 value++;
                 li.append(temp);
                  $("#listreq").append(li);
                  $("#listreq").append(div);
                     $("#listreq").append(div1);
                      $("#listreq").append(div2);
                 // $("#listreq").append(li)



                }


// Gives value of flag
            },

            error: function (response) {
                   alert(window.location.href);
            }
        });

},5000);

});

  $("#strq").click(function(){
            for (var i = 1; i < 9999; i++)
             {clearInterval(refreshIntervalId);}
              alert("stopped");
                  });

  $("#acrec").click(function(){
     djform();
    $.ajax({
            type: "GET",
            url: "/recac", //url of site no need to enter full site
           dataType: "json",

            contentType: 'application/json',

            success: function (response) {
               console.log(response.areqs);
                for (var i = 1; i < 9999; i++)
             {clearInterval(refreshIntervalId);}

                  $("#listreq").empty();
                $("#maincont").empty();


                var mainc = document.createElement("div");
                mainc.setAttribute("id","container2");
                $("#maincont").append(mainc);
                for (var key in  response.areqs){
                  var temp = response.areqs[key].room;
                  var temp2 = response.areqs[key].name;
                  var he = document.createElement("h1");
                  he.setAttribute("class","records");
                  he.append(temp2+"------"+temp);
                  $("#container2").append(he);

                }
           }
    });
   });
  });