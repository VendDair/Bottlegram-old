<script>
  import jQuery from "jquery";
  import {url} from "../store"
  import MainPage from "./Main_Page.svelte";
    import Error from "./Error.svelte";

  let is_url = false
  if (localStorage.getItem("url") != undefined) {
    url.set(localStorage.getItem("url"))
    is_url = true
  }

  jQuery(document).ready(function() {
    jQuery("form").on("submit", function(e) {
      e.preventDefault()
      let input_value = jQuery("input").val()
      url.set(input_value)
      localStorage.setItem("url", input_value)
      
      is_url = true
    })
  })
</script>

{#if !is_url}
  
<form action="submit">
  <input type="text" placeholder="Enter the servel url">
  <button type="submit">Enter</button>
</form>
{:else}
  <MainPage/>
{/if}
<!-- <form action="submit">
  <input type="text" placeholder="Write your comment">
  <button type="submit">Send</button>
</form> -->

<style lang="scss">
  form {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    gap: 10px;
    input, button {
      font-size: 4vw;
    }
  }
</style>
