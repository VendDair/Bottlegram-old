<script>
  import NewPost from "./lib/New_post.svelte";
  import Post from "./lib/Post.svelte";
  import Error from "./lib/Error.svelte";
  import {new_post} from "./store"
  import jQuery from "jquery";
  var base64 = ""
  var titles = ""
  var descriptions = ""
  var ids = ""
  jQuery(document).ready(function() {
    //const error = new Error({
    //  target: jQuery("main").get()[0],
    //  props: {text: "soss"}
    //})
    jQuery.ajax({
      url: "http://127.0.0.1:5000/get_posts",
      type: "POST",
      success: function(response) {
        if (response != "500") {
          titles = response["titles"]
          descriptions = response["descriptions"]
          base64 = response["base64"]
          ids = response["ids"]
        }
        else {
          new Error({
            target: jQuery("main").get()[0],
            props: {text: "Cannot read posts!"}
          })
        }
      }
    })



    jQuery(".new_post").on("click", function() { 
      new_post.update(value => !value)
      //new_post = !new_post
    })
  })
</script>

<main>
  {#if $new_post}
    <NewPost/>
  {/if}
  <div class="header">
    <button class="new_post">New Post</button>
    <p>Bottlegram</p>
  </div>
  <div class="posts">
    {#each titles as _, i}
      <Post base64={base64[i]} title={titles[i]} description={descriptions[i]} id={ids[i]}/>
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
    justify-content: center;
    align-items: center;
    background-color: black;

    p {
      color: white;
      font-size: 30px;
      font-family: "Brush Script MT", cursive;
    }

    .new_post {
      position: absolute;
      left: 30px;
      font-size: 25px;
      border-radius: 10px;
      z-index: 2;
    }
  }
  
</style>
