<script>
  export let sender
  import jQuery from "jquery";
  import { url } from "../store";
  const name = localStorage.getItem("name")
  jQuery(document).ready(function() {
    jQuery("p." + sender).on("click", function() {
      jQuery.ajax({
        url: $url + "get_messages",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"name": name, "sender": sender}),
        success: function(response) {
          console.log(response)
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
