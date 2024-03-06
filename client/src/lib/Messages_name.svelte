<script>
  export let sender
  import jQuery, { data } from "jquery";
  import { url } from "../store";

  function set_messages(sender_list, text_list) {
    const messages_container = jQuery(".messages")
    messages_container.empty()
    for (let i = 0; i < sender_list.length; i++) {
      let message = jQuery("<p>")
      message.text(sender_list[i] + ": " + text_list[i])
      messages_container.append(message)

    }
  }
  const uuid = localStorage.getItem("uuid")
  jQuery(document).ready(function() {
    jQuery("p." + sender).on("click", function() {
      jQuery.ajax({
        url: $url + "get_messages",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"uuid": uuid, "sender": sender}),
        success: function(response) {
          if (localStorage.getItem("interval") != null) {
            clearInterval(parseInt(localStorage.getItem("interval")))
            localStorage.removeItem("interval")
          }
          let sender_message = response["sender"]
          let text = response["text"]
          console.log(sender_message)
          console.log(text)
          set_messages(sender_message, text)
          //const messages_container = jQuery(".messages")
          //messages_container.empty()
          //for (let i = 0; i < sender_message.length; i++) {
          //  let message = jQuery("<p>")
          //  message.text(sender_message[i] + ": " + text[i])
          //  messages_container.append(message)
          //}
          let repeat = setInterval(function() {
            jQuery.ajax({
              url: $url + "get_messages",
              type: "POST",
              data: JSON.stringify({"uuid": uuid, "sender": sender}),
              contentType: "application/json",
              success: function(response) {
                set_messages(response["sender"], response["text"])
              }
            })
            
          }, 2000)
          console.log(repeat)
          localStorage.setItem("interval", repeat.toString())
        }
      })
    })
  })
  //jQuery(document).ready(function() {
  //  jQuery("p").on("click", function() {
  //    console.log(this)
  //  })
  //})
</script>

<p class={sender}>{sender}</p>

<style lang="scss">
  p {
    color: white;
    padding: 0;
    margin: 0;
    transition: all .2s;
    &:hover {
      cursor: pointer;
      color: black;
      text-shadow: -1px -1px white, 1px 1px white;
      
    }
  }

</style>
