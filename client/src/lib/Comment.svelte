<script>
  export let text
  export let name
  export let id_p
  import jQuery from "jquery";
  import { url, comments_amount, name_temp } from "../store";
  import { get_current_component } from "svelte/internal";
  const component = get_current_component()
  
  function delete_comment() {
    console.log(jQuery(this).parent())
    console.log(name)
    console.log(text)
    console.log(id_p)
    jQuery.ajax({
      url: $url + "delete_comment",
      type: "POST",
      data: JSON.stringify({"name": name, "text": text, "id_p": id_p}),
      contentType: "application/json",
      success: function(response) {
        component.$destroy()
        comments_amount.update(value => value - 1)
      }
    })
  }
</script>

<div class="container">
  {#if $name_temp == name}
    <div class="delete" on:click={delete_comment}>x</div>
  {/if}
  <p>{name}: {text}</p>
</div>

<style lang="scss">
  .container {
    width: 100%;
    background-color: rgb(40, 40, 40);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin: 10px 0;

    .delete {
      background-color: red;
      border-radius: 100%;
      padding: 5px 10px;
      transition: color .2s;
      &:hover {
        cursor: pointer;
        color: red;
        background-color: black;
        border: 1px solid red;
        padding: 4px 9px;
      
      }
    }

    p {
      color: white;
      word-wrap: anywhere;
      padding: 0 10px;
      font-size: calc(1vmin + .6pc);
    }
  }
</style>
