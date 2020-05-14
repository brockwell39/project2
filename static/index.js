document.addEventListener("DOMContentLoaded",function(){
  document.getElementById("bbutton").addEventListener("click",function(event){
    event.preventDefault()
    const request = new XMLHttpRequest;
    const user = document.querySelector("#user").value;

    request.open('POST','/check');

    request.onload = function(){

      const data = JSON.parse(request.responseText);

      if(data.success){
        document.getElementById('index').submit();
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
  });
});

function myfunc(){
  alert("test")
  document.getElementById("channel").addEventListener("click",function(event){
    event.preventDefault()
    const request = new XMLHttpRequest;
    const user = document.querySelector("#user").value;

    request.open('POST','/channelcheck');

    request.onload = function(){

      const data = JSON.parse(request.responseText);

      if(data.success){
        document.getElementById('channel').submit();
      }
      else{
        document.getElementById('channel').reset();
        alert("That channel is in use");
      }
    }
    const data = new FormData();
    data.append('user',user);

    request.send(data);
    return false;
  });
};
