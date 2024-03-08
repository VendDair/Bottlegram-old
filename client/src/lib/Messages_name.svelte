<script>
  export let name
  import jQuery from "jquery";
  import { url, enc_key } from "../store";
  import { decryptMessage } from "../funcs"
  
  let uuid = localStorage.getItem("uuid")
  
  function request() {
    jQuery.ajax({
      url: $url + "get_messages",
      type: "POST",
      data: JSON.stringify({"uuid": uuid, "sender": name}),
      contentType: "application/json",
      success: function(response) {
        console.log(response)
        const messages = jQuery(".messages")
        messages.empty()
        for (let i = 0; i < response["sender"].length; i++) {
          let p = jQuery("<p>")
          p.text(response["sender"][i] + ": " + decryptMessage(response["text"][i], $enc_key))
          messages.append(p)
        }
      }

    })
  }

  function open_messages() {
    console.log(name)
    let interval = localStorage.getItem("interval")
    if (interval != null) {
      clearInterval(parseInt(interval))
    }
    localStorage.setItem("name", name)
    request()
    let get_messages = setInterval(function() { 
      request()
    }, 1000)
    localStorage.setItem("interval", get_messages)
  }
</script>

<p on:click={open_messages}>{name}</p>

<style lang="scss">
  p {
    color: white;
    margin: 0;
    margin-bottom: 10px;
    &:hover {
      cursor: pointer;
    }
  }

</style>
