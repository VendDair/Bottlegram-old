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
    {#if name == localStorage.getItem("name")}
      <div class="delete">x</div>
    {/if}
    <div class="exit">&lt</div>
  </div>
</main>

<script>
  export let base64
  export let title
  export let description
  export let id
  export let name
  import { new_post, url, comments_amount } from "../store"
  import { isWhitespaceString } from "../funcs"
  import Comment from "./Comment.svelte";

  import jQuery, { queue } from "jquery";
  import Error from "./Error.svelte";
  jQuery(document).ready(function() {
    if ($new_post == false) {
      let img = jQuery('.post img[id="' + id + '"]')
      img.on("click", function(e) {
        let comments = img.parent().find("div")[0]
        //let amount = 0
        comments_amount.set(0)

        jQuery.ajax({
          //url: "http://127.0.0.1:5000/get_comments",
          url: $url + "get_comments",
          type: "POST",
          data: JSON.stringify({"id": id}),
          contentType: "application/json",
          headers: {
              "accept": "application/json",
              "Access-Control-Allow-Origin":"*"
          },
          success: function(response) {
            let data = response["data"]
            comments_amount.set(data.length)
            //amount = data.length
            data.forEach(bin => {
              new Comment({
                target: jQuery("section[id='" + id + "']").get()[0],
                props: {text: bin[0], name: bin[2], id_p: bin[3]}
              })
            });
          }
        })






        let repeat = setInterval(function() {
          jQuery.ajax({
            //url: "http://127.0.0.1:5000/get_comments",
            url: $url + "get_comments",
            type: "POST",
            data: JSON.stringify({"id": id}),
            contentType: "application/json",
            headers: {
                "accept": "application/json",
                "Access-Control-Allow-Origin":"*"
            },
            success: function(response) {
              let data = response["data"]
              let length = data.length
              jQuery("section[id='" + id + "']").empty()
              data.forEach(bin => {
                new Comment({
                  target: jQuery("section[id='" + id + "']").get()[0],
                  props: {text: bin[0], name: bin[2], id_p: bin[3]}
                })
              })
              //if ($comments_amount < length) {
              //  data = data.slice($comments_amount)
              //  
              //  comments_amount.set(length)
              //  //amounat = length
              //                
              //  //jQuery("section[id='" + id + "']").empty()
              //
              //  data.forEach(bin => {
              //    new Comment({
              //      target: jQuery("section[id='" + id + "']").get()[0],
              //      props: {text: bin[0], name: bin[2], id_p: bin[3]}
              //    })
              //  })
              //} else if ($comments_amount > length) {
              //  jQuery("section[id='" + id + "']").empty()
              //  data.forEach(bin => {
              //    new Comment({
              //      target: jQuery("section[id='" + id + "']").get()[0],
              //      props: {text: bin[0], name: bin[2], id_p: bin[3]}
              //    })
              //  })}
              //} else if (amount > length){
              //  data = data.slice(0, amount);
              //  let diference = amount - length
              //  let container = jQuery("section[id='" + id + "']").get()[0]


              //}
            }
          })

        }, 1000)

        

        let form_for_new_comment = jQuery(comments).find("form")[0]
        let name = localStorage.getItem("name")
        jQuery(form_for_new_comment).on("submit", function(event) {
          event.preventDefault()
          let input_field = jQuery(form_for_new_comment).find("input")[0]
          const text = jQuery(input_field).val()
          
          if (isWhitespaceString(text)) {
            new Error({
              target: jQuery("main").get()[0],
              props: {text: "Enter the text"}
            })
            return
          }
          jQuery.ajax({
            //url: "http://127.0.0.1:5000/new_comment",
            url: $url + "new_comment",
            type: "POST",
            data: JSON.stringify({
              "text": jQuery(input_field).val(), 
              "id": id,
              "name": name
            }),

            contentType: "application/json",
            success: function(response) {
              if (response != "500") {
                //new Comment({
                //  target: jQuery("section[id='" + id + "']").get()[0],
                //  props: {text: jQuery(input_field).val(), name: name}
                //})
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
          clearInterval(repeat)
        })
        //alert(jQuery(e.target).attr("id"))

        if (name == localStorage.getItem("name")) {
          let delete_btn = jQuery(img.parent()[0].lastChild).find(".delete")
          delete_btn.on("click", function() {
            console.log(id)

            jQuery.ajax({
              url: $url + "delete_post",
              type: "POST",
              data: JSON.stringify({"id": id}),
              contentType: "application/json",
              success: function(response) {
                location.reload()
              }
            })
          })
        }
      })
    }   
  })
</script>

<style lang="scss">
  .post {
    width: 25dvw;
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
      width: 95dvw;
      height: 95dvh;
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
      .delete {
        position: absolute;
        top: 10px;
        left: 50px;
        border-radius: 100%;
        background-color: red;
        padding: 5px 10px;
        transition: all .2s;
        &:hover {
          cursor: pointer;
          color: red;
          background-color: black;
          border: 1px solid red;

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
            width: 80%;
          }

          input, button {
            padding: 5px;
            font-size: calc(1vw + 1vh);
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
        max-height: 90%;
        margin: auto;
      }
    }

    p {
      color: whitesmoke;
      font-size: calc(1vmin + 1pc);
    }

    img {
      margin-top: 5%;
      width: 90%;
      border-radius: 10px;
    }
  }
  @media screen and (orientation:portrait) {
    
    .post {
      width: 90vw;
      .full_info {
        flex-direction: column;
        img {
          max-width: 60%;
          max-height: 100%;
          aspect-ratio: 1/1;
        }
        
        .comments {
          section {
            max-height: 67.5%;
          }
          form {
            width: 100%;
            border-radius: 0 0 10px 10px;
          }
          width: 100%;
          height: 60%;
          border-radius: 10px 0 10px 10px;
        }
      }
    }
  }
</style>
