<script>
  import MainPage from "./Main_Page.svelte";
  import Error from "./Error.svelte";
  import { isWhitespaceString } from "../funcs";
  import { url } from "../store"
  import jQuery from "jquery";

  jQuery(document).ready(function() {
    jQuery(".back").on("click", function() {
      new MainPage({
        target: jQuery("#app").get()[0]
      })
      jQuery(".Messages_Page").remove()
    })

    jQuery("form").on("submit", function(e) {
      e.preventDefault()
      let name = jQuery("form .name").val()
      let text = jQuery("form .text").val()
      let sender = localStorage.getItem("name")
      if (isWhitespaceString(name)) {
        new Error({
          target: jQuery(".Messages_Page").get()[0],
          props: {"text": "Enter the username!"}
        })
        return
      }
      

      jQuery.ajax({
        url: $url + "new_message",
        type: "POST",
        data: JSON.stringify({"text": text, "name": name, "sender": sender}),
        contentType: "application/json",
        success: function(response) {
          if (response == "500") {
            new Error({
              target: jQuery(".Messages_Page").get()[0],
              props: {"text": "Cannot send message!"}
            })
            return
          }
        }
      })
    })
  })
</script>

<main class="Messages_Page">
  <div class="back">&lt</div>
  <form action="submit">
    <input type="text" class="name" placeholder="Enter the username">
    <input type="text" class="text" placeholder="Enter your text">
    <button type="submit">Send</button>
  </form>
</main>


<style lang="scss">
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
