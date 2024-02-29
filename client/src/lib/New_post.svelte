<script>
  import jQuery from "jquery";
  import Error from "./Error.svelte";
  import Loading from "./Loading.svelte";
  
  jQuery(document).ready(function() {
    jQuery(".submit").on("click", function() {
      const file = jQuery(".image")[0].files[0]
      
      const loading = new Loading({
        target: jQuery("main").get()[0]
      })

      const reader = new FileReader()
      reader.onload = function(e) {
        const base64 = e.target.result

        jQuery.ajax({
          url: "http://127.0.0.1:5000/new_post",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify({
            "title": jQuery(".title").val(),
            "description": jQuery(".description").val(),
            "base64": base64
          }),
          headers: {
              "accept": "application/json",
              "Access-Control-Allow-Origin":"*"
          },
          success: function(response) {
            if (response == "200") {
              location.reload()
            }
            else {
              new Error({
                target: jQuery("main").get()[0],
                props: {text: "Try Again!"}
              })
            }
            loading.$destroy()
          }
        })

      }
      reader.readAsDataURL(file)
    })
  })
</script>

<main class="main">
  <div class="bg"></div>
  <h2 class="center">New Post</h2>
  
  <div class="form center">

    <input type="text" class="title font" placeholder="title">
    <input type="text" class="description font" placeholder="description">
    <input type="file" class="image font" accept="image/*" style="color: white;">
    <button class="font submit">Submit</button>

  </div>
</main>


<style lang="scss">
  .font {
    font-size: 20px;
  }

  .main {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 1;
    display: flex;
    justify-content: center;
    align-items: center;

    .form {
      display: flex;
      flex-direction: column;
      gap: 20px;
      top: 50%;
      z-index: 2;
    }

    h2 {
      position: absolute;
      top: 10px;
      color: white;
      font-family: "Brush Script MT", cursive;
      font-size: 35px;
    }

    .bg {
      top: 0;
      left: 0;
      position: absolute;
      width: 100%;
      height: 100%;
      opacity: 0.7;
      background-color: black;
    }
  }
</style>
