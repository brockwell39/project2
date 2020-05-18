
if(!(localStorage.getItem('user'))){
    window.location.href = "http://127.0.0.1:5000/newuser";
  }
if(localStorage.getItem('user')){
      user = localStorage.getItem('user');
      document.getElementById('user').innerHTML = user;
    }





function func1(){
    const request = new XMLHttpRequest;
    const user = document.querySelector("#user").value;
    if(user != ''){
    request.open('POST','/check');

    request.onload = function(){

      const data = JSON.parse(request.responseText);

      if(data.success){
        document.getElementById('index').submit();
        localStorage.setItem('user',user);
      }
      else{
        document.getElementById('index').reset();
        alert("That username is in use");
      }
    }
    const data = new FormData();
    data.append('user',user);

    request.send(data);
    return false;
   }
   else{
     document.getElementById('index').reset();
     alert("Please enter a username")
   };
  };

function func2(){
      const request = new XMLHttpRequest;
      const channel = document.querySelector("#channel").value;
      if(channel != ''){
      request.open('POST','/channelcheck');

      request.onload = function(){

        const data = JSON.parse(request.responseText);

        if(data.success){
          document.getElementById('channelf').submit();
        }
        else{
          document.getElementById('channelf').reset();
          alert("That channel name is in use");
        }
      }
      const data = new FormData();
      data.append('channel',channel);

      request.send(data);
      return false;
     }
     else{
       document.getElementById('channelf').reset();
       alert("Please enter a channel name")
     };
    };

var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
function chat1(){
  var user = localStorage.getItem('user');
  socket.on('connect');
  const message = document.getElementById('message').value;
  socket.emit('chat', {'message': message,'user':user});
  document.getElementById('chatf').reset();
};

socket.on('announce message',function(data){
  document.querySelector('#Textarea1').innerHTML='';
  var i;
for (i = 0; i < data.length; i++) {
  let li = data[i] + "\n";

  document.querySelector('#Textarea1').append(li);
  };
});
