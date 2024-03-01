<main class="post {id}">
  <img src={base64} alt="" id={id}>
  <p>{title}</p>

  <div class="full_info a{id}">
    <img src={base64} alt="">
    <div class="comments">

      <div class="description">
        <p>{name}: {description}</p>
      </div>

      <section id={id}>

      </section>

      <form action="submit">
        <input type="text" placeholder="Write your comment">
        <button type="submit">Send</button>
      </form>

    </div>
    <div class="exit">&lt</div>
  </div>
</main>

<script>
  export let base64
  export let title
  export let description
  export let id
  export let name
  import { new_post, url } from "../store"
  import Comment from "./Comment.svelte";

  import jQuery, { data } from "jquery";
    import Error from "./Error.svelte";
  jQuery(document).ready(function() {
    if ($new_post == false) {
      let img = jQuery('.post img[id="' + id + '"]')
      img.on("click", function(e) {
        let comments = img.parent().find("div")[0]
        
        jQuery.ajax({
          //url: "http://127.0.0.1:5000/get_comments",
          url: $url + "/get_comments",
          type: "POST",
          data: JSON.stringify({"id": id}),
          contentType: "application/json",
          headers: {
              "accept": "application/json",
              "Access-Control-Allow-Origin":"*"
          },
          success: function(response) {
            let data = response["data"]
            data.forEach(bin => {
              new Comment({
                target: jQuery("section[id='" + id + "']").get()[0],
                props: {text: bin[0], name: bin[2]}
              })
            });
          }
        })

        let form_for_new_comment = jQuery(comments).find("form")[0]
        let name = localStorage.getItem("name")
        jQuery(form_for_new_comment).on("submit", function(event) {
          event.preventDefault()
          let input_field = jQuery(form_for_new_comment).find("input")[0]
          const text = jQuery(input_field).val()
          const isWhitespaceString = str => !str.replace(/\s/g, '').length
          
          if (isWhitespaceString(text)) {
            new Error({
              target: jQuery("main").get()[0],
              props: {text: "Enter the text"}
            })
            return
          }
          jQuery.ajax({
            //url: "http://127.0.0.1:5000/new_comment",
            url: $url + "/new_comment",
            type: "POST",
            data: JSON.stringify({
              "text": jQuery(input_field).val(), 
              "id": id,
              "name": name
            }),

            contentType: "application/json",
            success: function(response) {
              if (response != "500") {
                new Comment({
                  target: jQuery("section[id='" + id + "']").get()[0],
                  props: {text: jQuery(input_field).val(), name: name}
                })
                jQuery(input_field).val("")
              } else {
                new Error({
                  target: jQuery("main").get()[0],
                  props: {text: "Try Again!"}
                })
              }
            }
          })

          
        })

        jQuery(comments).css("display", "flex")
        let exit = img.parent()[0].lastChild.lastChild
        jQuery(exit).on("click", function() {
          jQuery(comments).css("display", "none")
          jQuery("section[id='" + id + "']").empty()
  
        })
        //alert(jQuery(e.target).attr("id"))
      })
    }   
  })
</script>

<style lang="scss">
  @use 'sass:math';
  $width: math.div(100%, 4);
  .post {
    max-width: $width;
    height: auto;
    background-color: gray;
    border-radius: 10px;
    display: flex;
    align-items: center;
    flex-direction: column;
    margin: 1px;
    transition: all .2s;

    &:hover {
      border: 1px solid red;
      background-color: black;
      margin: 0;
    }

    .full_info {
      position: fixed;
      top: 2.5vh;
      left: 2.5vw;
      width: 95vw;
      height: 95vh;
      border-radius: 10px;
      background-color: gray;
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      z-index: 2;
      display: none;

      .exit {
        position: absolute;
        top: 10px;
        left: 10px;
        border-radius: 100%;
        background-color: white;
        padding: 5px 10px;
        transition: all .2s;
        &:hover {
          cursor: pointer;
          color: white;
          background-color: black;
          border: 1px solid white;
        }
      }

      .comments {
        width: 50%;
        background-color: black;
        height: 100%;
        border-radius: 0 0 10px 0;

        section {
          overflow-y: scroll;
          max-height: 85%;
          p {
            color: white;
          }
        }

        form {
          display: flex;
          justify-content: center;
          align-items: center;
          position: absolute;
          background-color: rgb(40, 40, 40);
          width: 50%;
          height: 10%;
          gap: 10px;
          bottom: 0;
          border-radius: 0 0 10px 0;
          
          input {
            width: 85%;
          }

          input, button {
            padding: 5px;
            font-size: 25px;
            border-radius: 10px;
          }

        }

        .description {
          border-radius: 0 10px 0 0;
          display: flex;
          flex-wrap: wrap;
          justify-content: center;
          width: 95%;
          background-color: rgb(30, 30, 30);
          text-align: justify;
          padding: 0 2.5%;
        }
      }
      
      img {
        max-width: 40%;
        max-height: 100%;
        margin: auto;
        transition: all .2s;
      }
    }

    p {
      color: whitesmoke;
      font-size: 25px;
    }

    img {
      margin-top: 5%;
      width: 90%;
      border-radius: 10px;
    }
  }
</style>
