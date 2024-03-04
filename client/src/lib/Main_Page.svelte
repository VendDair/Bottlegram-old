<script>
  import NewPost from "./New_post.svelte";
  import Post from "./Post.svelte";
  import Error from "./Error.svelte";
  import Name from "./Name.svelte";
  import MessagesPage from "./Messages_Page.svelte";
  import Loading from "./Loading.svelte";
  import {new_post, url, init} from "../store"
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
    const loading = new Loading({
      target: jQuery(".Main_Page").get()[0]
    })
    function get_posts() {
      jQuery.ajax({
        //url: "http://127.0.0.1:5000/get_posts",
        url: $url + "get_posts",
        type: "POST",
        contentType: "application/json",
        success: function(response) {
          if (response != "500") {
            loading.$destroy()
            titles = response["titles"]
            descriptions = response["descriptions"]
            base64 = response["base64"]
            ids = response["ids"]
            names = response["names"]
          }
          else {
            loading.$destroy()
            new Error({
              target: jQuery("main").get()[0],
              props: {text: "Cannot read posts!"}
            })
          }
        }
      })
    }
    get_posts()
    //if ($init != true) {
    //  init.set(true)
    //  jQuery.ajax({
    //    url: $url + "init",
    //    type: "POST",
    //    contentType: "application/json",
    //    success: function(response) {
    //      get_posts()
    //    }
    //  })
    //} else {
    //  get_posts()
    //}
    

    jQuery(".reset_url").on("click", function() {
      localStorage.removeItem("url")
      location.reload()
    })
    
    jQuery(".new_post").on("click", function() { 
      new_post.update(value => !value)
    })

    jQuery(".messages").on("click", function() {
      jQuery(".Main_Page").remove()
      new MessagesPage({
        target: jQuery("body").get()[0]
      })
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
    <button class="messages">Messages</button>
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

    button {
      border-radius: 10px;
    }

    .reset_url {
      font-size: calc(0.2vw + 1pc);
    }

    .messages {
      font-size: calc(0.2vw + 1pc);
    }

    p {
      color: white;
      font-size: 30px;
      font-family: "Brush Script MT", cursive;
    }

    .new_post {
      font-size: calc(0.4vw + 1.2pc);
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
      gap: 10px;

      p {
        margin: 0;
      }
    }
  }
  
</style>
