<script>
  import {generate} from "random-words"
  import {url} from "../store"
  import Error from "./Error.svelte";
  import jQuery from "jquery";
  
  let new_name = ""
  function set_name(name) {
    jQuery.ajax({
      url: $url + "set_name",
      type: "POST",
      data: JSON.stringify({"name": name, "uuid": uuid_user}),
      contentType: "application/json",
      success: function(response) {
        if (response != "500") {
          console.log(response)
          return
        }
          //new Error({
          //  target: jQuery(".Main_Page").get()[0],
          //  props: {"text": "Cannot set username!"}
          //})
      }
    })
  }
  //set_name()

  let uuid_user = localStorage.getItem("uuid")
  if (!uuid_user) {
    uuid_user = crypto.randomUUID()
    localStorage.setItem("uuid", uuid_user)
    let words = generate({min:3, max: 5, minLength: 1, maxLength: 3})
    words.forEach(element => {
      new_name += element + "_"
    })
    new_name = new_name.slice(0, -1)
    console.log(uuid_user)
    set_name(new_name)
  } else {
    jQuery.ajax({
      url: $url + "check_name",
      type: "POST",
      data: JSON.stringify({"uuid": uuid_user}),
      contentType: "application/json",
      success: function(response) {
        if (response == "500") {
          let words = generate({min:3, max: 5, minLength: 1, maxLength: 3})
          words.forEach(element => {
            new_name += element + "_"
          })
          new_name = new_name.slice(0, -1)
          set_name(new_name)
          return
        }
        new_name = response["name"]
      }
    })
  }
  
</script>

<main class="name">
  {new_name}
</main>

<style lang="scss">
  main.name {
    color: white;
  }
</style>
