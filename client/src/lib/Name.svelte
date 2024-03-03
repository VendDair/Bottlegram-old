<script>
  import {generate} from "random-words"
  import {url} from "../store"
  import Error from "./Error.svelte";
  import jQuery from "jquery";
  if (localStorage.getItem("name") == null)
  {
    let new_name = ""
    let words = generate({min:3, max: 5, minLength: 1, maxLength: 3})
    words.forEach(element => {
      new_name += element + "_"
    })
    new_name = new_name.slice(0, -1)
    localStorage.setItem("name", new_name)
    jQuery.ajax({
      url: $url + "set_name",
      type: "POST",
      data: JSON.stringify({"name": new_name}),
      contentType: "application/json",
      success: function(response) {
        if (response == "500") {
          new Error({
            target: jQuery(".Main_Page").get()[0],
            props: {"text": "Cannot set username!"}
          })
        }
      }
    })
  }
</script>

<main class="name">
  {localStorage.getItem("name")}
</main>

<style lang="scss">
  main.name {
    color: white;
  }
</style>
