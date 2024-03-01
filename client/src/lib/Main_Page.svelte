<script>
  import NewPost from "./New_post.svelte";
  import Post from "./Post.svelte";
  import Error from "./Error.svelte";
  import Name from "./Name.svelte";
  import {new_post, url} from "../store"
  import jQuery from "jquery";
  var base64 = ""
  var titles = ""
  var descriptions = ""
  var ids = ""
  let names = ""
  jQuery(document).ready(function() {
    //const error = new Error({
    //  target: jQuery("main").get()[0],
    //  props: {text: "soss"}
    //})
    jQuery.ajax({
      //url: "http://127.0.0.1:5000/get_posts",
      url: $url + "get_posts",
      type: "POST",
      success: function(response) {
        if (response != "500") {
          titles = response["titles"]
          descriptions = response["descriptions"]
          base64 = response["base64"]
          ids = response["ids"]
          names = response["names"]
        }
        else {
          new Error({
            target: jQuery("main").get()[0],
            props: {text: "Cannot read posts!"}
          })
        }
      }
    })

    jQuery(".reset_url").on("click", function() {
      localStorage.removeItem("url")
      location.reload()
    })
    
    jQuery(".new_post").on("click", function() { 
      new_post.update(value => !value)
    })
  })
</script>

<main class="Main_Page">
  {#if $new_post}
    <NewPost/>
  {/if}
  <div class="header">
    <button class="new_post">New Post</button>
    <button class="reset_url">Reset URL</button>
    <p>Bottlegram</p>
    <Name/>
  </div>
  <div class="posts">
    {#each titles as _, i}
      <Post base64={base64[i]} title={titles[i]} description={descriptions[i]} id={ids[i]} name={names[i]}/>
    {/each}
  </div>

</main>

<style lang="scss">
  .posts {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
    gap: 100px;
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: black;
    padding: 0 2pc;

    .reset_url {
      position: absolute;
      font-size: calc(0.6vw + .6vh);
      left: 20vw;
      border-radius: 10px;
    }

    p {
      color: white;
      font-size: 30px;
      font-family: "Brush Script MT", cursive;
    }

    .new_post {
      font-size: calc(1vw + 1vh);
      border-radius: 10px;
      z-index: 2;
    } 
  }
  @media screen and (orientation:portrait) {
    .posts {
      flex-direction: column;
      gap: 3vw;
    }
    .header {
      padding: 2pc 0;
      flex-direction: column;
    }
  }
  
</style>
