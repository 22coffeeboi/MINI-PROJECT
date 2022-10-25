$(document).ready(function(){
var value; var response2;

  $.ajax({
            type: "GET",
            url: "/room", //url of site no need to enter full site
           dataType: "json",

            contentType: 'application/json',
             success: function (response) {
                 response2=response;
                console.log(response.rooms);
                $("#container").empty();
                  value= 1;
                 for(var key in response.rooms){
                 var temp =response.rooms[key].name;
                 var bttn2 = document.createElement("button");
                 var bttn = document.createElement("button");
                 var div = document.createElement("div");
                 var divbn = document.createElement("div");
                 var divbn2 = document.createElement("div");
                 var he = document.createElement("h1");
                 bttn2.textContent="i";
                 bttn2.setAttribute("id","in"+value);

                 divbn2.setAttribute("class","bttn2");
                 divbn2.append(bttn2);
                 div.setAttribute("class","card1");
                 div.setAttribute("id","c"+value);
                 he.setAttribute("class","text1");
                 he.setAttribute("id","r"+value);
                 he.append(temp);
                 div.append(he);
                 divbn.setAttribute("class","bttn1");
                 bttn.textContent="BOOK";
                 bttn.setAttribute("id","b"+value);
                 divbn.append(bttn);
                 div.append(divbn);
                 div.append(divbn2);
                 $("#container").append(div);
                 value++;
                 }
                 const loader = document.querySelector(".loader .loading--ease-spin");
                 loader.style.animationPlayState = 'paused';
                 loader.style.visibility = 'hidden';



                 console.log(loader);


                }
       });
$("#master").empty();
$(document).on('click', '.bttn2 button', function(e){
    var bn1 =this.id;
  var bnc1 = bn1.replaceAll('in', '');

  var room1 =$("#"+"r"+bnc1).text();
  var str;

  for(var keys in response2.rooms){
      var matchroom = JSON.stringify(response2.rooms[keys]); //stringifys he current key starting from 0
      var matchroom1 = JSON.parse(matchroom); // parse the json string
      var matchroom2 = JSON.stringify(matchroom1.name); // stringyfy the name
      var res = JSON.stringify(matchroom1.resource); // stringify the resource
      // matchroom2=matchroom2.slice(1,5);   // method 1 for removing quotations
      matchroom2=matchroom2.replaceAll('"', ''); // method 2 f removing quoatations
      console.log(escape(matchroom2));
     if(room1 == matchroom2){
       // alert(matchroom2);

       str= res;
       str =str.replaceAll('"', '');
       str=str.replaceAll(/\\n/g, '\n').replaceAll(/\\r/g, '\r');
       // str =str.replaceAll('\\', '');
      // alert(str);
       break;
     }
  }
  if(document.getElementById("c"+bnc1).classList.contains('cardinfo')){
     document.getElementById("c"+bnc1).className = "card1";
     document.getElementById("in"+bnc1).textContent="i";
     var rm = document.getElementById("c"+bnc1);
     var rm2 = document.getElementById("c"+bnc1).lastChild;
     rm.removeChild(rm2);

  }
  else{
     document.getElementById("c"+bnc1).className = "cardinfo";
     document.getElementById("in"+bnc1).textContent="x";
     let div = document.createElement("div");
     let hr = document.createElement("p");
     hr.append(str);
     div.setAttribute("class","cardres");
     div.append(hr);
     $("#c"+bnc1).append(div);


   }

});

$(document).on('click', '.bttn1 button', function(e){
   let bn = this.id;
   let bnc = bn.replaceAll('b', '');
   let room = $("#"+"r"+bnc).text();
   let user = $("#uuserid").text();
       user = user.split("welcome|").pop();
   const loader = document.querySelector(".loader .loading--ease-spin");
                 loader.style.animationPlayState = 'running';
                 loader.style.visibility = 'visible';


    $.ajax({

                 type: "GET",
              url: "/book", //url of site no need to enter full site
              dataType: "json",

              contentType: 'application/json',
                data :{  'room' : room,
                         'name' : user,


                      },
                success: function(response){


                   $("#pend").empty();
                    loader.style.animationPlayState = 'paused';
                     loader.style.visibility = 'hidden';
                   var temp = "Pending : 1";
                   $("#pend").append(temp);

                }









    });


});






 });