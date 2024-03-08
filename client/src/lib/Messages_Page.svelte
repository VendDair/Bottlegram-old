<script>
  import MainPage from "./Main_Page.svelte";
  import Error from "./Error.svelte";
  import Name from "./Name.svelte";
  import MessagesName from "./Messages_name.svelte";
  import { isWhitespaceString, encryptMessage } from "../funcs";
  import { url, enc_key } from "../store"
  import jQuery from "jquery";
  const uuid = localStorage.getItem("uuid")
  jQuery(document).ready(function() {
    jQuery.ajax({
      url: $url + "get_names",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"uuid": uuid}),
      success: function(response) {
        console.log(response)
        response["names"].forEach(name => {
          new MessagesName({
            target: jQuery(".names").get()[0],
            props: {"name": name}
          })
        })
      }
    })



    jQuery(".back").on("click", function() {
      new MainPage({
        target: jQuery("#app").get()[0]
      })
      if (localStorage.getItem("interval") != null) {
        clearInterval(parseInt(localStorage.getItem("interval")))
        localStorage.removeItem("interval")
      }
      jQuery(".Messages_Page").remove()
    })

    jQuery("form").on("submit", function(e) {
      e.preventDefault()

      let name = localStorage.getItem("name")
      let text = jQuery("form .text").val()
      let enc_message = encryptMessage(text, $enc_key)

      if (!localStorage.getItem("name") || isWhitespaceString(name)) {
        new Error({
          target: jQuery(".Messages_Page").get()[0],
          props: {"text": "Unable to get username!"}
        })
        return
      }
      

      jQuery.ajax({
        url: $url + "new_message",
        type: "POST",
        data: JSON.stringify({"text": enc_message, "name": name, "uuid": uuid}),
        contentType: "application/json",
        success: function(response) {
          if (response == "500") {
            new Error({
              target: jQuery(".Messages_Page").get()[0],
              props: {"text": "Cannot send message!"}
            })
            return
          } else if (response == "name not found") {
            new Error({
              target: jQuery(".Messages_Page").get()[0],
              props: {"text": "Enter a valid username!"}
            })
          }
        }
      })
    })
  })
</script>

<main class="Messages_Page">
  <div class="back">&lt</div>
  <div class="name"><Name/></div>
  <div class="container">
    <div class="names"></div>
    <div class="messages"></div>
  </div>
    <form action="submit">
    <input type="password" class="enc_key" bind:value={$enc_key} placeholder="Enter the encryption key">
    <input type="text" class="text" placeholder="Enter your text">
    <button type="submit">Send</button>
  </form>
</main>


<style lang="scss">
  form {
    position: fixed;
    bottom: 10px;
    left: 50vw;
    transform: translateX(-50%);
  }
  .names {
    position: relative;
    padding: 0;
    height: 100dvh;
    background-color: rgb(40, 40, 40);
  }
  .container  {
    display: flex;
  }
  .name {
    width: 100dvw;
    height: 10vh;
    background-color: rgb(20, 20, 20);
    display: flex;
    justify-content: space-around;
    align-items: center;

  }
  .back {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: whitesmoke;
    border-radius: 100%;
    padding: .3vh 1vh;
    font-size: 2dvh;
    transition: all .2s;
    &:hover {
      cursor: pointer;
      background-color: black;
      color: white;
      border: 1px solid white;
    }
  }

</style>
